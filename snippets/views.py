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

from snippets.serializers import AddressStateSerializer
from snippets.serializers import AddressCitySerializer
from snippets.serializers import AddressDistrictSerializer
from snippets.serializers import FeedSerializer
from snippets.serializers import PlanSerializer
from snippets.serializers import SportSerializer
from snippets.serializers import SpotSerializer
from snippets.serializers import UserSpotSerializer
from snippets.serializers import UserSportSerializer
from snippets.serializers import SubscriptionSerializer
from snippets.serializers import ActivationCodeSerializer
from snippets.serializers import SpotConditionSerializer
from snippets.serializers import SpotTideSerializer
from snippets.serializers import SpotAdvertisingSerializer
from snippets.serializers import SettingSerializer
from snippets.serializers import UserSerializer
from snippets.serializers import CouponSerializer
from snippets.serializers import PromotionSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.forms.models import model_to_dict
import os
from random import randint
from datetime import datetime
from snippets import utils
from snippets import helper
from snippets.helper import FooException
from django.db import connection
from django.contrib.auth.hashers import make_password
from django.utils import timezone

cursor = connection.cursor()


@api_view(['POST'])
def user_device(request):
    statusCode = status.HTTP_200_OK

    response = {
        "error": False,
        "user": []
    }

    try:
        user = ""
        token = ""
        appVersion = ""

        if 'user' in request.data:
            user = request.data['user']
        if 'code' in request.data:
            code = request.data['code']
        else:
            raise FooException("O código do dispositivo é requerido!")
        if 'token' in request.data:
            token = request.data['token']
        if 'appVersion' in request.data:
            appVersion = request.data['appVersion']

        device = Device.objects.get(code=code)
        if not device:
            device = Device()

        if not device.token and not token:
            token = code

        device.os = request.user.is_authenticated
        if user:
            device.user = user
        if code:
            device.code = code
        if token:
            device.token = token
        if appVersion:
            device.app_version = appVersion
        device.status = 1

        device.save()

        if device.user:
            subscription = Subscription.objects.get(user=device.user)

            if subscription and

    except Exception as e:
        if hasattr(e, 'message'):
            response = {
                "error": True,
                "message": str(e.message)
            }
        else:
            response = {
                "error": True,
                "message": str(e)
            }
        statusCode = status.HTTP_400_BAD_REQUEST
    finally:
        return Response(response, statusCode)


@api_view(['POST'])
def user_logout(request):
    statusCode = status.HTTP_200_OK

    responseData = {
        "error": False,
        "user": []
    }

    try:
        deviceCode = ""
        if 'device-code' in request.headers:
            deviceCode = request.headers['device-code']
        elif 'deviceCode' in request.data:
            deviceCode = request.data['deviceCode']

        device = Device.objects.get(code=deviceCode)

        if device:
            device.user = None
            device.save()

    except Exception as e:
        if hasattr(e, 'message'):
            responseData = {
                "error": True,
                "message": str(e.message)
            }
        else:
            responseData = {
                "error": True,
                "message": str(e)
            }

        statusCode = status.HTTP_400_BAD_REQUEST

    finally:
        return Response(responseData, statusCode)


@api_view(['POST'])
def user_login(request):
    response = {
        "error": False,
        "user": []
    }
    statusCode = status.HTTP_200_OK

    try:
        keywords = ['email', 'password']
        check = all(item in list(request.data.keys()) for item in keywords)
        if not check:
            response = {
                "error": False,
                "message": "All fields are required"
            }

            statusCode = status.HTTP_400_BAD_REQUEST

            return

        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email)
        if user:
            if user[0].status == 2:
                serializer = UserSerializer(user, many=True)
                response.update({
                    "user": serializer.data
                })
            else:
                user = User.objects.filter(email=email, password=make_password(password, salt=None, hasher='unsalted_md5'))
                serializer = UserSerializer(user, many=True)

                if user:
                    response.update({
                        "user": serializer.data
                    })
                else:
                    response.update({
                        "error": True,
                        "message": "Senha incorreta"
                    })
        else:
            response.update({
                "error": True,
                "message": "Usuário não encontrado"
            })

    except Exception as e:
        if hasattr(e, 'message'):
            response = {
                "error": True,
                "message": str(e.message)
            }
        else:
            response = {
                "error": True,
                "message": str(e)
            }

        statusCode = status.HTTP_400_BAD_REQUEST

    finally:
        return Response(response, statusCode)


@api_view(['POST'])
def user_update_sport(request):
    response = {
        "error": False,
        "message": ""
    }
    statusCode = status.HTTP_200_OK

    try:
        keywords = ['user', 'sport']
        check = all(item in list(request.data.keys()) for item in keywords)
        if not check:
            response = {
                "error": False,
                "message": "All fields are required"
            }

            statusCode = status.HTTP_400_BAD_REQUEST

            return

        user = request.data['user']
        sport = request.data['sport']

        userSport = UserSport.objects.filter(user=user, sport=sport)

        if userSport:
            userSport.delete()
            response.update({
                "message": "Favorito removido"
            })
        else:
            user = User.objects.get(pk=user)
            sport = Sport.objects.get(pk=sport)
            UserSport(
                user=user,
                sport=sport
            ).save()

            response.update({
                "message": "Favorito adicionado"
            })

    except Exception as e:
        if hasattr(e, 'message'):
            response = {
                "error": True,
                "message": str(e.message)
            }
        else:
            response = {
                "error": True,
                "message": str(e)
            }

        statusCode = status.HTTP_400_BAD_REQUEST

    finally:
        return Response(response, statusCode)


@api_view(['POST'])
def user_update_spot(request):
    response = {
        "error": False,
        "message": ""
    }
    statusCode = status.HTTP_200_OK

    try:
        keywords = ['user', 'spot']
        check = all(item in list(request.data.keys()) for item in keywords)
        if not check:
            response = {
                "error": False,
                "message": "All fields are required"
            }

            statusCode = status.HTTP_400_BAD_REQUEST

            return

        user = request.data['user']
        spot = request.data['spot']

        userSpot = UserSpot.objects.filter(user=user, spot=spot)

        if userSpot:
            userSpot.delete()
            response.update({
                "message": "Favorito removido"
            })
        else:
            user = User.objects.get(pk=user)
            spot = Spot.objects.get(pk=spot)
            UserSpot(
                user=user,
                spot=spot
            ).save()

            response.update({
                "message": "Favorito adicionado"
            })

    except Exception as e:
        if hasattr(e, 'message'):
            response = {
                "error": True,
                "message": str(e.message)
            }
        else:
            response = {
                "error": True,
                "message": str(e)
            }

        statusCode = status.HTTP_400_BAD_REQUEST

    finally:
        return Response(response, statusCode)


@api_view(['POST'])
def user_update(request):
    response = {
        "error": False,
        "message": ""
    }
    statusCode = status.HTTP_200_OK

    try:
        keywords = ['id', 'facebookId', 'name', 'email', 'cellPhone', 'password', 'sendEmail', 'sendPush', 'sendSms']
        check = all(item in list(request.data.keys()) for item in keywords)
        if not check:
            response = {
                "error": False,
                "message": "All fields are required"
            }

            statusCode = status.HTTP_400_BAD_REQUEST

            return

        if 'status' in request.POST:
            status_value = request.data['status']
        else:
            status_value = 1

        id_value = request.data['id']
        facebookId = request.data['facebookId']
        name = request.data['name']
        email = request.data['email']
        cellPhone = request.data['cellPhone']
        password = request.data['password']
        sendEmail = request.data['sendEmail']
        sendPush = request.data['sendPush']
        sendSms = request.data['sendSms']

        if id_value:
            user = User.objects.filter(email=email)
            if user:
                response.update({
                    "message": "Este email já está sendo utilizado!"
                })
            else:
                user = User.objects.filter(pk=id_value)

                email = email.strip()
                user.update(
                    updated_at=timezone.now(),
                    facebook_id=facebookId,
                    name=name,
                    email=email,
                    cell_phone=cellPhone,
                    password=make_password(password, salt=None, hasher='unsalted_md5'),
                    send_email=sendEmail,
                    send_push=sendPush,
                    send_sms=sendSms
                )

                response.update({
                    "message": "Dados Atualizados"
                })
        else:
            user = User.objects.filter(email=email)
            if user:
                response.update({
                    "message": "Este email já está sendo utilizado!"
                })
            else:
                exitLoop = False

                activationCode = 0

                while exitLoop:
                    activationCode = randint(0000000000, 9999999999)
                    user = User.objects.get(activation_code=activationCode)
                    if user:
                        exitLoop = False
                    else:
                        exitLoop = True

                if email:
                    user = User(
                        created_at=timezone.now(),
                        updated_at=timezone.now(),
                        facebook_id=facebookId,
                        name=name,
                        email=email,
                        cell_phone=cellPhone,
                        password=make_password(password, salt=None, hasher='unsalted_md5'),
                        send_email=sendEmail,
                        send_push=sendPush,
                        send_sms=sendSms,
                        status=status_value
                    )

                    if not user.facebook_id:
                        user.activation_code = None
                    else:
                        user.activation_code = activationCode

                    user.save()

                    response.update({
                        "message": "Cadastro realizado com sucesso!"
                    })

                else:
                    response.update({
                        "message": "O campo de email não pode estar em branco!"
                    })

    except Exception as e:
        if hasattr(e, 'message'):
            response = {
                "error": True,
                "message": str(e.message)
            }
        else:
            response = {
                "error": True,
                "message": str(e)
            }

        statusCode = status.HTTP_400_BAD_REQUEST

        current_path = os.path.join(os.path.join(os.path.dirname(__file__), "storage"), "user.txt")
        with open(file=current_path, encoding="utf-8", mode="a") as file:
            file.write(str(e) + "\n")

    finally:
        return Response(response, statusCode)


@api_view(['POST'])
def payment_buy(request):
    user = request.data['user']
    cpf = request.data['cpf']
    plain = request.data['plain']
    plan = request.data['plan']
    if 'paymentType' in request.POST:
        paymentType = request.data['paymentType']
    else:
        paymentType = 2
    if 'cardHolder' in request.POST:
        cardHolder = request.data['cardHolder']
    else:
        cardHolder = None
    if 'cardNumber' in request.POST:
        cardNumber = request.data['cardNumber']
    else:
        cardNumber = None
    if 'cardSecurity' in request.POST:
        cardSecurity = request.data['cardSecurity']
    else:
        cardSecurity = None
    if 'cardDate' in request.POST:
        cardDate = request.data['cardDate']
    else:
        cardDate = "01/20"
    if 'addressStreet' in request.POST:
        addressStreet = request.data['addressStreet']
    else:
        addressStreet = None
    if 'addressNumber' in request.POST:
        addressNumber = request.data['addressNumber']
    else:
        addressNumber = None
    if 'addressComplement' in request.POST:
        addressComplement = request.data['addressComplement']
    else:
        addressComplement = None
    if 'addressDistrict' in request.POST:
        addressDistrict = request.data['addressDistrict']
    else:
        addressDistrict = None
    if 'addressCity' in request.POST:
        addressCity = request.data['addressCity']
    else:
        addressCity = None
    if 'addressState' in request.POST:
        addressState = request.data['addressState']
    else:
        addressState = None
    if 'addressCountry' in request.POST:
        addressCountry = request.data['addressCountry']
    else:
        addressCountry = None
    if 'addressZipCode' in request.POST:
        addressZipCode = request.data['addressZipCode']
    else:
        addressZipCode = None
    if 'couponCode' in request.POST:
        couponCode = request.data['couponCode']
    else:
        couponCode = None
    if 'instantBuyKey' in request.POST:
        instantBuyKey = request.data['instantBuyKey']
    else:
        instantBuyKey = None
    spotId = request.data['spotId']

    response = {
        "error": False,
        "message": ""
    }
    status_code = status.HTTP_200_OK
    try:
        user = User.objects.filter(id=user)
        user.update(doc_cpf=cpf)

        if not user:
            raise FooException("Not Found User")

        plan = Plan.objects.get(id=plan)

        if not plan:
            raise FooException("Not Found Plan")

        paymentType = PaymentType.objects.get(id=paymentType)
        if not paymentType:
            raise FooException("Not Found PaymentType")

        is_valid = helper.PaymentHelper_isValid(paymentType, plan)
        if not is_valid['isValid']:
            return Response(is_valid)

        payment = {
            "type": paymentType.id,
            "number": cardNumber,
            "holder": cardHolder,
            "date": cardDate,
            "security": cardSecurity,
            "addressStreet": addressStreet,
            "addressNumber": addressNumber,
            "addressComplement": addressComplement,
            "addressDistrict": addressDistrict,
            "addressCity": addressCity,
            "addressState": addressState,
            "addressCountry": addressCountry,
            "addressZipCode": addressZipCode,
            "instantBuyKey": instantBuyKey,
            "spotId": spotId,
        }

        if instantBuyKey == "":
            checkPayment = utils.PaymentHelper_checkPayment(payment)
            if not checkPayment['isValid']:
                response = checkPayment

        if couponCode != "":
            response = utils.PaymentHelper_couponPayment(request, couponCode, user[0], plan, payment)
        else:
            response = utils.PaymentHelper_defaultPayment(user[0], plan, payment)

    except FooException as e:
        print(e)
        status_code = status.HTTP_202_ACCEPTED
        response.update({
            "error": True,
            "message": e.foo
        })

    except Exception as e:
        if hasattr(e, 'message'):
            response.update({
                "error": True,
                "message": str(e.message)
            })
        else:
            response.update({
                "error": True,
                "message": str(e)
            })

    finally:
        return Response(response, status_code)


@api_view(['POST'])
def coupon_check(request):
    if request.method == 'POST':
        try:
            keywords = ['user', 'plan', 'couponCode', 'paymentType']
            check = all(item in list(request.data.keys()) for item in keywords)
            if not check:
                data = {
                    "error": False,
                    "message": "All fields are required"
                }
                return Response(data, status.HTTP_400_BAD_REQUEST)
            user = User.objects.filter(id=request.data['user'])
            if not user:
                data = {
                    "error": False,
                    "message": "Unavailable user"
                }
                return Response(data)
            user = user[0].id
            plan = PromotionPlan.objects.filter(plan=request.data['plan'])
            if not plan:
                data = {
                    "error": False,
                    "message": "Unavailable plan"
                }
                return Response(data)
            plan = plan[0].id
            couponCode = request.data['couponCode']
            paymentType = request.data['paymentType']
            current_date = datetime.now()
            flag = True

            coupon = CouponCode.objects.raw(
                "SELECT * FROM coupon_code WHERE `code` = {} AND `status` = 1 AND validity_date > '{}'"
                    .format(couponCode, current_date)
            )

            if coupon and coupon[0] and coupon[0].coupon:
                coupon_id = coupon[0].coupon.id
                coupon_model = Coupon.objects.raw(
                    'SELECT * FROM coupon WHERE id = {} AND start_date < "{}" AND end_date >= "{}" AND status = 1'
                        .format(coupon_id, current_date, current_date)
                )

                if coupon_model and coupon_model[0]:
                    promotion_id = coupon_model[0].promotion.id
                    promotion_model = Promotion.objects.raw(
                        'SELECT * FROM promotion WHERE id = {} AND start_date < "{}" AND end_date >= "{}" AND '
                        'status = 1'.format(promotion_id, current_date, current_date)
                    )
                    if promotion_model and promotion_model[0]:
                        promotion_plan_model = PromotionPlan.objects.filter(plan=plan)
                        if promotion_plan_model:
                            data = {
                                "error": False,
                                "isValid": True,
                                "message": "Cupom válido"
                            }

                            coupon_usage_limit = coupon_model[0].usage_limit
                            coupon_count = CouponUsage.objects.filter(coupon=coupon_model[0].coupon).__len__()
                            coupon_usage_model = CouponUsage.objects.filter(user=user, coupon_code=coupon[0].id)

                            if (coupon_usage_limit != 0 and coupon_count > coupon_usage_limit) or coupon_usage_model \
                                    .__len__() > 0:
                                data = {
                                    "error": False,
                                    "isValid": False,
                                    "message": "Limite de uso excedido para este cupom."
                                }
                        else:
                            flag = False
                            data = {
                                "error": True,
                                "isValid": False,
                                "message": "Este cupom não é válido para o plano escolhido."
                            }
                    else:
                        flag = False
                        data = {
                            "error": True,
                            "isValid": False,
                            "message": "Esta promoção já foi finalizada."
                        }
                else:
                    flag = False
                    data = {
                        "error": True,
                        "isValid": False,
                        "message": "Código de cupom expirado."
                    }
            else:
                flag = False
                data = {
                    "error": True,
                    "isValid": False,
                    "message": "Código de cupom inválido e/ou expirado."
                }

            if flag is False:
                return Response(data)

            payment_coupon = CouponCode.objects.filter(code=couponCode)
            if payment_coupon and payment_coupon[0]:
                coupon_serializer = CouponSerializer(Coupon.objects.all(), many=True)
                promotion_serializer = PromotionSerializer(Promotion.objects.all(), many=True)
                if coupon_serializer and coupon_serializer.data:
                    if promotion_serializer and promotion_serializer.data:
                        payment_type = PlanPaymentType.objects.filter(payment_type=paymentType)
                        if payment_type and payment_type[0]:
                            data = {
                                "error": False,
                                "isValid": True,
                                "message": "Pagamento válido para está promoção"
                            }
                            if promotion_serializer.data.__len__() > 0:
                                promotion_value = promotion_serializer.data[0]
                                amount_cents = 0
                                if promotion_value['discount_type'] == '%':
                                    amount_cents = plan[0].price - (
                                            plan[0].price * (promotion_value['discount_amount'] / 100))
                                elif promotion_value['discount_type'] == 'v':
                                    amount_cents = plan[0].price - promotion_value['discount_amount']
                                data = {
                                    "error": False,
                                    "message": "",
                                    "amountInCents": amount_cents,
                                    "name": promotion_value['name'],
                                    "description": promotion_value['description'],
                                    "rule": promotion_value['rule'],
                                    "recurrences": promotion_value['recurrences'],
                                }
                        else:
                            data = {
                                "error": True,
                                "message": "Não é possível utilizar este cupom para este metodo de pagamento"
                            }
                    else:
                        data = {
                            "error": True,
                            "message": "Não existe promoção cadastrada para esse cupom"
                        }
                else:
                    data = {
                        "error": True,
                        "message": "Código de cupom inválido e/ou expirado."
                    }
            else:
                data = {
                    "error": True,
                    "message": "Limite de uso excedido para este cupom."
                }
            return Response(data)

        except Exception as e:
            if hasattr(e, 'message'):
                data = {
                    "error": True,
                    "message": str(e.message)
                }
            else:
                data = {
                    "error": True,
                    "message": str(e)
                }
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def plan_basic2_list(request):
    if request.method == 'GET':
        try:
            snippets = Plan.objects.raw("SELECT * FROM plan WHERE eh_basico = 1")
            serializer = PlanSerializer(snippets, many=True)
            if serializer.data and serializer.data[0]['status']:
                data = {
                    "error": False,
                    "basic_plan2": serializer.data[0]
                }
            else:
                data = {
                    "error": False,
                    "basic_plan2": "Plano Basico 2 inativo"
                }
            return Response(data)
        except Exception as e:
            if hasattr(e, 'message'):
                data = {
                    "error": True,
                    "message": str(e.message)
                }
            else:
                data = {
                    "error": True,
                    "message": str(e)
                }
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def plan_basic_list(request):
    if request.method == 'GET':
        try:
            snippets = Plan.objects.raw("SELECT * FROM plan WHERE eh_basico = 1")
            serializer = PlanSerializer(snippets, many=True)
            if serializer.data and serializer.data[0]['status']:
                data = {
                    "error": False,
                    "is_basic_pan": False
                }
            else:
                data = {
                    "error": False,
                    "is_basic_pan": True
                }
            return Response(data)
        except Exception as e:
            if hasattr(e, 'message'):
                data = {
                    "error": True,
                    "message": str(e.message)
                }
            else:
                data = {
                    "error": True,
                    "message": str(e)
                }
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def setting_list(request):
    if request.method == 'GET':
        try:
            snippets = Setting.objects.all()
            serializer = SettingSerializer(snippets, many=True)
            data = {
                "error": False,
                "setting": serializer.data
            }
            return Response(data)
        except Exception as e:
            if hasattr(e, 'message'):
                data = {
                    "error": True,
                    "message": str(e.message)
                }
            else:
                data = {
                    "error": True,
                    "message": str(e)
                }
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def spot_advertising_list(request, spot):
    if request.method == 'GET':
        try:
            snippets = Advertising.objects.raw(
                """
                SELECT advertising.* FROM advertising_spot
                LEFT JOIN advertising ON advertising.id = advertising_spot.advertising
                INNER JOIN campaign ON campaign.id = advertising.campaign
                WHERE advertising_spot.spot = {} AND advertising.file LIKE '%%mp4%%'
                AND campaign.starts_at <= CURDATE() AND campaign.ends_at >= CURDATE()
                AND campaign.status = 1 AND advertising.advertising_type = 1
                AND advertising.status = 1
                ORDER BY RAND() LIMIT 1
                """.format(spot)
            )

            serializer = SpotAdvertisingSerializer(snippets, many=True)

            project_directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
            field_names = ['id', 'file_video_mp4', 'file_video_mov', 'file_video_webm']
            advertising_id = None
            for record in serializer.data:
                for field_name in field_names:
                    if 'file_video' in field_name:
                        file_path = os.path.join(project_directory, "media")
                        file_path = os.path.join(file_path, "advertising")
                        file_path = os.path.join(file_path, "mp4")
                        file_path = os.path.join(file_path, record[field_name])
                        record[field_name] = file_path
                    else:
                        advertising_id = record[field_name]

            data = {
                "error": False,
                "advertising": serializer.data
            }

            current_date = datetime.now()
            client_ip = helper.get_client_ip(request)

            query = "INSERT INTO access_log (advertising, `date`, ip) VALUES (%s, %s, %s)"

            cursor.execute(
                query, [advertising_id, current_date, client_ip]
            )

            return Response(data)

        except Exception as e:
            if hasattr(e, 'message'):
                data = {
                    "error": True,
                    "message": str(e.message)
                }
            else:
                data = {
                    "error": True,
                    "message": str(e)
                }
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def spot_advertising_user_list(request, spot, user):
    if request.method == 'GET':
        try:
            snippets = Advertising.objects.raw(
                """
                SELECT advertising.* FROM advertising_spot
                LEFT JOIN advertising ON advertising.id = advertising_spot.advertising
                INNER JOIN campaign ON campaign.id = advertising.campaign
                WHERE advertising_spot.spot = {} AND advertising.file LIKE '%%mp4%%'
                AND campaign.starts_at <= CURDATE() AND campaign.ends_at >= CURDATE()
                AND campaign.status = 1 AND advertising.advertising_type = 1
                AND advertising.status = 1
                ORDER BY RAND() LIMIT 1
                """.format(spot)
            )

            serializer = SpotAdvertisingSerializer(snippets, many=True)

            project_directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
            field_names = ['id', 'file_video_mp4', 'file_video_mov', 'file_video_webm']
            advertising_id = None
            for record in serializer.data:
                for field_name in field_names:
                    if 'file_video' in field_name:
                        file_path = os.path.join(project_directory, "media")
                        file_path = os.path.join(file_path, "advertising")
                        file_path = os.path.join(file_path, "mp4")
                        file_path = os.path.join(file_path, record[field_name])
                        record[field_name] = file_path
                    else:
                        advertising_id = record[field_name]

            data = {
                "error": False,
                "advertising": serializer.data
            }

            current_date = datetime.now()
            client_ip = helper.get_client_ip(request)

            query = "INSERT INTO access_log (`user`, advertising, `date`, ip) VALUES (%s, %s, %s, %s)"

            cursor.execute(
                query, [user, advertising_id, current_date, client_ip]
            )

            return Response(data)

        except Exception as e:
            if hasattr(e, 'message'):
                data = {
                    "error": True,
                    "message": str(e.message)
                }
            else:
                data = {
                    "error": True,
                    "message": str(e)
                }
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def spot_tide_list(request, tide):
    if request.method == 'GET':
        try:
            snippets = Tide.objects.raw(
                """
                SELECT * FROM tide 
                LEFT JOIN tide_data ON tide_data.tide = tide.id
                WHERE tide.id = {} AND tide_data.date >= CURDATE() AND 
                DATE(tide_data.date) < DATE_ADD(CURDATE(), INTERVAL 3 DAY)
                ORDER BY tide_data.date ASC
                """.format(tide)
            )

            field_names = ['date', 'height', 'moon', 'tide']

            snippets_data = []
            for p in snippets:
                dict_obj = model_to_dict(p)
                for name in field_names:
                    if name == 'date':
                        field = getattr(p, name).strftime("%d/%m/%Y, %H:%M:%S")
                    else:
                        field = getattr(p, name)
                    dict_obj.update({name: field})
                snippets_data.append(dict_obj)

            data = {
                "error": False,
                "tide": snippets_data
            }

            return Response(data)

        except Exception as e:
            if hasattr(e, 'message'):
                data = {
                    "error": True,
                    "message": str(e.message)
                }
            else:
                data = {
                    "error": True,
                    "message": str(e)
                }
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def spot_condition_list(request, spot):
    if request.method == 'GET':
        try:
            snippets = Condition.objects.raw(
                """
                SELECT * FROM `condition`
                WHERE spot = {} AND condition.date >= CURDATE() AND
                DATE(condition.date) < DATE_ADD(CURDATE(), INTERVAL 3 DAY)
                ORDER BY condition.date ASC
                """.format(spot)
            )

            serializer = SpotConditionSerializer(snippets, many=True)

            data = {
                "error": False,
                "condition": serializer.data
            }

            return Response(data)

        except Exception as e:
            if hasattr(e, 'message'):
                data = {
                    "error": True,
                    "message": str(e.message)
                }
            else:
                data = {
                    "error": True,
                    "message": str(e)
                }
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def user_activation_code(request, code):
    if request.method == 'GET':
        try:
            snippets = User.objects.filter(activation_code=code)
            if snippets:
                snippets.update(activation_code=None)
                data = {
                    "error": False,
                    "message": "Esta conta foi verificada!"
                }
                return Response(data)
            else:
                data = {
                    "error": True,
                    "message": "Não foi possivel verificar sua conta com o código informado!"
                }
                return Response(data)
        except Exception as e:
            if hasattr(e, 'message'):
                data = {
                    "error": True,
                    "message": str(e.message)
                }
            else:
                data = {
                    "error": True,
                    "message": str(e)
                }
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def user_subscription_list(request, user):
    if request.method == 'GET':
        try:
            snippets = OrderPayment.objects.raw(
                """
                SELECT *, subscription.id As subscription_id, subscription.status AS subscription_status, 
                subscription.created_at AS subscription_created_at,
                plan.id AS subscription_plan, plan.price AS subscription_price FROM subscription
                INNER JOIN plan ON plan.id = subscription.plan
                LEFT JOIN order_item ON order_item.id = subscription.order_item
                LEFT JOIN order_payment ON order_payment.order = order_item.order
                WHERE subscription.user = {} AND subscription.expiration_at >=DATE_ADD(CURDATE(), INTERVAL -4 DAY)
                """.format(user)
            )

            field_names = ['subscription_id', 'subscription_status', 'subscription_created_at',
                           'subscription_plan', 'subscription_price']

            snippets_data = []
            for p in snippets:
                dict_obj = model_to_dict(p)
                for name in field_names:
                    dict_obj.update({name: getattr(p, name)})
                snippets_data.append(dict_obj)

            data = {
                "error": False,
                "subscription": snippets_data
            }
            return Response(data)
        except Exception as e:
            if hasattr(e, 'message'):
                data = {
                    "error": True,
                    "message": str(e.message)
                }
            else:
                data = {
                    "error": True,
                    "message": str(e)
                }
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def user_sport_list(request, user):
    if request.method == 'GET':
        try:
            snippets = UserSport.objects.raw(
                """
                SELECT * FROM user_sport
                INNER JOIN sport ON sport.id = user_sport.sport
                WHERE user_sport.user = {}
                ORDER BY sport.order ASC
                """.format(user)
            )

            serializer = UserSportSerializer(snippets, many=True)

            data = {
                "error": False,
                "sport": serializer.data
            }

            return Response(data)

        except Exception as e:
            if hasattr(e, 'message'):
                data = {
                    "error": True,
                    "message": str(e.message)
                }
            else:
                data = {
                    "error": True,
                    "message": str(e)
                }
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def user_sport_list_detail(request, user, sport):
    if request.method == 'GET':
        try:
            snippets = UserSport.objects.raw(
                """
                SELECT * FROM user_sport
                INNER JOIN sport ON sport.id = user_sport.sport
                WHERE user_sport.user = {} AND sport.id = {}
                ORDER BY sport.order ASC
                """.format(user, sport)
            )

            serializer = UserSportSerializer(snippets, many=True)

            data = {
                "error": False,
                "sport": serializer.data
            }

            return Response(data)

        except Exception as e:
            if hasattr(e, 'message'):
                data = {
                    "error": True,
                    "message": str(e.message)
                }
            else:
                data = {
                    "error": True,
                    "message": str(e)
                }
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def user_spot_list(request, user):
    if request.method == 'GET':
        try:
            snippets = UserSpot.objects.raw(
                """
                SELECT spot.*, partner.id AS partner, partner.name AS partner_name,
                partner.note AS partner_note  , partner.description AS partner_description,
                partner.site AS partner_site  , partner.facebook AS partner_facebook,
                partner.phone AS partner_phone, partner.address AS partner_address,
                partner.image AS partner_image, partner.status AS partner_status
                FROM user_spot
                INNER JOIN spot ON spot.id = user_spot.spot
                LEFT JOIN partner ON partner.id = spot.partner
                WHERE user_spot.user = {} ORDER BY spot.order ASC
                """.format(user)
            )

            field_names = ['partner_name', 'partner_note', 'partner_description', 'partner_site', 'partner_facebook',
                           'partner_phone', 'partner_address', 'partner_image', 'partner_status']

            snippets_data = []
            for p in snippets:
                dict_obj = model_to_dict(p)
                for name in field_names:
                    dict_obj.update({name: getattr(p, name)})
                snippets_data.append(dict_obj)

            data = {
                "error": False,
                "spot": snippets_data
            }
            return Response(data)
        except Exception as e:
            if hasattr(e, 'message'):
                data = {
                    "error": True,
                    "message": str(e.message)
                }
            else:
                data = {
                    "error": True,
                    "message": str(e)
                }
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def user_spot_list_detail(request, user, spot):
    if request.method == 'GET':
        try:
            snippets = UserSpot.objects.raw(
                """
                SELECT spot.*, partner.id AS partner, partner.name AS partner_name,
                partner.note AS partner_note  , partner.description AS partner_description,
                partner.site AS partner_site  , partner.facebook AS partner_facebook,
                partner.phone AS partner_phone, partner.address AS partner_address,
                partner.image AS partner_image, partner.status AS partner_status
                FROM user_spot
                INNER JOIN spot ON spot.id = user_spot.spot
                LEFT JOIN partner ON partner.id = spot.partner
                WHERE user_spot.user = {} AND spot.id = {} ORDER BY spot.order ASC
                """.format(user, spot)
            )

            field_names = ['partner_name', 'partner_note', 'partner_description', 'partner_site', 'partner_facebook',
                           'partner_phone', 'partner_address', 'partner_image', 'partner_status']

            snippets_data = []
            for p in snippets:
                dict_obj = model_to_dict(p)
                for name in field_names:
                    dict_obj.update({name: getattr(p, name)})
                snippets_data.append(dict_obj)

            data = {
                "error": False,
                "spot": snippets_data
            }
            return Response(data)
        except Exception as e:
            if hasattr(e, 'message'):
                data = {
                    "error": True,
                    "message": str(e.message)
                }
            else:
                data = {
                    "error": True,
                    "message": str(e)
                }
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def spot_list_detail(request, spot):
    if request.method == 'GET':
        try:
            snippets = Spot.objects.raw(
                """
                SELECT spot.*, route.friendly_url AS slug, partner.id AS partner, partner.name AS partner_name,
                partner.note AS partner_note, partner.description AS partner_description, partner.site AS partner_site,
                partner.facebook AS partner_facebook, partner.phone AS partner_phone, partner.address AS partner_address,
                partner.image AS partner_image, partner.status AS partner_status FROM spot
                LEFT JOIN partner ON partner.id = spot.partner
                INNER JOIN route ON route.spot = spot.id
                WHERE spot.status = 1 AND spot.id = {} ORDER BY spot.order ASC
                """.format(spot)
            )

            field_names = ['slug', 'partner_name', 'partner_note', 'partner_description', 'partner_site',
                           'partner_facebook',
                           'partner_phone', 'partner_address', 'partner_image', 'partner_status']

            snippets_data = []
            for p in snippets:
                dict_obj = model_to_dict(p)
                for name in field_names:
                    dict_obj.update({name: getattr(p, name)})
                snippets_data.append(dict_obj)

            data = {
                "error": False,
                "spot": snippets_data
            }
            return Response(data)
        except Exception as e:
            if hasattr(e, 'message'):
                data = {
                    "error": True,
                    "message": str(e.message)
                }
            else:
                data = {
                    "error": True,
                    "message": str(e)
                }
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'POST'])
def spot_list(request):
    if request.method == 'GET':
        try:
            snippets = Spot.objects.raw(
                """
                SELECT spot.*, route.friendly_url AS slug, partner.id AS partner, partner.name AS partner_name,
                partner.note AS partner_note, partner.description AS partner_description, partner.site AS partner_site,
                partner.facebook AS partner_facebook, partner.phone AS partner_phone, partner.address AS partner_address,
                partner.image AS partner_image, partner.status AS partner_status FROM spot
                LEFT JOIN partner ON partner.id = spot.partner
                INNER JOIN route ON route.spot = spot.id
                WHERE spot.status = 1 ORDER BY spot.order ASC
                """
            )

            field_names = ['slug', 'partner_name', 'partner_note', 'partner_description', 'partner_site',
                           'partner_facebook',
                           'partner_phone', 'partner_address', 'partner_image', 'partner_status']
            snippets_data = []
            for p in snippets:
                dict_obj = model_to_dict(p)
                for name in field_names:
                    dict_obj.update({name: getattr(p, name)})
                snippets_data.append(dict_obj)
            data = {
                "error": False,
                "spot": snippets_data
            }

            return Response(data)
        except Exception as e:
            if hasattr(e, 'message'):
                data = {
                    "error": True,
                    "message": str(e.message)
                }
            else:
                data = {
                    "error": True,
                    "message": str(e)
                }
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        statusCode = status.HTTP_200_OK
        response = {
            "error": False,
            "response": []
        }
        try:
            paginate = 50

            state = request.POST['state']
            city = request.POST['city']
            district = request.POST['district']

            spotList = Spot.objects.raw(
                """
                SELECT DISTINCT spot.*, route.friendly_url AS slug, partner.id AS partner, 
                partner.name AS partner_name, partner.note AS partner_note, partner.description AS partner_description,
                partner.site AS partner_site, partner.facebook AS partner_facebook,
                partner.phone AS partner_phone, partner.address AS partner_address,
                partner.image AS partner_image, partner.status AS partner_status
                FROM spot
                LEFT JOIN partner ON partner.id = spot.partner
                INNER JOIN route ON route.spot = spot.id
                WHERE spot.status = 1
                ORDER BY spot.order ASC
                """
            )

            if district is not None:
                spotList = Spot.objects.raw(
                    """
                    SELECT DISTINCT spot.*, route.friendly_url AS slug, partner.id AS partner, 
                    partner.name AS partner_name, partner.note AS partner_note, partner.description AS partner_description,
                    partner.site AS partner_site, partner.facebook AS partner_facebook,
                    partner.phone AS partner_phone, partner.address AS partner_address,
                    partner.image AS partner_image, partner.status AS partner_status
                    FROM spot
                    LEFT JOIN partner ON partner.id = spot.partner
                    INNER JOIN route ON route.spot = spot.id
                    INNER JOIN address ON address.id = spot.address
                    INNER JOIN address_district ON address_district.id = address.address_district
                    WHERE spot.status = 1 AND address_district.id = {}
                    ORDER BY spot.order ASC
                    """.format(district)
                )
            else:
                if city is not None:
                    spotList = Spot.objects.raw(
                        """
                        SELECT DISTINCT spot.*, route.friendly_url AS slug, partner.id AS partner, 
                        partner.name AS partner_name, partner.note AS partner_note, partner.description AS partner_description,
                        partner.site AS partner_site, partner.facebook AS partner_facebook,
                        partner.phone AS partner_phone, partner.address AS partner_address,
                        partner.image AS partner_image, partner.status AS partner_status
                        FROM spot
                        LEFT JOIN partner ON partner.id = spot.partner
                        INNER JOIN route ON route.spot = spot.id
                        INNER JOIN address ON address.id = spot.address
                        INNER JOIN address_district ON address_district.id = address.address_district
                        WHERE spot.status = 1 AND address_district.address_city = {}
                        ORDER BY spot.order ASC
                        """.format(city)
                    )
                else:
                    if state is not None:
                        spotList = Spot.objects.raw(
                            """
                            SELECT DISTINCT spot.*, route.friendly_url AS slug, partner.id AS partner, 
                            partner.name AS partner_name, partner.note AS partner_note, partner.description AS partner_description,
                            partner.site AS partner_site, partner.facebook AS partner_facebook,
                            partner.phone AS partner_phone, partner.address AS partner_address,
                            partner.image AS partner_image, partner.status AS partner_status
                            FROM spot
                            LEFT JOIN partner ON partner.id = spot.partner
                            INNER JOIN route ON route.spot = spot.id
                            INNER JOIN address ON address.id = spot.address
                            INNER JOIN address_district ON address_district.id = address.address_district
                            WHERE spot.status = 1 AND address_district.address_state = {}
                            ORDER BY spot.order ASC
                            """.format(state)
                        )

            field_names = ['slug', 'partner_name', 'partner_note', 'partner_description', 'partner_site',
                           'partner_facebook',
                           'partner_phone', 'partner_address', 'partner_image', 'partner_status']

            newSpotList = []
            for p in spotList:
                dict_obj = model_to_dict(p)
                for name in field_names:
                    dict_obj.update({name: getattr(p, name)})
                newSpotList.append(dict_obj)

            snippets_data = []
            for spot in newSpotList:
                if 'stream' in spot:
                    spot['stream'] = spot['stream']
                else:
                    spot['stream'] = spot['m3u8']

                if request.META['HTTP_USER_AGENT'] == "ios":
                    if 'http' not in spot.stream:
                        spot['stream'] = 'http://' + spot['stream']
                    if 'http' not in spot.m3u8:
                        spot['m3u8'] = 'http://' + spot['m3u8']

                snippets_data = spot

            response.update({
                "response": snippets_data
            })

        except Exception as e:
            statusCode = status.HTTP_400_BAD_REQUEST
            response = {
                "error": True,
                "message": str(e)
            }

        finally:
            return Response(response, statusCode)


@api_view(['GET'])
def sport_list(request):
    if request.method == 'GET':
        try:
            snippets = Sport.objects.raw(
                'SELECT * FROM sport WHERE STATUS = 1 ORDER BY "order" ASC'
            )
            serializer = SportSerializer(snippets, many=True)
            data = {
                "error": False,
                "sport": serializer.data
            }
            return Response(data)
        except Exception as e:
            if hasattr(e, 'message'):
                data = {
                    "error": True,
                    "message": str(e.message)
                }
            else:
                data = {
                    "error": True,
                    "message": str(e)
                }
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def plan_list(request):
    if request.method == 'GET':
        try:
            snippets = Plan.objects.raw(
                'SELECT * FROM plan WHERE STATUS = 1 AND NAME != "Plano Basico 2"'
            )
            serializer = PlanSerializer(snippets, many=True)
            data = {
                "error": False,
                "plan": serializer.data
            }
            return Response(data)
        except Exception as e:
            if hasattr(e, 'message'):
                data = {
                    "error": True,
                    "message": str(e.message)
                }
            else:
                data = {
                    "error": True,
                    "message": str(e)
                }
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def plain_list(request):
    if request.method == 'GET':
        try:
            snippets = Plan.objects.raw(
                "SELECT * FROM plan WHERE status = 1"
            )
            serializer = PlanSerializer(snippets, many=True)
            data = {
                "error": False,
                "plain": serializer.data
            }
            return Response(data)
        except Exception as e:
            if hasattr(e, 'message'):
                data = {
                    "error": True,
                    "message": str(e.message)
                }
            else:
                data = {
                    "error": True,
                    "message": str(e)
                }
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def feed_spot_list(request):
    if request.method == 'GET':
        try:
            snippets = Feed.objects.raw(
                "SELECT * FROM feed WHERE (DATE >= CURDATE() AND STATUS = 1) OR spot IS NULL"
            )
            serializer = FeedSerializer(snippets, many=True)
            data = {
                "error": False,
                "feed": serializer.data
            }
            return Response(data)
        except Exception as e:
            if hasattr(e, 'message'):
                data = {
                    "error": True,
                    "message": str(e.message)
                }
            else:
                data = {
                    "error": True,
                    "message": str(e)
                }
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def feed_spot_list_detail(request, spot):
    if request.method == 'GET':
        try:
            snippets = Feed.objects.raw(
                "SELECT * FROM feed WHERE (spot = {} AND DATE >= CURDATE() AND STATUS = 1) OR spot IS NULL".format(spot)
            )
            serializer = FeedSerializer(snippets, many=True)
            data = {
                "error": False,
                "feed": serializer.data
            }
            return Response(data)
        except Exception as e:
            if hasattr(e, 'message'):
                data = {
                    "error": True,
                    "message": str(e.message)
                }
            else:
                data = {
                    "error": True,
                    "message": str(e)
                }
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def address_district_list(request, city):
    if request.method == 'GET':
        try:
            snippets = AddressDistrict.objects.raw(
                """
                SELECT address_district.*
                FROM address_district
                INNER JOIN address ON address.address_district = address_district.id
                INNER JOIN spot ON spot.address = address.id
                WHERE spot.status = 1 AND address_city = {}
                """.format(city)
            )
            serializer = AddressDistrictSerializer(snippets, many=True)
            data = {
                "error": False,
                "response": serializer.data
            }
            return Response(data)
        except Exception as e:
            if hasattr(e, 'message'):
                data = {
                    "error": True,
                    "message": str(e.message)
                }
            else:
                data = {
                    "error": True,
                    "message": str(e)
                }
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def address_city_list(request, state):
    if request.method == 'GET':
        try:
            snippets = AddressCity.objects.raw(
                """
                SELECT address_city.*
                FROM address_city
                INNER JOIN address_district ON address_district.address_city = address_city.id
                INNER JOIN address ON address.address_district = address_district.id
                INNER JOIN spot ON spot.address = address.id
                WHERE spot.status = 1 AND address_state = {}
                """.format(state)
            )
            serializer = AddressCitySerializer(snippets, many=True)
            data = {
                "error": False,
                "response": serializer.data
            }
            return Response(data)
        except Exception as e:
            if hasattr(e, 'message'):
                data = {
                    "error": True,
                    "message": str(e.message)
                }
            else:
                data = {
                    "error": True,
                    "message": str(e)
                }
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def address_state_list(request):
    if request.method == 'GET':
        try:
            snippets = AddressState.objects.raw(
                """
                SELECT address_state.*
                FROM address_state
                INNER JOIN address_city ON address_city.address_state = address_state.id
                INNER JOIN address_district ON address_district.address_city = address_city.id
                INNER JOIN address ON address.address_district = address_district.id
                INNER JOIN spot ON spot.address = address.id
                WHERE spot.status = 1
                """
            )
            serializer = AddressStateSerializer(snippets, many=True)
            data = {
                "error": False,
                "response": serializer.data
            }
            return Response(data)
        except Exception as e:
            if hasattr(e, 'message'):
                data = {
                    "error": True,
                    "message": str(e.message)
                }
            else:
                data = {
                    "error": True,
                    "message": str(e)
                }
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)
