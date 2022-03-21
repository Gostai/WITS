from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from app import views
from rest_framework.authtoken import views as Tviews


app_name = 'app'

urlpatterns = [
    path('app/', views.OpinionList.as_view()),
    path('app/<int:pk>/', views.OpinionDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    
    path('auth/', Tviews.obtain_auth_token),
    path('register/activate/<str:sign>/', views.user_activate, name='register_activate'),
    path('register/', views.UserRegister.as_view()),
    ]




urlpatterns = format_suffix_patterns(urlpatterns)
