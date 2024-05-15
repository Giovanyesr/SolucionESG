import math
class EcuacionSegundoGrado:
    def calculoESG(self,a,b,c):
        discriminante = math.pow(b,2) - 4 * a * c
        if discriminante >= 0:
            raizDiscriminante =math.sqrt(discriminante)
            raiz1 = (-b + raizDiscriminante) / (2 * a)
            raiz2 = (-b - raizDiscriminante) / (2 * a)

        return raiz1,raiz2
