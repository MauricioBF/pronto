# 11) Escreva uma classe pessoa com suas propriedades e um método __str__ para refazer o exercício 8.
# "8) Leia os dados de uma pessoa: nome, dataNascimento, telefone (1 ou mais). Guarde-os em uma só variável e imprima os dados. Use a classe dict."

class Pessoa:
    def __init__ (self, nome, dataNascimento, telefone):
        self._nome = nome
        self._dataNascimento = dataNascimento
        self._telefone = telefone
    def _get_nome(self):
        return self._nome
    def _get_dataNascimento(self):
        return self._dataNascimento
    def _get_telefone(self):
        return self._telefone
    def _set_nome(self, nome):
        self._nome = nome 
    def _set_dataNascimento(self, dataNascimento):
        self._dataNascimento = dataNascimento
    def _set_telefone(self, telefone):
        self._telefone = telefone
    def __str__(self):
        return "nome:{}, nascimento:{}, telefone:{}".format(self._nome, self._dataNascimento, self._telefone)
        
d = Pessoa("Yudi", "12/11/10",40028922)
print(d)