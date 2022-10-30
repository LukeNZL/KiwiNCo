from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:item_id>/', views.item, name='item'),
    path('<str:catagory>/', views.catagory, name='catagory'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)