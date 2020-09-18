from django.urls import path,include
from django.conf.urls import url
from .views import RegisterView,LoginView,profile

urlpatterns = [
    url(r'^api/register/$',RegisterView.as_view(),name='register'),
    url(r'^api/login/$',LoginView.as_view(),name='login'),
    url(r'^api/profile/(?P<unique_id>.+?)/$',profile,name='profile'),
]