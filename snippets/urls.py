from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

router = DefaultRouter()
router.register(r'address', views.AddressViewSet)
router.register(r'address/country/list', views.AddressCountryViewSet)
router.register(r'address/state/list', views.AddressStateViewSet)
router.register(r'address/city/list', views.AddressCityViewSet)
router.register(r'address/district/list', views.AddressDistrictViewSet)
router.register(r'feed', views.FeedViewSet)
router.register(r'plain/list', views.PlainViewSet)
router.register(r'plan/list', views.PlanViewSet)
router.register(r'sport/list', views.SportViewSet)
router.register(r'spot/list', views.SpotViewSet)
router.register(r'partner', views.PartnerViewSet)
router.register(r'route', views.RouteViewSet)
router.register(r'spot/condition', views.SpotConditionViewSet)
router.register(r'spot/tide', views.SpotTideViewSet)
router.register(r'spot/advertising', views.AdvertisingSpotViewSet)
router.register(r'setting/list', views.SettingViewSet)

router.register(r'user/spot', views.UserSpotViewSet)
router.register(r'user/sport', views.UserSportViewSet)
router.register(r'user/subscription', views.UserSubscriptionViewSet)
router.register(r'user/activation', views.UserSubscriptionViewSet)
router.register(r'user/logout', views.UserLogoutViewSet)
router.register(r'user/device', views.UserDeviceViewSet)
router.register(r'user/loginwithfacebook', views.UserLoginWithFacebookViewSet)
router.register(r'user/changepassword', views.UserChangePasswordViewSet)
router.register(r'user/freespots', views.UserSpotBasicPlanViewSet)

router_v2 = DefaultRouter()
router_v2.register(r'user/device', views.UserDeviceV2ViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v2/', include(router_v2.urls)),
]

urlpatterns += [
    # path('v1/user/spot/<int:test>', views.spot)
]
