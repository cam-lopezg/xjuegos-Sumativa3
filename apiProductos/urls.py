from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuxCarritoProductoViewSet, ProductoViewSet,ProductosPorCarritoViewSet, CarritoPorUsuarioViewSet, CarritoViewSet

router = DefaultRouter()
router.register(r'carrito/(?P<carrito_id>\d+)/productos', ProductosPorCarritoViewSet, basename='productos-por-carrito')
router.register(r'usuario/(?P<email>.+)/carrito', CarritoPorUsuarioViewSet, basename='carrito-por-usuario')
router.register(r'carritos', CarritoViewSet, basename='carrito')  # Ruta para la creación de carritos
router.register(r'productos', ProductoViewSet, basename='producto')
router.register(r'auxcarritoproducto', AuxCarritoProductoViewSet, basename='auxcarritoproducto')


# URLConf
urlpatterns = [
    path('', include(router.urls)),
]