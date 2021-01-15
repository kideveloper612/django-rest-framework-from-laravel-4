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


class AccessLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessLog
        fields = "__all__"


class AccessLogArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessLogArchive
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class AddressCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressCity
        fields = "__all__"


class AddressCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressCountry
        fields = "__all__"


class AddressDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressDistrict
        fields = "__all__"


class AddressStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressState
        fields = "__all__"


class AdvertisingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertising
        fields = "__all__"


class AdvertisingPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisingPage
        fields = "__all__"


class AdvertisingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisingSpot
        fields = "__all__"


class AdvertisingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisingType
        fields = "__all__"


class AdvertisingZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisingZone
        fields = "__all__"


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = "__all__"


class AuthGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthGroup
        fields = "__all__"


class AuthGroupPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthGroupPermissions
        fields = "__all__"


class AuthPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthPermission
        fields = "__all__"


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = "__all__"


class AuthUserGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUserGroups
        fields = "__all__"


class AuthUserUserPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUserUserPermissions
        fields = "__all__"


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = "__all__"


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = "__all__"


class CouponCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouponCode
        fields = "__all__"


class CouponUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouponUsage
        fields = "__all__"


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"


class DjangoAdminLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoAdminLog
        fields = "__all__"


class DjangoContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoContentType
        fields = "__all__"


class DjangoMigrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoMigrations
        fields = "__all__"


class DjangoSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoSession
        fields = "__all__"


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = "__all__"


class EmailContextSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailContext
        fields = "__all__"


class EmailQueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailQueue
        fields = "__all__"


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = "__all__"


class FeedMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedMedia
        fields = "__all__"


class FeedMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedMessage
        fields = "__all__"


class FeedMessageOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedMessageOption
        fields = "__all__"


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class NewsMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsMedia
        fields = "__all__"


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


class NotificationFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationFilter
        fields = "__all__"


class NotificationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationStatus
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderData
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderLog
        fields = "__all__"


class OrderPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPayment
        fields = "__all__"


class OrderPaymentCallbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPaymentCallback
        fields = "__all__"


class OrderPaymentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPaymentRequest
        fields = "__all__"


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = "__all__"


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"


class PartnerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerCategory
        fields = "__all__"


class PaymentAcquirerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentAcquirer
        fields = "__all__"


class PaymentGatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentGateway
        fields = "__all__"


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = "__all__"


class PaymentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentStatus
        fields = "__all__"


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = "__all__"


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"


class PlanPaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanPaymentType
        fields = "__all__"


class PlanResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanResource
        fields = "__all__"


class PlanSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanSpot
        fields = "__all__"


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = "__all__"


class PromotionPaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionPaymentType
        fields = "__all__"


class PromotionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionPlan
        fields = "__all__"


class PushQueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = PushQueue
        fields = "__all__"


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = "__all__"


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = "__all__"


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = "__all__"


class SmsQueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmsQueue
        fields = "__all__"


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = "__all__"


class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"


class SubscriptionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionLog
        fields = "__all__"


class TideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tide
        fields = "__all__"


class TideDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TideData
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = "__all__"


class UserGroupMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroupMenu
        fields = "__all__"


class UserGroupPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroupPermission
        fields = "__all__"


class UserPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPayment
        fields = "__all__"


class UserSportSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSport
        fields = "__all__"


class UserSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSpot
        fields = "__all__"


class UserSpotBasicPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSpotBasicPlan
        fields = "__all__"


class UserUserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserUserGroup
        fields = "__all__"
