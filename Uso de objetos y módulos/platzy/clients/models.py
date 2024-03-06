import uuid

class Client:
    def __init__(self,name,company,email,position, uid=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4()

    def to_dict(self):
        #"checka lo que regresa el metodo dict, y nos permite acceder a un diccionari"
        return vars(self)
    
    @staticmethod
    #metodo estatico que se puede ejectuar sin estancia de clase
    def schema (): #no recibe self porquee no necesita instancia
        return ['name', 'company', 'email', 'position', 'uid']

