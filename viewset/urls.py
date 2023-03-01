from django.contrib import admin
from django.urls import path,include
from testapp import views
from rest_framework.routers import DefaultRouter

routers= DefaultRouter()
routers.register('stulist',views.stulist ,basename='stu')
routers.register('stulist/<int:pk>',views.stulist ,basename='stu')
urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',include(routers.urls)),
]
