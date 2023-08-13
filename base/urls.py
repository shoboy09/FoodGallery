from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('reservation/', views.reservation, name="reservation"),
    path('contact/', views.contact, name="contact"),
    path('menu/', views.menu, name="menu"),
    path('wew/', views.wew, name="wew"),
    path('getItems/<int:category_id>/', views.getItems, name='get_items'),
]
