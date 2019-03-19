# 15) Escreva um programa que leia três coordenadas, verifique se as mesmas formam um triângulo e construam o objeto da classe triângulo. Por fim o programa mostra o tipo do triângulo: Escaleno, Isósceles ou Equilátero.

if(((b - c) < a < (b + c)) and ((a - c) < b < (a + c)) and ((a - b) < c < (a + b))):
    chama = Triangulo(a, b, c)
    
class Triangulo:
    def __init__ (self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
    def _get_a(self):
        return self._a
    def _get_b(self):
        return self._b
    def _get_c(self):
        return self._c
    def _set_a(self, a):
        self._xa = a
    def _set_b(self, b):
        self._b = b
    def _set_c(self, c):
        self._c = c
    a = property(_get_a, _set_a)
    b = property(_get_b, _set_b)
    c = property(_get_c, _set_c)
    def verifica (self):
        if (((a == b) and != c)) or ((c == b) and != a)) or ((a == c) and != b))):
            print("O triângulo é isósceles")
        elif ((a == b == c)):
            print("O triângulo é equilátero")
        else:
            print("O triângulo é escaleno")
