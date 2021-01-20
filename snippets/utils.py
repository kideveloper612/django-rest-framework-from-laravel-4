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

from datetime import timedelta
from django.utils import timezone


class FooException(Exception):
    def __init__(self, foo):
        self.foo = foo


def PaymentHelper_couponPayment(couponCode, user, plan, payment):
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

    isValid = PaymentHelper_isValidToPromotion(payment['type'], couponCode)
    if not isValid['isValid']:
        return response

    isValid = CouponHelper_isValid(couponCode, plan, user)
    if not isValid['isValid']:
        return response

    calculated = CouponHelper_calculate(couponCode, plan)

    i = 0
    # while True:
    #     if i < calculated['recurrences']:
    #         break

    return response


def PaymentHelper_defaultPayment(user, plan, payment):
    pass


def CouponHelper_isValid(coupon_code, plan, user):
    try:
        coupon_Code = CouponCode.objects.filter(code=coupon_code, status=1, validity_date__gt=timezone.now())
        if not coupon_Code:
            raise FooException("Código de cupom inválido e/ou expirado.")

        coupon = Coupon.objects.filter(id=coupon_Code[0].coupon, end_date__gte=timezone.now(), start_date__lte=timezone.now(), status=1)
        if not coupon:
            raise FooException("Código de cupom expirado.")

        promotion = Promotion.objects.filter(id=coupon[0].promotion, end_date__gte=timezone.now(), start_date__lt=timezone.now(), status=1)
        if not promotion:
            raise FooException("Esta promoção já foi finalizada.")

        promotionPlan = PromotionPlan.objects.filter(plan=plan.id, promotion=promotion[0].id)
        if not promotionPlan:
            raise FooException("Este cupom não é válido para o plano escolhido.")

        coupon_usage_limit = coupon_Code[0].usage_limit
        coupon_count = CouponUsage.objects.filter(coupon=coupon_Code[0].coupon).__len__()
        coupon_usage_model = CouponUsage.objects.filter(user=user, coupon_code=coupon[0].id)

        response = {
            "error": False,
            "isValid": True,
            "message": "Cupom válido"
        }

        if (coupon_usage_limit != 0 and coupon_count > coupon_usage_limit) or coupon_usage_model \
                .__len__() > 0:
            response = {
                "error": False,
                "isValid": False,
                "message": "Limite de uso excedido para este cupom."
            }

    except FooException as e:
        response = {
            "error": True,
            "isValid": False,
            "message": e.foo
        }

    finally:
        return response


def CouponHelper_calculate(couponCode, plan):
    response = {}
    try:
        coupon_code = CouponCode.objects.get(code=couponCode)
        if not coupon_code:
            raise FooException("Erro ao calcular desconto")

        coupon = Coupon.objects.get(id=coupon_code['id'])
        if not coupon:
            raise FooException("Erro ao calcular desconto")

        promotion = Promotion.objects.get(id=coupon['id'])
        if not promotion:
            raise FooException("Erro ao calcular desconto")

        if promotion['discount_type'] == "%":
            response = {
                "amountInCents": plan['price'] - (plan['price'] * (promotion['discount_amount']/100))
            }
        elif promotion['discount_type'] == "v":
            response = {
                "amountInCents": plan['price'] - promotion['discount_amount']
            }
        else:
            response = {
                "amountInCents": ""
            }

        response.update({
            "name": promotion['name'],
            "description": promotion['description'],
            "rule": promotion['rule'],
            "recurrences": promotion['recurrences'],
        })

    except FooException as e:
        response = e.foo

    finally:
        return response


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


def PaymentHelper_isValid(paymentType, plan):
    data = {
        "error": False,
        "isValid": True,
        "message": ""
    }
    try:
        paymentType_model = PaymentType.objects.filter(id=paymentType.id, status=1)

        if not paymentType_model:
            raise FooException("Método de pagamento inválido e/ou inativo.")

        planPaymentType_model = PlanPaymentType.objects.filter(plan=plan.id)
        if not planPaymentType_model:
            raise FooException("Este plano não aceita este metódo de pagamento")

        data.update({
            "message": "Pagamento válido"
        })

    except FooException as e:
        data.update({
            "message": e.foo
        })

    finally:
        return data


def PaymentHelper_isValidToPromotion(paymentType, couponCode):
    response = {
        "error": False,
        "isValid": True,
        "message": "Pagamento válido para está promoção"
    }
    try:
        couponCode = CouponCode.objects.get(code=couponCode)
        if not couponCode:
            raise FooException("Código de cupom inválido e/ou expirado.")

        if not Coupon.objects.all():
            raise FooException("cupom inválido e/ou expirado.")

        if not Promotion.objects.all():
            raise FooException("Não existe promoção cadastrada para esse cupom")

        promotionPaymentType = PromotionPaymentType.objects.filter(payment_type=paymentType)
        if not promotionPaymentType:
            raise FooException("Não é possível utilizar este cupom para este metodo de pagamento")

    except FooException as e:
        response.update({
            "error": True,
            "isValid": False,
            "message": e.foo
        })

    finally:
        return response


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
