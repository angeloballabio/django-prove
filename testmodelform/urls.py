from django.urls import path
from . import views #index, testmodelform

#da qui i vari indirizzi per le pagine
urlpatterns = [
    path('', views.index, name='index'),
    path('testform/', views.testform , name='testform'),
    path('ModificaPubblicita/<int:pk>/', views.ModificaPubblicita, name='modifica_pubblicita'),
]