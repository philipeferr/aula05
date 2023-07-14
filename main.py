##main main


from classe_carros import Carros
from classes_atributos import Cadastrouser
from classe_getter_setters import Vendasprodutos
from classes_tipo_metodos import Livros
##intanciando objetos

carro1 = Carros("Chevette","Chevrolet")
carro2 = Carros("Focus","Ford")
carro3 = Carros("Fox", "Volkswagen")

carro1.imprime()
print(carro3.modelo)

##Exibião de atributos de classe

print(Carros.cor)

##Usar o metodo magico __dict__ para listar atributos de objct e classe

print(carro3.__dict__)

print(Carros.__dict__)

user1 = Cadastrouser('João',1234)
user2= Cadastrouser('Miguel', 777222)
#print(user1.__senha)

#o metodo naming mangling é usadono python para forçar a exibição de um valor
## de atributo privado
##o metodo magico dir

print(dir(user1))
print(user1._Cadastrouser__senha)

print(user1.__dict__)
print(user2.__dict__)


#produtos

produto1 = Vendasprodutos('Feijao',10,9.50)
produto2 = Vendasprodutos("Macarrao",5,6.60)

#print(produto.__valor)

print(produto1.produto)
print(produto1.quantidade)
print(produto2.quantidade)

##Ajustar a quantidade

produto1.quantidade = 20
produto2.quantidade = 10


print(produto1.quantidade)
print(produto2.quantidade)

print(produto1.valor_total_compra)

##Livros

livro1 = Livros('O Pequeno Principe',"Esuperri",1960)
livro2 = Livros('as cronicas de peter pan', 'maldova', 1930)

livro1.imprime()
livro1.anoPublicacao()