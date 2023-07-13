##main main


from classe_carros import Carros
from classes_atributos import Cadastrouser


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