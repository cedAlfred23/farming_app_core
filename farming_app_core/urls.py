from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', views.home),
    # path('about/', views.about),
    path('api/v1/auth/', include('accounts.urls')),
    re_path("login", views.login),
    re_path("signup", views.signup),
    re_path("test_token", views.test_token),
]
