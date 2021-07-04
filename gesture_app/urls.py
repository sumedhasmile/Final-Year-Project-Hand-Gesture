from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('navigate_vedio/', views.Navigate_Vedio, name='navigate'),
    path('navigate_ppt/', views.Navigate_Player, name='navigate_ppt'),
    path('navigate_paint/',views.PaintWindow,name='navigate_paint'),
    path('home',views.Home,name='home'),
]