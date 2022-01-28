# class 

# syntax

class Computador:
    #construtor com dados que serao usados 
    def __init__(self,marca:str,memoria="8gb"):
        #marca, memoria , placa de video
        self.marca = marca
        self.memoria = memoria
        self.placa = "Nvidia"
        print(self.ligar())

    def ligar(self):
        return  "ligando compiuri"

    def desligar(self):
        print("desligando")

    infos = lambda self: print(f"marca:{self.marca}, memoria:{self.memoria}, placa:{self.placa}")


#comp  = Computador("asus","12gb")
#comp.infos()
#comp.marca = "Samsung"
#comp.infos()

#=================================================================================================

class Heranca(Computador):
    def __init__(self):
        super().__init__(marca="aaaaaa")

    def elemento(self):
        print("bateria " + self.marca + f" but memory the {self.memoria} " + self.placa)

hr = Heranca()

#hr.infos()
hr.elemento()

"""se passa outro construtor para minha class Heranca sera chamado de polimorfismo
que e atribuição de outros valores ao meu objeto , para mim usar um init novo e 
tbm usar o init com os valores ca minha outra class eu passo a seguinte 
informção :

super().__init__(v=10,i=5) v and i sao atributos aleatorios que eu coloquei

ex: class Heranca(Computador):
    def __init__(self):
        super().__init__(marca,memoria="8gn")"""




#=================================================================================================

class Privada:
    """essa class recebe argumentos privados"""
    def __init__(self,nome,sobrenome):
        self.__firstName = nome
        self.__lastName = sobrenome
    def nomeCompleto(self):
        return f"{str(self.__firstName).title()} {str(self.__lastName).title()}"


"""mostra argumentos privados"""
nome = Privada("guilherme","felipe")
print(nome._Privada__firstName)
print(nome._Privada__lastName)

#print(nome.__lastName) <= nao funciona pq eu nao chamei o nome  da class

"""adiciona valores detro do argumento privados"""
nome._Privada__lastName = "felipe pereira"
print(nome.nomeCompleto())


#===================================================================================================

class Pessoa:
    """usando o get e o set  nas class"""
    def __init__(self,nome,idade):
        self.__nome = nome
        self.__idade = idade
    
    def get_nome(self):
        """get ele sempre retorna algo"""
        return print(self.__nome)
    def get_idade(self):
        return print(self.__idade)

    def set_idade(self,idade):
        """set ele nunca retorna nada ele altera os valores de uma variavel"""
        self.__idade = idade


p = Pessoa("guilherme",12)

p.get_idade() # puxo idade

p.set_idade(18) # atribuiu uma idade

p.get_idade() # mostro novamente a nova idade


#===================================================================================================



# setando propriedades nas class

class Client:
    def __init__(self,nome):
        self.__nome = nome

    @property 
    #@property significa que é uma propriedade da class  ou seja eu posso chama sem passa como se fosse uma funcao , lembrando que a class
    #é obrigada a ser privada se nao o programa falara que o atributo nao pode ser alterado.
    def nome(self):
        return print(self.__nome.title())


cliente = Client("guilherme felipe")
cliente.nome  # chamando a funcao sem passa os parametro de aspas