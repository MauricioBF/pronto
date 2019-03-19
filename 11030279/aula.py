#Exemplo de classe com decoração

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome 
        self._idade = idade 
    @propertyidade
    def idade (self):
         return self._idade
    @idade.setter
    def idade (self, idade):
         self._idade = idade
    @propertynome
    def nome (self):
        return self._nome
    @nome.setter
    def nome (self, nome):
        self._nome = nome

#Exemplo de classe sem decoração

class  Animal:
    def __init__(self, apelido, patas):
        self._apelido = apelido 
        self._patas = patas
    def _get_apelido(self):
        return self._apelido
    def _get_patas(self):
        return self._patas
    def _set_apelido(self, apelido):
        self._apelido = apelido 
    def _set_patas(self, patas):
        self._patas = patas
    
    nome = property(_set_nome, _get_nome)
    patas = property(_set_patas, _get_patas)