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

from rest_framework import serializers


class AccessLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccessLog
        fields = "__all__"


class AccessLogArchiveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccessLogArchive
        fields = "__all__"


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class AddressCitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AddressCity
        fields = "__all__"


class AddressCountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AddressCountry
        fields = "__all__"


class AddressDistrictSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AddressDistrict
        fields = "__all__"


class AddressStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AddressState
        fields = "__all__"


class AdvertisingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advertising
        fields = "__all__"


class AdvertisingPageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdvertisingPage
        fields = "__all__"


class AdvertisingSpotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdvertisingSpot
        fields = "__all__"


class AdvertisingTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdvertisingType
        fields = "__all__"


class AdvertisingZoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdvertisingZone
        fields = "__all__"


class ApiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Api
        fields = "__all__"


class AuthGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AuthGroup
        fields = "__all__"


class AuthGroupPermissionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AuthGroupPermissions
        fields = "__all__"


class AuthPermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AuthPermission
        fields = "__all__"


class AuthUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AuthUser
        fields = "__all__"


class AuthUserGroupsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AuthUserGroups
        fields = "__all__"


class AuthUserUserPermissionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AuthUserUserPermissions
        fields = "__all__"


class CampaignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Campaign
        fields = "__all__"


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ConditionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Condition
        fields = "__all__"


class CouponSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coupon
        fields = "__all__"


class CouponCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CouponCode
        fields = "__all__"


class CouponUsageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CouponUsage
        fields = "__all__"


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"


class DjangoAdminLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DjangoAdminLog
        fields = "__all__"


class DjangoContentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DjangoContentType
        fields = "__all__"


class DjangoMigrationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DjangoMigrations
        fields = "__all__"


class DjangoSessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DjangoSession
        fields = "__all__"


class EmailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Email
        fields = "__all__"


class EmailContextSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmailContext
        fields = "__all__"


class EmailQueueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmailQueue
        fields = "__all__"


class FeedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feed
        fields = "__all__"


class FeedMediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FeedMedia
        fields = "__all__"


class FeedMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FeedMessage
        fields = "__all__"


class FeedMessageOptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FeedMessageOption
        fields = "__all__"


class MediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Media
        fields = "__all__"


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class NewsMediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewsMedia
        fields = "__all__"


class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


class NotificationFilterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NotificationFilter
        fields = "__all__"


class NotificationStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NotificationStatus
        fields = "__all__"


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderData
        fields = "__all__"


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderLog
        fields = "__all__"


class OrderPaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderPayment
        fields = "__all__"


class OrderPaymentCallbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderPaymentCallback
        fields = "__all__"


class OrderPaymentRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderPaymentRequest
        fields = "__all__"


class OrderStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderStatus
        fields = "__all__"


class PartnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"


class PartnerCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PartnerCategory
        fields = "__all__"


class PaymentAcquirerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaymentAcquirer
        fields = "__all__"


class PaymentGatewaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaymentGateway
        fields = "__all__"


class PaymentMethodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = "__all__"


class PaymentStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaymentStatus
        fields = "__all__"


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaymentType
        fields = "__all__"


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"


class PlanPaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlanPaymentType
        fields = "__all__"


class PlanResourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlanResource
        fields = "__all__"


class PlanSpotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlanSpot
        fields = "__all__"


class PromotionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Promotion
        fields = "__all__"


class PromotionPaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PromotionPaymentType
        fields = "__all__"


class PromotionPlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PromotionPlan
        fields = "__all__"


class PushQueueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PushQueue
        fields = "__all__"


class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resource
        fields = "__all__"


class RouteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Route
        fields = "__all__"


class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"


class SettingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Setting
        fields = "__all__"


class SmsQueueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SmsQueue
        fields = "__all__"


class SportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sport
        fields = "__all__"


class SpotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Spot
        fields = "__all__"


class SubscriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"


class SubscriptionLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubscriptionLog
        fields = "__all__"


class TideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tide
        fields = "__all__"


class TideDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TideData
        fields = "__all__"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserGroup
        fields = "__all__"


class UserGroupMenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserGroupMenu
        fields = "__all__"


class UserGroupPermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserGroupPermission
        fields = "__all__"


class UserPaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserPayment
        fields = "__all__"


class UserSportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserSport
        fields = "__all__"


class UserSpotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserSpot
        fields = "__all__"


class UserSpotBasicPlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserSpotBasicPlan
        fields = "__all__"


class UserUserGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserUserGroup
        fields = "__all__"
