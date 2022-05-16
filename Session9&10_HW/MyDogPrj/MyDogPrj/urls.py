"""MyDogPrj URL Configuration

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
from django.contrib import admin
from django.urls import path
from BoardApp import views
from BoardApp.views import PostCreate, PostUpdate

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.list_post, name='home'),
    path('detail/<int:post_pk>', views.detail_post, name='detail_post'),
    path('update/<int:pk>', PostUpdate.as_view(), name='update_post'),
    path('create_post/', PostCreate.as_view(), name='create_post'),
    path('delete_post/<int:post_pk>', views.delete_post, name='delete_post'),
    path('delete_comment/<int:comment_pk>', views.delete_comment, name='delete_comment')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)