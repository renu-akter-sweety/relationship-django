
from django.contrib import admin
from django.urls import path
from myproject.views import*
urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/',employeePage,name="employee"),
    path('info/',infoPage,name="info"),
    path('',homePage,name="home"),
    
]
