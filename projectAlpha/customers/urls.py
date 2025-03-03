

from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('success/', views.success_view, name='success')
]
