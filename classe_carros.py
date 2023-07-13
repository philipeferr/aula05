class Carros():
    def __init__ (self, marca, modelo): #metodo criador de objetos
        self.marca = marca
        self.modelo = modelo
    
    def imprime(self): #não é funçao é METODO
        print("Esse carro é %s e o modelo %s"%(self.marca,self.mdelo))