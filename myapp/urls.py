from django.urls import path
from .import views
urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contacts/',views.contacts,name='contacts'),
    path('tracker/',views.tracker,name='tracker'),
    path('search/',views.search,name='search'),
    path('productview/<int:id>',views.productview,name='productview'),
    path('checkout/',views.checkout,name='checkout'),
]