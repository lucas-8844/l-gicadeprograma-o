class Diciplina:
    def __init__(self, __nome):
        self.__nome = __nome
        
    def get_nome(self):
     return self.__nome  # getter
    def set_nome(self, nome):
        self.__nome = nome  # setter