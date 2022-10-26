from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('catagory/', views.catagory, name='catagory'),
    path('item/', views.item, name='item'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)