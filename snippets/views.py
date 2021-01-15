from snippets.models import Address
from snippets.models import AddressCountry
from snippets.models import AddressState
from snippets.models import AddressCity
from snippets.models import AddressDistrict
from snippets.models import Spot
from snippets.models import Feed
from snippets.models import Plan
from snippets.models import Sport
from snippets.models import Partner
from snippets.models import Route
from snippets.models import Condition
from snippets.models import Tide
from snippets.models import UserSpot
from snippets.models import UserSport
from snippets.models import Subscription
from snippets.models import User
from snippets.models import Device
from snippets.models import UserSpotBasicPlan
from snippets.models import AdvertisingSpot
from snippets.models import Setting

from snippets.serializers import AddressStateSerializer
from snippets.serializers import AddressCitySerializer
from snippets.serializers import AddressDistrictSerializer
from snippets.serializers import FeedSerializer
from snippets.serializers import PlanSerializer
from snippets.serializers import SportSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


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
def plan_list(request):
    if request.method == 'GET':
        try:
            snippets = Plan.objects.raw(
                'SELECT * FROM plan WHERE STATUS = 1 AND NAME != "Plano Basico 2"'
            )
            serializer = PlanSerializer(snippets, many=True)
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
def plain_list(request):
    if request.method == 'GET':
        try:
            snippets = Plan.objects.raw(
                "SELECT * FROM plan WHERE status = 1"
            )
            serializer = PlanSerializer(snippets, many=True)
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
def feed_spot_list(request, spot):
    if request.method == 'GET':
        try:
            snippets = Feed.objects.raw(
                "SELECT * FROM feed WHERE (spot = {} AND DATE >= CURDATE() AND STATUS = 1) OR spot IS NULL".format(spot)
            )
            serializer = FeedSerializer(snippets, many=True)
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


# class SpotViewSet(viewsets.ModelViewSet):
#     queryset = Spot.objects.all()
#     serializer_class = SpotSerializer
#     permissions = [permissions.IsAuthenticatedOrReadOnly]
#
#     def get_queryset(self):
#         return Spot.objects.raw(
#             """
#             SELECT spot.*, route.friendly_url AS slug, partner.id AS partner, partner.name AS partner_name,
#             partner.note AS partner_note, partner.description AS partner_description, partner.site AS partner_site,
#             partner.facebook AS partner_facebook, partner.phone AS partner_phone, partner.address AS partner_address,
#             partner.image AS partner_image, partner.status AS partner_status FROM spot
#             LEFT JOIN partner ON partner.id = spot.partner
#             INNER JOIN route ON route.spot = spot.id
#             WHERE spot.status = 1 ORDER BY spot.order ASC
#             """
#         )
#
#
# class SpotConditionViewSet(viewsets.ModelViewSet):
#     queryset = Condition.objects.all()
#     serializer_class = SpotConditionSerializer
#     permissions = [permissions.IsAuthenticatedOrReadOnly]
#
#     def get_queryset(self):
#         return Condition.objects.raw(
#             """
#             SELECT * FROM `condition` WHERE spot = 1 AND "date" >= CURDATE() AND
#             DATE("date") < DATE_ADD(CURDATE(), INTERVAL 3 DAY) ORDER BY "date" ASC
#             """
#         )
#
#
# class SpotTideViewSet(viewsets.ModelViewSet):
#     queryset = Tide.objects.all()
#     serializer_class = SpotTideSerializer
#
#
# class AdvertisingSpotViewSet(viewsets.ModelViewSet):
#     queryset = AdvertisingSpot.objects.all()
#     serializer_class = AdvertisingSpotSerializer
#
#
# class SettingViewSet(viewsets.ModelViewSet):
#     queryset = Setting.objects.all()
#     serializer_class = SettingSerializer
#
#
# class CouponCodeViewSet(viewsets.ModelViewSet):
#     queryset = Setting.objects.all()
#     serializer_class = SettingSerializer
#
#
#
# class UserSpotViewSet(viewsets.ModelViewSet):
#     queryset = UserSpot.objects.all()
#     serializer_class = UserSpotSerializer
#
#
# class UserSportViewSet(viewsets.ModelViewSet):
#     queryset = UserSport.objects.all()
#     serializer_class = UserSportSerializer
#
#
# class UserSubscriptionViewSet(viewsets.ModelViewSet):
#     queryset = Subscription.objects.all()
#     serializer_class = UserSubscriptionSerializer
#
#
# class UserActivationViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserActivationSerializer
#
#
# class UserLogoutViewSet(viewsets.ModelViewSet):
#     queryset = Device.objects.all()
#     serializer_class = UserLogoutSerializer
#
#
# class UserDeviceViewSet(viewsets.ModelViewSet):
#     queryset = Device.objects.all()
#     serializer_class = UserDeviceSerializer
#
#
# class UserLoginWithFacebookViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserLoginWithFacebookSerializer
#
#
# class UserChangePasswordViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserChangePasswordSerializer
#
#
# class UserSpotBasicPlanViewSet(viewsets.ModelViewSet):
#     queryset = UserSpotBasicPlan.objects.all()
#     serializer_class = UserSpotBasicPlanSerializer
#
#
# class UserDeviceV2ViewSet(viewsets.ModelViewSet):
#     queryset = Device.objects.all()
#     serializer_class = UserDeviceV2Serializer
#
#
# from rest_framework import status
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from snippets.models import UserSpot
# from snippets.serializers import UserSpotSerializer
#
#
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def spot_list(request, test):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = UserSpot.objects.all()
#         serializer = UserSpotSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = UserSpotSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def spot_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = UserSpot.objects.get(pk=pk)
#     except UserSpot.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = UserSpotSerializer(snippet)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = UserSpotSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
