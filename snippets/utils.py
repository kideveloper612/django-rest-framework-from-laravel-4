from snippets.models import AccessLog
from snippets.models import AccessLogArchive
from snippets.models import Address
from snippets.models import AddressCity
from snippets.models import AddressCountry
from snippets.models import AddressDistrict
from snippets.models import AddressState
from snippets.models import Advertising
from snippets.models import AdvertisingPage
from snippets.models import AdvertisingSpot
from snippets.models import AdvertisingType
from snippets.models import AdvertisingZone
from snippets.models import Api
from snippets.models import AuthGroup
from snippets.models import AuthGroupPermissions
from snippets.models import AuthPermission
from snippets.models import AuthUser
from snippets.models import AuthUserGroups
from snippets.models import AuthUserUserPermissions
from snippets.models import Campaign
from snippets.models import Category
from snippets.models import Condition
from snippets.models import Coupon
from snippets.models import CouponCode
from snippets.models import CouponUsage
from snippets.models import Device
from snippets.models import DjangoAdminLog
from snippets.models import DjangoContentType
from snippets.models import DjangoMigrations
from snippets.models import DjangoSession
from snippets.models import Email
from snippets.models import EmailContext
from snippets.models import EmailQueue
from snippets.models import Feed
from snippets.models import FeedMedia
from snippets.models import FeedMessage
from snippets.models import FeedMessageOption
from snippets.models import Media
from snippets.models import Menu
from snippets.models import News
from snippets.models import NewsMedia
from snippets.models import Notification
from snippets.models import NotificationFilter
from snippets.models import NotificationStatus
from snippets.models import Order
from snippets.models import OrderData
from snippets.models import OrderItem
from snippets.models import OrderLog
from snippets.models import OrderPayment
from snippets.models import OrderPaymentCallback
from snippets.models import OrderPaymentRequest
from snippets.models import OrderStatus
from snippets.models import Partner
from snippets.models import PartnerCategory
from snippets.models import PaymentAcquirer
from snippets.models import PaymentGateway
from snippets.models import PaymentMethod
from snippets.models import PaymentStatus
from snippets.models import PaymentType
from snippets.models import Permission
from snippets.models import Plan
from snippets.models import PlanPaymentType
from snippets.models import PlanResource
from snippets.models import PlanSpot
from snippets.models import Promotion
from snippets.models import PromotionPaymentType
from snippets.models import PromotionPlan
from snippets.models import PushQueue
from snippets.models import Resource
from snippets.models import Route
from snippets.models import Session
from snippets.models import Setting
from snippets.models import SmsQueue
from snippets.models import Sport
from snippets.models import Spot
from snippets.models import Subscription
from snippets.models import SubscriptionLog
from snippets.models import Tide
from snippets.models import TideData
from snippets.models import User
from snippets.models import UserGroup
from snippets.models import UserGroupMenu
from snippets.models import UserGroupPermission
from snippets.models import UserPayment
from snippets.models import UserSport
from snippets.models import UserSpot
from snippets.models import UserSpotBasicPlan
from snippets.models import UserUserGroup

from datetime import timedelta, datetime
from django.utils import timezone

from snippets import helper


def PaymentHelper_couponPayment(request, couponCode, user, plan, payment):
    response = {
        "error": True,
        "message": "Falha ao realizar pagamento!"
    }

    if Order.objects.filter(user=user.id, created_at__gt=timezone.now()-timedelta(seconds=5)):
        response = {
            "error": True,
            "message": "Já existe um pedido em processamento!"
        }
        return response

    isValid = helper.PaymentHelper_isValidToPromotion(payment['type'], couponCode)
    if not isValid['isValid']:
        return response

    isValid = helper.CouponHelper_isValid(couponCode, plan, user)
    if not isValid['isValid']:
        return response

    calculated = helper.CouponHelper_calculate(couponCode, plan)

    i = 0
    while True:
        order = Order(
            order_status=OrderStatus.objects.first(),
            user=User.objects.get(pk=user.id),
            created_at=timezone.now(),
            total=plan.price,
            total_paid=plan.price,
            total_pending=int(calculated['amountInCents']),
            total_discounted=plan.price - int(calculated['amountInCents']),
            note="Pedido realizado por " + request.user.email,
            ip_address=helper.get_client_ip(request)
        )
        order.save()

        orderLog = OrderLog(
            order=order,
            created_at=timezone.now(),
            description="Pedido criado!",
            ip_address=helper.get_client_ip(request)
        )
        orderLog.save()

        orderData = OrderData(
            order=order,
            user_name=user.name,
            user_email=user.email,
            user_cell_phone=user.cell_phone,
            user_doc_cpf=user.doc_cpf,
            user_address_street=payment['addressStreet'],
            user_address_number=payment['addressNumber'],
            user_address_complement=payment['addressComplement'],
            user_address_district=payment['addressDistrict'],
            user_address_city=payment['addressCity'],
            user_address_state=payment['addressState'],
            user_address_country=payment['addressCountry'],
            user_address_zip_code=payment['addressZipCode']
        )
        orderData.save()

        orderItem = OrderItem(
            order=order,
            plan=plan,
            quantity=1,
            price=plan.price
        )
        orderItem.save()

        orderPayment = OrderPayment(
            order=order,
            payment_gateway=PaymentGateway.objects.first(),
            payment_status=PaymentStatus.objects.first(),
            created_at=timezone.now()
        )
        if payment['type'] == 1:
            orderPayment.credit_card_date = datetime.strptime("01/{}".format(payment['date']), "%d/%m/%y")
        orderPayment.save()

        options = {
            "orderId": order.id,
            "orderPaymentId": orderPayment.id,
            "amountInCents": calculated['amountInCents'],
            "isAuth": False
        }

        useGateway = True
        if payment['type'] == 1:
            paymentType = PaymentType.objects.get(pk=payment['type'])
            paymentMethod = PaymentMethod.objects.get(integration_code=paymentType.integration_code)

            if paymentMethod.tax * 100 > options['amountInCents']:
                useGateway = False

            if i == 0:
                orderPayment.order = order
                orderPayment.payment_method = paymentMethod
                orderPayment.payment_gateway = PaymentGateway.objects.first()
                orderPayment.amount = options['amountInCents']
                orderPayment.captured_date = timezone.now()
                orderPayment.due_date = timezone.now()
                orderPayment.payment_status = PaymentStatus.objects.first()
                orderPayment.note = "Não foi realizada requisição para mundipagg pois o valor do final do pedido é " \
                                    "menor que a taxa do boleto "
                order.order_status = OrderStatus.objects.first()
                order.total_pending = 0
                orderItem.applied = 1

                order.save()
                orderItem.save()
                orderPayment.save()

                helper.CouponHelper_register(orderItem, couponCode, user)

                plan.couponCode = couponCode

                helper.Subscription_updateSubscription(request, user, plan)
            else:
                if plan.free_days > 0 and helper.Subscription_hasSubscription(request, user) and \
                        helper.CouponHelper_isAccumulative(couponCode):
                    orderPayment.due_date = timezone.now() + timedelta(plan.free_days + plan.days * i)
                else:
                    orderPayment.due_date = timezone.now() + timedelta(plan.days * i)

                order.order_status = OrderStatus.objects.first()
                order.save()
                orderPayment.save()

            if i == 0:
                response = {
                    "error": False,
                    "message": "",
                    "order": order
                }

        if i == 0 and useGateway is True:
            helperResponse = helper.MundiPaggHelper_doPayment(user, payment, options)
            if not isinstance(helperResponse, list):
                instantBuyKey = None
                maskedCreditCardNumber = None
                slipOurNumber = None
                slipBarCode = None
                slipUrl = None
                authorizationCode = None
                creditCardBrand = None
                transactionKey = None
                instantBuyKey = None

                # if payment['type'] == 2:


        i += 1

        if calculated['recurrences'] is None:
            break
        elif calculated['recurrences'] is not None and i < int(calculated['recurrences']):
            break

    return response


def PaymentHelper_defaultPayment(user, plan, payment):
    pass


def PaymentHelper_checkPayment(payment):
    data = {
        "error": False,
        "isValid": True,
        "message": "pagamento válido"
    }

    if payment['type'] == 1:
        data.update({
            "error": True,
            "isValid": False
        })
        if payment['addressStreet'] == "":
            data.update({
                "message": "É preciso preencher um nome de endereço válido"
            })
        elif payment['addressNumber'] == "":
            data.update({
                "message": "É preciso preencher um numero de endereço válido"
            })
        elif payment['addressDistrict'] == "":
            data.update({
                "message": "É preciso preencher um nome de bairro válido"
            })
        elif payment['addressCity'] == "":
            data.update({
                "message": "É preciso preencher um nome de cidade válido"
            })
        elif payment['addressState'] == "":
            data.update({
                "message": "É preciso preencher um nome de estado válido"
            })
        elif payment['addressZipCode'] == "":
            data.update({
                "message": "É preciso preencher um endereço postal válido"
            })
    elif payment['type'] == 2:
        data.update({
            "error": True,
            "isValid": False
        })
        if payment['number'] == "":
            data.update({
                "message": "É preciso preencher um numero de cartão válido"
            })
        elif payment['holder'] == "":
            data.update({
                "message": "É preciso preencher um nome de usuário válido"
            })
        elif payment['date'] == "":
            data.update({
                "message": "É preciso preencher uma data de vencimento válida"
            })
        elif payment['security'] == "":
            data.update({
                "message": "É preciso preencher um código de segurança válido"
            })

    return data


