from django.contrib import admin
from django.urls import path, include
from esoapp import views

appname = "esoapp"

urlpatterns = [
    path('esochoose/', views.esochoose, name="esochoose"),
    path('brainfuck/', views.brainfuck, name="brainfuck"),
    path('about/', views.about, name="about"),
    path('spl/', views.spl, name="spl"),
    path('malbolge/', views.malbolge, name="malbolge"),
    path('esoterrible/', views.esoterrible, name="esoterrible"),
    path('example/', views.example, name="example"),
]
