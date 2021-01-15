from django.urls import path, include
from rest_framework.routers import DefaultRouter
from default import views

router = DefaultRouter()

router.register('AccessLog', views.AccessLogViewSet)
router.register('AccessLogArchive', views.AccessLogArchiveViewSet)
router.register('Address', views.AddressViewSet)
router.register('AddressCity', views.AddressCityViewSet)
router.register('AddressCountry', views.AddressCountryViewSet)
router.register('AddressDistrict', views.AddressDistrictViewSet)
router.register('AddressState', views.AddressStateViewSet)
router.register('Advertising', views.AdvertisingViewSet)
router.register('AdvertisingPage', views.AdvertisingPageViewSet)
router.register('AdvertisingSpot', views.AdvertisingSpotViewSet)
router.register('AdvertisingType', views.AdvertisingTypeViewSet)
router.register('AdvertisingZone', views.AdvertisingZoneViewSet)
router.register('Api', views.ApiViewSet)
router.register('AuthGroup', views.AuthGroupViewSet)
router.register('AuthGroupPermissions', views.AuthGroupPermissionsViewSet)
router.register('AuthPermission', views.AuthPermissionViewSet)
router.register('AuthUser', views.AuthUserViewSet)
router.register('AuthUserGroups', views.AuthUserGroupsViewSet)
router.register('AuthUserUserPermissions', views.AuthUserUserPermissionsViewSet)
router.register('Campaign', views.CampaignViewSet)
router.register('Category', views.CategoryViewSet)
router.register('Condition', views.ConditionViewSet)
router.register('Coupon', views.CouponViewSet)
router.register('CouponCode', views.CouponCodeViewSet)
router.register('CouponUsage', views.CouponUsageViewSet)
router.register('Device', views.DeviceViewSet)
router.register('DjangoAdminLog', views.DjangoAdminLogViewSet)
router.register('DjangoContentType', views.DjangoContentTypeViewSet)
router.register('DjangoMigrations', views.DjangoMigrationsViewSet)
router.register('DjangoSession', views.DjangoSessionViewSet)
router.register('Email', views.EmailViewSet)
router.register('EmailContext', views.EmailContextViewSet)
router.register('EmailQueue', views.EmailQueueViewSet)
router.register('Feed', views.FeedViewSet)
router.register('FeedMedia', views.FeedMediaViewSet)
router.register('FeedMessage', views.FeedMessageViewSet)
router.register('FeedMessageOption', views.FeedMessageOptionViewSet)
router.register('Media', views.MediaViewSet)
router.register('Menu', views.MenuViewSet)
router.register('News', views.NewsViewSet)
router.register('NewsMedia', views.NewsMediaViewSet)
router.register('Notification', views.NotificationViewSet)
router.register('NotificationFilter', views.NotificationFilterViewSet)
router.register('NotificationStatus', views.NotificationStatusViewSet)
router.register('Order', views.OrderViewSet)
router.register('OrderData', views.OrderDataViewSet)
router.register('OrderItem', views.OrderItemViewSet)
router.register('OrderLog', views.OrderLogViewSet)
router.register('OrderPayment', views.OrderPaymentViewSet)
router.register('OrderPaymentCallback', views.OrderPaymentCallbackViewSet)
router.register('OrderPaymentRequest', views.OrderPaymentRequestViewSet)
router.register('OrderStatus', views.OrderStatusViewSet)
router.register('Partner', views.PartnerViewSet)
router.register('PartnerCategory', views.PartnerCategoryViewSet)
router.register('PaymentAcquirer', views.PaymentAcquirerViewSet)
router.register('PaymentGateway', views.PaymentGatewayViewSet)
router.register('PaymentMethod', views.PaymentMethodViewSet)
router.register('PaymentStatus', views.PaymentStatusViewSet)
router.register('PaymentType', views.PaymentTypeViewSet)
router.register('Permission', views.PermissionViewSet)
router.register('Plan', views.PlanViewSet)
router.register('PlanPaymentType', views.PlanPaymentTypeViewSet)
router.register('PlanResource', views.PlanResourceViewSet)
router.register('PlanSpot', views.PlanSpotViewSet)
router.register('Promotion', views.PromotionViewSet)
router.register('PromotionPaymentType', views.PromotionPaymentTypeViewSet)
router.register('PromotionPlan', views.PromotionPlanViewSet)
router.register('PushQueue', views.PushQueueViewSet)
router.register('Resource', views.ResourceViewSet)
router.register('Route', views.RouteViewSet)
router.register('Session', views.SessionViewSet)
router.register('Setting', views.SettingViewSet)
router.register('SmsQueue', views.SmsQueueViewSet)
router.register('Sport', views.SportViewSet)
router.register('Spot', views.SpotViewSet)
router.register('Subscription', views.SubscriptionViewSet)
router.register('SubscriptionLog', views.SubscriptionLogViewSet)
router.register('Tide', views.TideViewSet)
router.register('TideData', views.TideDataViewSet)
router.register('User', views.UserViewSet)
router.register('UserGroup', views.UserGroupViewSet)
router.register('UserGroupMenu', views.UserGroupMenuViewSet)
router.register('UserGroupPermission', views.UserGroupPermissionViewSet)
router.register('UserPayment', views.UserPaymentViewSet)
router.register('UserSport', views.UserSportViewSet)
router.register('UserSpot', views.UserSpotViewSet)
router.register('UserSpotBasicPlan', views.UserSpotBasicPlanViewSet)


urlpatterns = [
    path('', include(router.urls))
]
