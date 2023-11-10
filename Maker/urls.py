"""
URL configuration for Maker project.

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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Aplications.productos.views import cart,modify_p,carga_p,search,search_c,practica,producto_delete
from Aplications.Usuarios.views import prueba,User_regist,home,log_out,init,proba,tomail,carta
from Aplications.carrito.views import int,updateItem,carrito,carrito_clean
urlpatterns = [
    path('admin/', admin.site.urls),
    path('lost/',prueba),
    path('',home,name='padre'),
    path('registro/',User_regist,name='registro'),
    path('logout/',log_out,name='logout'),
    path('inicio/',init,name='inicio'),
    path('send/', proba,name='send'),
    path('send_mail/', tomail ,name='send_mail'),
    path('carti/<id>/', cart,name='carti'),
    path('modify/<id>/', modify_p, name='modify'),
    path('cargar/',carga_p,name='cargar'),
    path('del_item/<id>/',producto_delete,name='del_item'),
    path('sub/',int ,name= 'sub'),
    path('cart/',carrito,name='cart'),
    path('update_item/',updateItem,name='update_item'),
    path('clear/',carrito_clean,name='clear'),
    path('card/',carta,name='card'),
    path('buscar/', search,name='buscar'),
    path('cate/<categoria_id>/',search_c,name='cate'),
    path('intento/',practica,name='intento'),
    
]

from django.conf import settings

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)