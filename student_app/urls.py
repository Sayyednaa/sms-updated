"""student_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# in student_app/urls.py
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include

from django.contrib import admin
from .views import home
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('todo/', include('todo.urls')),
    path('notes/', include('notes.urls')),
    path('time/', include('daily.urls')),
    path('test/', include('test.urls')),
    path('login',views.loginUser),
    path('logout',views.logoutUser),
    path('forgot_password',views.forgetPass),
    path('signup',views.createac),
    path('profile',views.user_profile),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
