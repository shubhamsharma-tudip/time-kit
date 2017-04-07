from django.conf.urls import include, url
from django.contrib import admin
from guest import views as guest_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', guest_views.index, name='index'),
    url(r'^login/$', guest_views.usersubmit, name='usersubmit'),
    url(r'^logout/$', guest_views.user_logout, name='userlogout'),
    url(r'^calender/$',guest_views.usercalender, name='usercalender'),
    url(r'^entry/$',guest_views.entryview, name='entryview'),
    url(r'^user_login/$', guest_views.user_login, name='user_login'),
    url(r'^signup/user/$', guest_views.signup, name='signup'),
    url(r'^signup/timekit/$',guest_views.timekit_signup, name='timekit_signup' ),
    url(r'^login/timekit/$',guest_views.timekit_login, name="timekit_login"),
    url(r'^user/appsignup/$',guest_views.app_signup, name='app_signup'),
    url(r'^user/applogin/$',guest_views.app_login, name='app_login'),
    url(r'^reset/password/$',guest_views.reset_password, name="reset_password"),
    url(r'^reset_app_password/$',guest_views.reset_app_password, name="reset_app_password"),
    url(r'^update/details/$',guest_views.update_details, name="update_details"),
    url(r'^update/content/$',guest_views.update_content, name="update_content"),
    url(r'^guest/math/booking/$', guest_views.math_booking, name='math_booking'),
    url(r'^guest/physics/booking/$', guest_views.physics_booking, name='physics_booking'),
    url(r'^guest/chemistry/booking/$',guest_views.chemistry_booking, name='chemistry_booking'),
]


