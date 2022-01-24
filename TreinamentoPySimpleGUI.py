#pip install PySimpleGUI
import PySimpleGUI as ps 

#ps.Text == label
#size == tamanho dos objetos
#key == chave que cada elemento vai receber
class TelaPy:
    def __init__(self):
        #tema
        ps.change_look_and_feel("DarkBrown")

        #layout
        Meu_layout = [
        [ps.Text("Nome:",size=(5,0)),ps.Input(size=(15,0),key="nome")],
        [ps.Text("Idade:",size=(5,0)),ps.Input(size=(15,0),key="idade")],

        [ps.Text("Formas de envio:")],
        [ps.Checkbox("Gmail",key="Gmail"),ps.Checkbox("Facebook",key="Facebook"),ps.Checkbox("GitHub",key="GitHub")],

        [ps.Text("Cartões")],
        [ps.Radio("Sim","Cartão",key="SimCartao"),ps.Radio("Nao","Cartão",key="NaoCartao")],

        [ps.Slider(range=(0,413000),default_value = 0,orientation="h",key="velocidade",size=(15,20))],
         # slice mostra uma barra de velocidade infos(range == de tantos a tantos )
         # defalt_value == inicio 
         # orientacao 
         # chave do dicionario
         # size tamanho da barra #


        [ps.Button("Salvar")],

        [ps.Output(size=(50,30))], # cria campo de retorno pro usuario ver na aplicação
        
        ]
    
        #tela == criar janela
        self.janela = ps.Window("Agenda").layout(Meu_layout)
       
    
    def iniciar(self):
        """ Propriedade que esta iniciando e recebendo minhas informações... """
        while True:

            #Extrair dados da tela
            self.button, self.values = self.janela.Read()

            nome = self.values["nome"]
            idade = self.values["idade"]
            aceitaGmail = self.values["Gmail"]
            aceitaFace = self.values["Facebook"]
            aceitaGit = self.values["GitHub"]

            print(f"nome = {nome}")
            print(f"idade = {idade}")
            print(f"aceitaGmail = {aceitaGmail}")
            print(f"aceitaFace = {aceitaFace}")
            print(f"aceitaGit = {aceitaGit}")

    def MeuInit(self):
        while True:
            #Extrair dados da tela
            self.button, self.values = self.janela.Read()
            print(self.values)


tela = TelaPy()

tela.MeuInit()
