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

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.forms.models import model_to_dict
import os


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
            field_names = ['file_video_mp4', 'file_video_mov', 'file_video_webm']
            for record in serializer.data:
                for field_name in field_names:
                    file_path = os.path.join(project_directory, "media")
                    file_path = os.path.join(file_path, "advertising")
                    file_path = os.path.join(file_path, "mp4")
                    file_path = os.path.join(file_path, record[field_name])
                    record[field_name] = file_path

            data = {
                "error": False,
                "advertising": serializer.data
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


@api_view(['GET'])
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
