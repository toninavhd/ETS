from abc import ABC, abstractmethod

class MiClaseAbstracta(ABC):
    @abstractmethod
    def mi_metodo_abstracto(self):
        pass

class MiClaseConcreta(MiClaseAbstracta):
    def mi_metodo_abstracto(self):
        return "Implementación concreta del método abstracto"

# Intentemos crear una instancia de la clase concreta
try:
    obj = MiClaseConcreta()
    print(obj.mi_metodo_abstracto())
except TypeError:
    print("No se puede crear una instancia de una clase abstracta.")
