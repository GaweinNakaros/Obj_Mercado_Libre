## Programación Orientada a Objetos (POO)
 ## Conceptos Clave de POO
 ## Clases y Objetos: Definen estructuras de datos con comportamiento encapsulado.
 ## Encapsulamiento: Restringe el acceso directo a los atributos de un objeto.
 ## Herencia: Permite que una clase derive de otra y reutilice su funcionalidad.
 ## Polimorfismo: Habilidad de diferentes clases para compartir la misma interfaz.
 ##Decoradores y Métodos Especiales: Uso de @property, __str__, __repr__, entre otros.


## Ejercicio 1: Crear una clase Producto con métodos para modificar precio y stock
## 🔹 Explicación:
## ✔️ Creamos una clase Producto con atributos nombre, _precio y _stock.
## ✔️ Métodos para actualizar el precio y modificar el stock con validaciones.
## ✔️ Usamos __str__ para mostrar los datos del producto fácilmente.

class Producto:
    """
    Clase que representa un producto en un sistema de gestión de inventario.
    """
    
    def __init__(self, nombre: str, precio: float, stock: int):
        """
        Constructor de la clase Producto.
        
        :param nombre: Nombre del producto
        :param precio: Precio del producto en pesos
        :param stock: Cantidad de unidades disponibles en stock
        """
        self.nombre = nombre
        self._precio = precio  # Usamos _precio con _ para indicar que es "privado"
        self._stock = stock

    def actualizar_precio(self, nuevo_precio: float):
        """
        Actualiza el precio del producto.
        
        :param nuevo_precio: Nuevo precio en pesos
        """
        if nuevo_precio > 0:
            self._precio = nuevo_precio
        else:
            raise ValueError("El precio debe ser mayor a 0")

    def modificar_stock(self, cantidad: int):
        """
        Modifica la cantidad de stock disponible.
        
        :param cantidad: Número de unidades a agregar o restar
        """
        if self._stock + cantidad >= 0:
            self._stock += cantidad
        else:
            raise ValueError("No se puede tener stock negativo")

    def __str__(self):
        """
        Representación en string del producto.
        """
        return f"Producto: {self.nombre}, Precio: ${self._precio}, Stock: {self._stock}"


# Uso de la clase
producto1 = Producto("Media Sombra 4x50", 11500, 10)

print(producto1)  # Muestra los datos iniciales

producto1.actualizar_precio(12000)  # Cambia el precio
producto1.modificar_stock(-2)  # Vende 2 unidades

print(producto1)  # Muestra los datos actualizados


## 🔹 Ejercicio 2: Hacer una versión con @property y async
## 🔹 Explicación:
## ✔️ Usamos @property y @precio.setter para manejar getters y setters.
## ✔️ Método async def modificar_stock para simular una operación asíncrona.
## ✔️ Ejecutamos asyncio.run(main()) para esperar la actualización del stock.


class ProductoAsync:
    """
    Clase Producto con métodos asíncronos y uso de @property para acceder a los valores privados.
    """
    
    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre = nombre
        self._precio = precio
        self._stock = stock

    @property
    def precio(self):
        """Getter del precio"""
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        """Setter del precio con validación"""
        if nuevo_precio > 0:
            self._precio = nuevo_precio
        else:
            raise ValueError("El precio debe ser mayor a 0")

    @property
    def stock(self):
        """Getter del stock"""
        return self._stock

    async def modificar_stock(self, cantidad: int):
        """
        Modifica la cantidad de stock de manera asíncrona.
        
        :param cantidad: Número de unidades a agregar o restar
        """
        import asyncio
        await asyncio.sleep(1)  # Simula una operación de base de datos
        if self._stock + cantidad >= 0:
            self._stock += cantidad
        else:
            raise ValueError("No se puede tener stock negativo")

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: ${self._precio}, Stock: {self._stock}"


# Uso de la clase asíncrona
import asyncio

producto2 = ProductoAsync("Media Sombra 4x50", 11500, 10)
print(producto2)

producto2.precio = 12500  # Cambia el precio

async def main():
    await producto2.modificar_stock(-3)  # Vende 3 unidades
    print(producto2)

asyncio.run(main())

