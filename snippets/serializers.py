from rest_framework import serializers
from snippets.models import Address
from snippets.models import AddressCountry
from snippets.models import AddressState
from snippets.models import AddressCity
from snippets.models import AddressDistrict
from snippets.models import Feed
from snippets.models import Plan
from snippets.models import Sport
from snippets.models import Partner
from snippets.models import Route
from snippets.models import Spot
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
from snippets.models import CouponCode


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class AddressCountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AddressCountry
        fields = "__all__"


class AddressStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressState
        fields = "__all__"


class AddressCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressCity
        fields = "__all__"


class AddressDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressDistrict
        fields = "__all__"


class FeedSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%d/%m/%Y, %H:%M:%S")

    class Meta:
        model = Feed
        fields = "__all__"


class PlainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = "__all__"


class PartnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"


class RouteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Route
        fields = "__all__"


class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = "__all__"


class SpotConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = "__all__"


class SpotTideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tide
        fields = "__all__"


class AdvertisingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisingSpot
        fields = "__all__"


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = "__all__"


class IsBasicPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"


class CouponCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouponCode
        fields = "__all__"





class UserSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSpot
        fields = "__all__"


class UserSportSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSport
        fields = "__all__"


class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"


class UserActivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserLogoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"


class UserDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"


class UserLoginWithFacebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserSpotBasicPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSpotBasicPlan
        fields = "__all__"


class UserDeviceV2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"

