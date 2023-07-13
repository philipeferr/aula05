
##Atributos publicos de objcts são acessiveis a seus valores
## de qualquer parte do codigo

## Atributos Privados são encapsulados e não sã acessiveis pelo codigo .
## os valores ficam inacessiveis

## Abstração de atributos é == a deixalo publico acessivel
## Encapsulamento de atributos é == a deixalo privado (inacessivel)

## Nomenclatura de atributos publico
## EX self.nome=nome

## nomenclatura de atributos privados utilizamos o doubleUnder __
##EX self.__cpf = cpf

class Cadastrouser():
    def __init__(self,usuario, senha):
        self.usuario = usuario ##publico
        self.__senha = senha ##privado
