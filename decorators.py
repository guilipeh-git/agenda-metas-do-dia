#meus decorators
def textUpper(fun):
    def wrapper():
        return str(fun()).upper()
    return wrapper



    
@textUpper
def string():
    return "beatifull"


print(string())

