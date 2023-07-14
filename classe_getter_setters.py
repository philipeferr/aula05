##getter e setters sao asboas praticas de Gerenciamento abstraão e encapsulamento de
#atributos de uma classe

##por padrão e boas praticas de segurança todos os atributos deixamos encapsulado
##e abstraimos apenas auqeles que necessitam ou podem ficar publicos

##Getters
##Getters é uma boa pratica de abstrair um atributo privado tansformando em um metodo
## em python usamos o decorador @property para declarar um getter

##Setters
## o setter tranforma os valores e ações de um metodo getter e aplica alterações
## em cima de um objeto já instaciado
#permite alterar o valorde um objeto ou metodo sem refatoralo(reescrever)


class Vendasprodutos():
    def __init__(self, produto, quantidade, valor):
        self.__produto = produto
        self.__quantidade= quantidade
        self.__valor = valor

## Aplicar uma abstração com Getter
    @property
    def produto(self):
        return self.__produto
    @property
    def valor(self):
        return self.__valor
    @property
    def quantidade(self):
        return self.__quantidade
##Aplicação de modificações de uma ação ou valor de um metodo existente

    @quantidade.setter
    def quantidade(self,nova_quantidade):
        self.__quantidade = nova_quantidade

    @property
    def valor_total_compra(self):
        return self.__quantidade * self.__valor