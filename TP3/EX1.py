from abc import ABC, abstractmethod

class Forme(ABC):
    @abstractmethod
    def calculer_surface():
        pass
    
class Circle(Forme):
    def calculer_surface(rayon):
        return (rayon ** 2) * 3.14

class Rectangle(Forme):
    def calculer_surface(long, larg):
        return long * larg
        


print(Circle.calculer_surface(10))
print(Rectangle.calculer_surface(10, 20))



