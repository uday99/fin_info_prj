"""SampleEmp_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from SampleEmp_task import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/emp/',views.CreateEmp.as_view(),name='creat_emp'),
    path('list/emp/',views.List_Allemp.as_view(),name='list_emp'),
    path('one/emp/<regid>/',views.Read_One_Emp.as_view(),name='one_emp'),
    path('update/emp/<regid>/',views.Update_Emp.as_view(),name='modify_emp'),
    path('delete/emp/',views.Delete_Emp.as_view(),name='delete_emp')

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)