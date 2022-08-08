#KG220802 Demo for OOPS Inheritance using Shape 

from abc import abstractmethod


class Shape():
    def __init__(self,ps_n='Shape', pn_a=0, pn_p=0):
        self.s_name = ps_n
        self.n_area = pn_a
        self.n_perimeter = pn_p

    @abstractmethod
    def calc():
        pass

    def getdata():
        pass

    def show():
        pass
