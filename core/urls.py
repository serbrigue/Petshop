from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.inicio_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('peo',views.peo, name='peo'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
    path('eliminar_producto/<int:item_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('cambiar_cantidad/<int:item_id>/<int:nueva_cantidad>/', views.cambiar_cantidad, name='cambiar_cantidad'),
    path('pago/', views.procesar_pago, name='payment'),
    path('confirmacion_pago/,',views.confirmacion_pago, name='confirmacion_pago'),
    path('producto/<str:slug>/', views.producto_individual, name='producto_individual'),
    path('productos/categoria/<str:categoria>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('productos/categoria/<str:categoria_nombre>/<str:marca_nombre>/', views.productos_por_categoria_marca, name='productos_por_categoria_marca'),
    path('productos/animal/<str:animal_nombre>/<str:categoria_nombre>/', views.producto_animal_categoria, name='producto_animal_categoria'),
    path('productos/animal/<str:animal_nombre>/', views.productos_por_animal, name='productos_por_animal'),
    
]




