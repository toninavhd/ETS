from abc import ABC, abstractmethod

# Interfaz común para los productos
class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

# Implementación concreta de la interfaz
class ConcreteProductA(Product):
    def operation(self) -> str:
        return "Operación realizada por ConcreteProductA"

class ConcreteProductB(Product):
    def operation(self) -> str:
        return "Operación realizada por ConcreteProductB"

# Creator (clase abstracta que define el Factory Method)
class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Cliente: {product.operation()}"
        return result

# Implementación concreta del Creator
class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()

def client_code(creator: Creator) -> None:
    print(creator.some_operation())

if __name__ == "__main__":
    client_code(ConcreteCreatorA())  # Salida: "Cliente: Operación realizada por ConcreteProductA"
    client_code(ConcreteCreatorB())  # Salida: "Cliente: Operación realizada por ConcreteProductB"
