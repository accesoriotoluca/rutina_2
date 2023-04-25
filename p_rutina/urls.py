"""
! -------------  ARCHIVO ORIGINAL CREADO X DJANGO  ----------------------------

?1. Establecer las urls que los clientes o los usuarios pueden visitar
?2. ejemplo: ruta llamada about para ir a la página/vista 'acerca de' (productos, categorías, tu puta madre, etc.)
* carpeta_proyecto_django URL Configuration
"""

"""
URL configuration for p_rutina project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

# como se han separado las urls en otro archivo, se necesitan integrar al este archivo de urls original con el módulo include() incluye un bloque de url de otra app
# importar views puede ser 'carpeta_aplicacion_1 import views' y en función 'views.view_fun_hello'

from django.contrib import admin
from django.urls import path, include

"""
1. crea nueva 'rutas/url' (nombre en blanco = 'rutas/url o dominio principal o localhost 3000')
2. 'ruta_acerca_de/' = 'http://127.0.0.1:8000/ruta_acerca_de'
3. cada vez que entra en 'ruta_acerca_de/' ejecuta función 'view_fun_acerca_de'
3.1 se ejecuta código cada vez que una rutas/url es visitada
4. carpetas aplicaciones pueden guardar su propio archivo de rutas/urls
4.1 si este archivo deja de tener funciones de vistas de una carpeta/app entonces se puede borrar de aqui e importarlos desde el nuevo archivo urls que se creé 
4.2 este archivo url es el módulo principal configuraciones globales
4.3 si el primer parámetro de path tiene una ruta, esta presede de todo el bloque de urls de include(,) """

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('app_rutina.rutina_urls')),

]
