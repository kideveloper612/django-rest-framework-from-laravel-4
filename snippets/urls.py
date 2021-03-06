from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views


urlpatterns = [
    path('v1/address/state/list/', views.address_state_list),
    path('v1/address/city/list/<int:state>/', views.address_city_list),
    path('v1/address/district/list/<int:city>/', views.address_district_list),
    path('v1/feed/spot/', views.feed_spot_list),
    path('v1/feed/spot/<int:spot>/', views.feed_spot_list_detail),
    path('v1/plain/list/', views.plain_list),
    path('v1/plan/list/', views.plan_list),
    path('v1/sport/list/', views.sport_list),
    path('v1/spot/list', views.spot_list),
    path('v1/spot/list/', views.spot_list),
    path('v1/spot/list/<int:spot>/', views.spot_list_detail),
    path('v1/user/spot/<int:user>/', views.user_spot_list),
    path('v1/user/spot/<int:user>/<int:spot>/', views.user_spot_list_detail),
    path('v1/user/sport/<int:user>/', views.user_sport_list),
    path('v1/user/sport/<int:user>/<int:sport>/', views.user_sport_list_detail),
    path('v1/user/subscription/<int:user>/', views.user_subscription_list),
    path('v1/user/activation/<str:code>/', views.user_activation_code),
    path('v1/spot/condition/<int:spot>/', views.spot_condition_list),
    path('v1/spot/tide/<int:tide>/', views.spot_tide_list),
    path('v1/spot/advertising/<int:spot>/', views.spot_advertising_list),
    path('v1/spot/advertising/<int:spot>/<int:user>/', views.spot_advertising_user_list),
    path('v1/setting/list/', views.setting_list),
    path('v1/plan/isbasicplan/', views.plan_basic_list),
    path('v1/plan/basicplan2/', views.plan_basic2_list),

    path('v1/coupon/check', views.coupon_check),
    path('v1/user/update', views.user_update),
    path('v1/user/updateSpot', views.user_update_spot),
    path('v1/user/updateSport', views.user_update_sport),
    path('v1/user/login', views.user_login),
    path('v1/user/logout', views.user_logout),
    path('v1/user/device', views.user_device),
    path('v1/user/loginwithfacebook', views.user_loginwithfacebook),
    path('v1/user/register', views.user_register),
    path('v1/user/checkEmail', views.user_checkEmail),
    path('v1/user/changePassword', views.user_changePassword),
    path('v1/email/sendActivationCode', views.email_sendActivationCode),
    path('v1/notification/send', views.notification_send),
    path('v1/notification/register', views.notification_register),

    path('v1/user/freespots', views.user_freespots),
    path('v1/user/credits', views.user_credits),
    path('v1/user/creditsrenew', views.user_creditsrenew),
    path('v1/spot/spotstatus', views.spot_spotstatus),
    path('v1/user/spot/pb2', views.user_spot_pb2),



    path('apple/allowed', views.apple_allowed),
    path('app/checkVersionByCode', views.app_checkVersionByCode),


    path('v2/user/device', views.v2_user_device),
    path('v2/device/register', views.v2_user_device),
]
