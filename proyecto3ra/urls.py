"""
URL configuration for proyecto3ra project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from aplicacion.views import inicio, lista_estudiantes, nuevo_estudiante, editar_estudiante,eliminar_estudiante,ver_estudiante
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',admin.site.urls, name='admin'),
    path('', inicio, name='inicio'),
    path('estudiantes/', lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/nuevo/', nuevo_estudiante, name='nuevo_estudiante'),
    path('estudiantes/<int:estudiante_id>/', ver_estudiante, name='ver_estudiante'),
    path('estudiantes/<int:estudiante_id>/editar/', editar_estudiante, name='editar_estudiante'),
    path('estudiantes/<int:estudiante_id>/eliminar/', eliminar_estudiante, name='eliminar_estudiante'),
    path('usuarios/', include('usuarios.urls')),
    path('chat/', include('mensajeria.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
