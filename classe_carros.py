class Carros():
    #Atributo de classe. Aplicado em todos os objetos instanciados nessa classe.
    cor = "Preto"
    
    def __init__ (self, marca, modelo): #metodo construtor de objetos
        self.marca = marca
        self.modelo = modelo
    
    def imprime(self): #não é funçao é METODO
        print("Esse carro é %s e o modelo %s e de cor %s"%(self.marca,self.modelo,Carros.cor))