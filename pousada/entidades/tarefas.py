class Tarefas():
    def __init__(self, author, name, tel, checkin, checkout, person_num, kidquestion, kid1, kid2, kid3, discount, dialy_of_price, portion):
        self.__author = author
        self.__name = name
        self.__tel = tel
        self.__checkin = checkin
        self.__checkout = checkout
        self.__person_num = person_num
        self.__kidquestion= kidquestion
        self.__kid1 = kid1
        self.__kid2 = kid2
        self.__kid3 = kid3
        self.__discount = discount
        self.__dialy_of_price = dialy_of_price
        self.__portion = portion


    @property
    def name(self,):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name

    @property
    def author(self,):
        return self.__author

    @author.setter
    def author(self, author):
        self.__author

    @property
    def tel(self,):
        return self.__tel

    @tel.setter
    def tel(self, tel):
        self.__tel

    @property
    def checkin(self,):
        return self.__checkin

    @checkin.setter
    def checkin(self, checkin):
        self.__checkin

    @property
    def checkout(self,):
        return self.__checkout

    @checkout.setter
    def checkout(self, checkout):
        self.__checkout

    @property
    def person_num(self,):
        return self.__person_num

    @person_num.setter
    def person_num(self, person_num):
        self.__person_num

    @property
    def kidquestion(self,):
        return self.__kidquestion

    @kidquestion.setter
    def kidquestion(self, kidquestion):
        self.__kidquestion

    @property
    def kid1(self,):
        return self.__kid1

    @kid1.setter
    def kid1(self, kid1):
        self.__kid1

    @property
    def kid2(self,):
        return self.__kid2

    @kid2.setter
    def kid2(self, kid2):
        self.__kid2

    @property
    def kid3(self,):
        return self.__kid3

    @kid3.setter
    def kid3(self, kid3):
        self.__kid3

    @property
    def discount(self,):
        return self.__discount

    @discount.setter
    def discount(self, discount):
        self.__discount

    @property
    def dialy_of_price(self,):
        return self.__dialy_of_price

    @dialy_of_price.setter
    def dialy_of_price(self, dialy_of_price):
        self.__dialy_of_price

    @property
    def portion(self,):
        return self.__portion

    @portion.setter
    def portion(self, portion):
        self.__portion