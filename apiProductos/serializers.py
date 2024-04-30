from rest_framework import serializers
from .models import Producto, AuxCarritoProducto, Carrito
from apiUsuarios.models import Usuario 

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio']

class AuxCarritoProductoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    class Meta:
        model = AuxCarritoProducto
        fields = ['producto', 'cantidad']

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = ['id', 'usuario']

    def validate_usuario(self, value):
        """
        Verifica que el usuario exista antes de permitir la creación de un carrito.
        """
        if not Usuario.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Usuario no válido o no existe.")
        return value
    
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio']

from rest_framework import serializers
from .models import AuxCarritoProducto, Carrito, Producto

class AuxCarritoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuxCarritoProducto
        fields = ['id', 'carrito', 'producto', 'cantidad']

    def validate(self, data):
        """
        Añade validaciones personalizadas si es necesario, como verificar stock o restricciones específicas.
        """
        # Por ejemplo, asegurarse de que la cantidad no es negativa
        if data['cantidad'] < 1:
            raise serializers.ValidationError("La cantidad debe ser al menos 1.")
        return data