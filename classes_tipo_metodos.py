## Existem 4 tipos de metodos em python
## 1-Metodo de intancia que leva como argumento(atributo) o SELF 
## 2-Metodo de classe que é definido pelo decorador @classmethod
## 3-Metodo etsatico que gera um valor estatico(Parecido com atributo de classe)
##  que leva o decorador @staticmethod
## 4- Privete Method (metodo privado == inutil)

## 1- Metodos de Instancia
class Livros():
    ano_atual = 2023
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano  = ano
    def imprime(self):
        print("Esse livro é %s e o Autor %s"%(self.titulo,self.autor))

    def anoPublicacao(self):
        print("Tempo de publicação",self.ano_atual-self.ano,"anos")
    
    ## 2- Metodo de Classe, usamos o decorador @classmethod

    @classmethod
    def calculoAnoPubli(anoclasse,nome,ano):
        calculo = anoclasse.ano_atual - ano
        return(nome,"tempo publicação é",str(calculo),"anos")
    
    