"""
URL configuration for outpass project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('h1/',views.mainscreen,name='h1'),
    path('apply_outpass/',views.apply_outpass,name='apply_outpass'),
    path('submission/',views.apply_outpass,name='submission'),
    path('dashboards/',views.dashboards,name='dashboards'),
    path('get_approval_url/',views.get_approval,name='get_approval_url'),
    path('get_reject_url/',views.get_reject,name='get_reject_url'),
    path('leoni/', views.run_script, name='run_script'),
    

]
