"""settings URL Configuration

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
from currency.views import contact_us, rate_list, source_create, source_delete, source_list, source_update


from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact-us/', contact_us),
    path('rate-list/', rate_list),
    path('source-list/', source_list),
    path('source-list/create/', source_create),
    path('source-list/update/<int:pk>/', source_update),
    path('source-list/delete/<int:pk>/', source_delete)
]
