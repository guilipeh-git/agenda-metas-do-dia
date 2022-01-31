# pip install pysimplegui
# janela.extend layout(janela['container'],[[sg.Checkbox(''),sg.Input('')]])  <= atualiza janela
import PySimpleGUI as sg 

class Agenda_Gui:
    
    def __init__(self):
        pass

    def __criar_tela_inicial(self):
        """Cria layout"""
        sg.theme("DarkBlue4")
        self.layout = [[sg.Checkbox("",key="check"),sg.Input("",key="tarefa")]]

        MeuLayout = [
            [sg.Frame("Bloco de notas",layout=self.layout,key="container")],
            [sg.Button("Salvar"),sg.Button("Nova Tarefa"),sg.Button("Reset")],
            ]
        return sg.Window("Agenda_Gui",layout=MeuLayout,finalize=True) # <= criando a janela

    def __criar_janela(self):
        """criando janela"""
        janela = self.__criar_tela_inicial()
        #lendo eventos da janela
        while True:
            event,values = janela.read()
            if(event == sg.WIN_CLOSED):
                break
            elif(str(event).lower() == "nova tarefa"):  
                janela.extend_layout(janela["container"],[[sg.Checkbox("",key="check"),sg.Input("",key="tarefa")]]) # <=  essa linha insere + linhas no frame
            elif(str(event).lower() == "reset"):
                janela.close() 
                self.__criar_janela()
            elif(event == "Salvar"):
                print(values)
    @property
    def start(self):
        return self.__criar_janela()


p = Agenda_Gui()

p.start