"""Proyectos_notas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from postres import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('profesores/',views.profesor, name='profesor'),
    path('notas/', views.notas, name='notas'),
    path('anotaciones/', views.anotaciones, name='anotaciones'),
    path('actividadesp/',views.actividadesp,name='actividadesp'),
    path('alumno/',views.alumno,name='alumno'),
    path('notasal/',views.notasal,name='notasal'),
    path('actividadesal/',views.actividadesal, name='actividadesal'),
    path('loginalumno/',views.logina,name="loginalumno"),
    path('loginprofesor/',views.loginp,name='loginprofesor'),
    path('loginapoderado/',views.loginap,name='loginapoderado'),
    path('apoderados/',views.apoderados,name='apoderados'),
 

    
]
