from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views


urlpatterns = [
    path('v1/address/state/list/', views.address_state_list),
    path('v1/address/city/list/<int:state>', views.address_city_list),
    path('v1/address/district/list/<int:city>', views.address_district_list),
    path('v1/feed/spot/<int:spot>', views.feed_spot_list),
    path('v1/plain/list', views.plain_list),
    path('v1/plan/list', views.plan_list),
    path('v1/sport/list', views.sport_list),
]
