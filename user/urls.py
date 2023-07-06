from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path('',views.homepage),
    path('index/', views.index),
    path('showregister/',views.showregister),
    path('register/',views.register),
    path("adddata/",views.Add_data),
    path('checkname/',views.checkname),
    path('login/',views.login),
    path('endpage/',views.endpage),
    path('adddata/',views.adddata),
    path('viewdata/',views.viewdata),
    path('updatedata',views.updatedata),
    path('deletedata/',views.deletedata),
    

]

