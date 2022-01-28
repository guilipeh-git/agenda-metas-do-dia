#meus decorators
def textUpperGUI(fun):
    def wrapper():
        return str(fun()).upper()
    return wrapper




@textUpperGUI
def string():
    return "funciona"


print(string())

