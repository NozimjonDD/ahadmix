from django.urls import path

from . import views

app_name = 'common'

urlpatterns = [
     # path('', views.index, name='index'),
     path('', views.card,name='card' ),

     # path('old',views.outdoor,name='outdoor' ),
]
