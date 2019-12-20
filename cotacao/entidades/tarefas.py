class Tarefas():
    def __init__(self, checkin, checkout, num_adultos, num_crianças, user, pousadas,):
        self.__checkin = checkin
        self.__checkout = checkout
        self.__num_adultos = num_adultos
        self.__num_crianças = num_crianças
        self.__user = user
        self.__pousadas = pousadas


    @property
    def checkout(self,):
        return self.__checkout

    @checkout.setter
    def checkout(self, checkout):
        self.__checkout

    @property
    def checkin(self,):
        return self.__checkin

    @checkin.setter
    def checkin(self, checkin):
        self.__checkin

    @property
    def num_adultos(self,):
        return self.__num_adultos

    @num_adultos.setter
    def num_adultos(self, num_adultos):
        self.__num_adultos

    @property
    def num_crianças(self,):
        return self.__num_crianças

    @num_crianças.setter
    def num_crianças(self, num_crianças):
        self.__num_crianças

    @property
    def user(self,):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user

    @property
    def pousadas(self,):
        return self.__pousadas

    @pousadas.setter
    def pousadas(self, pousadas):
        self.__pousadas
        

class Tarefas_Update():
    def __init__(self, checkin, checkout, num_adultos, num_crianças, user, pousadas, id):
        self.__checkin = checkin
        self.__checkout = checkout
        self.__num_adultos = num_adultos
        self.__num_crianças = num_crianças
        self.__user = user
        self.__pousadas = pousadas
        self.__id = id


    @property
    def checkout(self,):
        return self.__checkout

    @checkout.setter
    def checkout(self, checkout):
        self.__checkout

    @property
    def checkin(self,):
        return self.__checkin

    @checkin.setter
    def checkin(self, checkin):
        self.__checkin

    @property
    def num_adultos(self,):
        return self.__num_adultos

    @num_adultos.setter
    def num_adultos(self, num_adultos):
        self.__num_adultos

    @property
    def num_crianças(self,):
        return self.__num_crianças

    @num_crianças.setter
    def num_crianças(self, num_crianças):
        self.__num_crianças

    @property
    def user(self,):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user

    @property
    def pousadas(self,):
        return self.__pousadas

    @pousadas.setter
    def pousadas(self, pousadas):
        self.__pousadas
        
        
    @property
    def id(self,):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id