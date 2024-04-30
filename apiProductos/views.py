from rest_framework import viewsets
from .models import Carrito, AuxCarritoProducto, Producto
from .serializers import CarritoSerializer, ProductoSerializer ,AuxCarritoProductoSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response

class ProductosPorCarritoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AuxCarritoProducto.objects.all()
    serializer_class = AuxCarritoProductoSerializer

    def get_queryset(self):
        """
        Filtra el queryset por carrito_id pasado como parámetro en la URL.
        """
        carrito_id = self.kwargs['carrito_id']
        return self.queryset.filter(carrito__id=carrito_id)

class CarritoPorUsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

    def get_queryset(self):
        """
        Filtra el queryset por el email del usuario pasado como parámetro en la URL.
        """
        usuario_email = self.kwargs['email']
        return self.queryset.filter(usuario__email=usuario_email)

class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        # Si no deseas que se liste nada, puedes devolver una respuesta vacía o ajustar según las necesidades.
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class AuxCarritoProductoViewSet(viewsets.ModelViewSet):
    queryset = AuxCarritoProducto.objects.all()
    serializer_class = AuxCarritoProductoSerializer