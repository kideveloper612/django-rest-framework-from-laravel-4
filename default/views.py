from rest_framework import viewsets

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

from default.serializers import AccessLogSerializer
from default.serializers import AccessLogArchiveSerializer
from default.serializers import AddressSerializer
from default.serializers import AddressCitySerializer
from default.serializers import AddressCountrySerializer
from default.serializers import AddressDistrictSerializer
from default.serializers import AddressStateSerializer
from default.serializers import AdvertisingSerializer
from default.serializers import AdvertisingPageSerializer
from default.serializers import AdvertisingSpotSerializer
from default.serializers import AdvertisingTypeSerializer
from default.serializers import AdvertisingZoneSerializer
from default.serializers import ApiSerializer
from default.serializers import AuthGroupSerializer
from default.serializers import AuthGroupPermissionsSerializer
from default.serializers import AuthPermissionSerializer
from default.serializers import AuthUserSerializer
from default.serializers import AuthUserGroupsSerializer
from default.serializers import AuthUserUserPermissionsSerializer
from default.serializers import CampaignSerializer
from default.serializers import CategorySerializer
from default.serializers import ConditionSerializer
from default.serializers import CouponSerializer
from default.serializers import CouponCodeSerializer
from default.serializers import CouponUsageSerializer
from default.serializers import DeviceSerializer
from default.serializers import DjangoAdminLogSerializer
from default.serializers import DjangoContentTypeSerializer
from default.serializers import DjangoMigrationsSerializer
from default.serializers import DjangoSessionSerializer
from default.serializers import EmailSerializer
from default.serializers import EmailContextSerializer
from default.serializers import EmailQueueSerializer
from default.serializers import FeedSerializer
from default.serializers import FeedMediaSerializer
from default.serializers import FeedMessageSerializer
from default.serializers import FeedMessageOptionSerializer
from default.serializers import MediaSerializer
from default.serializers import MenuSerializer
from default.serializers import NewsSerializer
from default.serializers import NewsMediaSerializer
from default.serializers import NotificationSerializer
from default.serializers import NotificationFilterSerializer
from default.serializers import NotificationStatusSerializer
from default.serializers import OrderSerializer
from default.serializers import OrderDataSerializer
from default.serializers import OrderItemSerializer
from default.serializers import OrderLogSerializer
from default.serializers import OrderPaymentSerializer
from default.serializers import OrderPaymentCallbackSerializer
from default.serializers import OrderPaymentRequestSerializer
from default.serializers import OrderStatusSerializer
from default.serializers import PartnerSerializer
from default.serializers import PartnerCategorySerializer
from default.serializers import PaymentAcquirerSerializer
from default.serializers import PaymentGatewaySerializer
from default.serializers import PaymentMethodSerializer
from default.serializers import PaymentStatusSerializer
from default.serializers import PaymentTypeSerializer
from default.serializers import PermissionSerializer
from default.serializers import PlanSerializer
from default.serializers import PlanPaymentTypeSerializer
from default.serializers import PlanResourceSerializer
from default.serializers import PlanSpotSerializer
from default.serializers import PromotionSerializer
from default.serializers import PromotionPaymentTypeSerializer
from default.serializers import PromotionPlanSerializer
from default.serializers import PushQueueSerializer
from default.serializers import ResourceSerializer
from default.serializers import RouteSerializer
from default.serializers import SessionSerializer
from default.serializers import SettingSerializer
from default.serializers import SmsQueueSerializer
from default.serializers import SportSerializer
from default.serializers import SpotSerializer
from default.serializers import SubscriptionSerializer
from default.serializers import SubscriptionLogSerializer
from default.serializers import TideSerializer
from default.serializers import TideDataSerializer
from default.serializers import UserSerializer
from default.serializers import UserGroupSerializer
from default.serializers import UserGroupMenuSerializer
from default.serializers import UserGroupPermissionSerializer
from default.serializers import UserPaymentSerializer
from default.serializers import UserSportSerializer
from default.serializers import UserSpotSerializer
from default.serializers import UserSpotBasicPlanSerializer
from default.serializers import UserUserGroupSerializer


class AccessLogViewSet(viewsets.ModelViewSet):
    queryset = AccessLog.objects.all()
    serializer_class = AccessLogSerializer


class AccessLogArchiveViewSet(viewsets.ModelViewSet):
    queryset = AccessLogArchive.objects.all()
    serializer_class = AccessLogArchiveSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressCityViewSet(viewsets.ModelViewSet):
    queryset = AddressCity.objects.all()
    serializer_class = AddressCitySerializer


class AddressCountryViewSet(viewsets.ModelViewSet):
    queryset = AddressCountry.objects.all()
    serializer_class = AddressCountrySerializer


class AddressDistrictViewSet(viewsets.ModelViewSet):
    queryset = AddressDistrict.objects.all()
    serializer_class = AddressDistrictSerializer


class AddressStateViewSet(viewsets.ModelViewSet):
    queryset = AddressState.objects.all()
    serializer_class = AddressStateSerializer


class AdvertisingViewSet(viewsets.ModelViewSet):
    queryset = Advertising.objects.all()
    serializer_class = AdvertisingSerializer


class AdvertisingPageViewSet(viewsets.ModelViewSet):
    queryset = AdvertisingPage.objects.all()
    serializer_class = AdvertisingPageSerializer


class AdvertisingSpotViewSet(viewsets.ModelViewSet):
    queryset = AdvertisingSpot.objects.all()
    serializer_class = AdvertisingSpotSerializer


class AdvertisingTypeViewSet(viewsets.ModelViewSet):
    queryset = AdvertisingType.objects.all()
    serializer_class = AdvertisingTypeSerializer


class AdvertisingZoneViewSet(viewsets.ModelViewSet):
    queryset = AdvertisingZone.objects.all()
    serializer_class = AdvertisingZoneSerializer


class ApiViewSet(viewsets.ModelViewSet):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer


class AuthGroupViewSet(viewsets.ModelViewSet):
    queryset = AuthGroup.objects.all()
    serializer_class = AuthGroupSerializer


class AuthGroupPermissionsViewSet(viewsets.ModelViewSet):
    queryset = AuthGroupPermissions.objects.all()
    serializer_class = AuthGroupPermissionsSerializer


class AuthPermissionViewSet(viewsets.ModelViewSet):
    queryset = AuthPermission.objects.all()
    serializer_class = AuthPermissionSerializer


class AuthUserViewSet(viewsets.ModelViewSet):
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer


class AuthUserGroupsViewSet(viewsets.ModelViewSet):
    queryset = AuthUserGroups.objects.all()
    serializer_class = AuthUserGroupsSerializer


class AuthUserUserPermissionsViewSet(viewsets.ModelViewSet):
    queryset = AuthUserUserPermissions.objects.all()
    serializer_class = AuthUserUserPermissionsSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer


class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class CouponCodeViewSet(viewsets.ModelViewSet):
    queryset = CouponCode.objects.all()
    serializer_class = CouponCodeSerializer


class CouponUsageViewSet(viewsets.ModelViewSet):
    queryset = CouponUsage.objects.all()
    serializer_class = CouponUsageSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DjangoAdminLogViewSet(viewsets.ModelViewSet):
    queryset = DjangoAdminLog.objects.all()
    serializer_class = DjangoAdminLogSerializer


class DjangoContentTypeViewSet(viewsets.ModelViewSet):
    queryset = DjangoContentType.objects.all()
    serializer_class = DjangoContentTypeSerializer


class DjangoMigrationsViewSet(viewsets.ModelViewSet):
    queryset = DjangoMigrations.objects.all()
    serializer_class = DjangoMigrationsSerializer


class DjangoSessionViewSet(viewsets.ModelViewSet):
    queryset = DjangoSession.objects.all()
    serializer_class = DjangoSessionSerializer


class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer


class EmailContextViewSet(viewsets.ModelViewSet):
    queryset = EmailContext.objects.all()
    serializer_class = EmailContextSerializer


class EmailQueueViewSet(viewsets.ModelViewSet):
    queryset = EmailQueue.objects.all()
    serializer_class = EmailQueueSerializer


class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer


class FeedMediaViewSet(viewsets.ModelViewSet):
    queryset = FeedMedia.objects.all()
    serializer_class = FeedMediaSerializer


class FeedMessageViewSet(viewsets.ModelViewSet):
    queryset = FeedMessage.objects.all()
    serializer_class = FeedMessageSerializer


class FeedMessageOptionViewSet(viewsets.ModelViewSet):
    queryset = FeedMessageOption.objects.all()
    serializer_class = FeedMessageOptionSerializer


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsMediaViewSet(viewsets.ModelViewSet):
    queryset = NewsMedia.objects.all()
    serializer_class = NewsMediaSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationFilterViewSet(viewsets.ModelViewSet):
    queryset = NotificationFilter.objects.all()
    serializer_class = NotificationFilterSerializer


class NotificationStatusViewSet(viewsets.ModelViewSet):
    queryset = NotificationStatus.objects.all()
    serializer_class = NotificationStatusSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDataViewSet(viewsets.ModelViewSet):
    queryset = OrderData.objects.all()
    serializer_class = OrderDataSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderLogViewSet(viewsets.ModelViewSet):
    queryset = OrderLog.objects.all()
    serializer_class = OrderLogSerializer


class OrderPaymentViewSet(viewsets.ModelViewSet):
    queryset = OrderPayment.objects.all()
    serializer_class = OrderPaymentSerializer


class OrderPaymentCallbackViewSet(viewsets.ModelViewSet):
    queryset = OrderPaymentCallback.objects.all()
    serializer_class = OrderPaymentCallbackSerializer


class OrderPaymentRequestViewSet(viewsets.ModelViewSet):
    queryset = OrderPaymentRequest.objects.all()
    serializer_class = OrderPaymentRequestSerializer


class OrderStatusViewSet(viewsets.ModelViewSet):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class PartnerCategoryViewSet(viewsets.ModelViewSet):
    queryset = PartnerCategory.objects.all()
    serializer_class = PartnerCategorySerializer


class PaymentAcquirerViewSet(viewsets.ModelViewSet):
    queryset = PaymentAcquirer.objects.all()
    serializer_class = PaymentAcquirerSerializer


class PaymentGatewayViewSet(viewsets.ModelViewSet):
    queryset = PaymentGateway.objects.all()
    serializer_class = PaymentGatewaySerializer


class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer


class PaymentStatusViewSet(viewsets.ModelViewSet):
    queryset = PaymentStatus.objects.all()
    serializer_class = PaymentStatusSerializer


class PaymentTypeViewSet(viewsets.ModelViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class PlanPaymentTypeViewSet(viewsets.ModelViewSet):
    queryset = PlanPaymentType.objects.all()
    serializer_class = PlanPaymentTypeSerializer


class PlanResourceViewSet(viewsets.ModelViewSet):
    queryset = PlanResource.objects.all()
    serializer_class = PlanResourceSerializer


class PlanSpotViewSet(viewsets.ModelViewSet):
    queryset = PlanSpot.objects.all()
    serializer_class = PlanSpotSerializer


class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer


class PromotionPaymentTypeViewSet(viewsets.ModelViewSet):
    queryset = PromotionPaymentType.objects.all()
    serializer_class = PromotionPaymentTypeSerializer


class PromotionPlanViewSet(viewsets.ModelViewSet):
    queryset = PromotionPlan.objects.all()
    serializer_class = PromotionPlanSerializer


class PushQueueViewSet(viewsets.ModelViewSet):
    queryset = PushQueue.objects.all()
    serializer_class = PushQueueSerializer


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class SettingViewSet(viewsets.ModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer


class SmsQueueViewSet(viewsets.ModelViewSet):
    queryset = SmsQueue.objects.all()
    serializer_class = SmsQueueSerializer


class SportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer


class SpotViewSet(viewsets.ModelViewSet):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class SubscriptionLogViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionLog.objects.all()
    serializer_class = SubscriptionLogSerializer


class TideViewSet(viewsets.ModelViewSet):
    queryset = Tide.objects.all()
    serializer_class = TideSerializer


class TideDataViewSet(viewsets.ModelViewSet):
    queryset = TideData.objects.all()
    serializer_class = TideDataSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserGroupViewSet(viewsets.ModelViewSet):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer


class UserGroupMenuViewSet(viewsets.ModelViewSet):
    queryset = UserGroupMenu.objects.all()
    serializer_class = UserGroupMenuSerializer


class UserGroupPermissionViewSet(viewsets.ModelViewSet):
    queryset = UserGroupPermission.objects.all()
    serializer_class = UserGroupPermissionSerializer


class UserPaymentViewSet(viewsets.ModelViewSet):
    queryset = UserPayment.objects.all()
    serializer_class = UserPaymentSerializer


class UserSportViewSet(viewsets.ModelViewSet):
    queryset = UserSport.objects.all()
    serializer_class = UserSportSerializer


class UserSpotViewSet(viewsets.ModelViewSet):
    queryset = UserSpot.objects.all()
    serializer_class = UserSpotSerializer


class UserSpotBasicPlanViewSet(viewsets.ModelViewSet):
    queryset = UserSpotBasicPlan.objects.all()
    serializer_class = UserSpotBasicPlanSerializer


class UserUserGroupViewSet(viewsets.ModelViewSet):
    queryset = UserUserGroup.objects.all()
    serializer_class = UserUserGroupSerializer
