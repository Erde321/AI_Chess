from enum import Enum

class c_position():

    rang = None
    linie = None

    def __init__(self, linie, rang):
        if (not (isinstance(rang, e_rang)) or not(isinstance(linie, e_linie))):
            raise TypeError("Ungültige Position eingegeben")
        
        self.rang = rang
        self.linie = linie
        

# Diese Klasse dient als Enumeration der Positionen einer Schachfigur in der y-Achse auch Rang genannt (Zahlen 1 bis 8)
class e_rang(Enum):
    r_1 = 0
    r_2 = 1
    r_3 = 2
    r_4 = 3
    r_5 = 4
    r_6 = 5
    r_7 = 6
    r_8 = 7

class e_linie_value(Enum):
    A = 0 
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6
    H = 7

# Diese Klasse dient als Enumeration der Positionen einer Schachfigur in der x-Achse auch Linie genannt (Zahlen A bis H)
class e_linie(Enum):
    l_a = e_linie_value.A
    l_b = e_linie_value.B
    l_c = e_linie_value.C
    l_d = e_linie_value.D
    l_e = e_linie_value.E
    l_f = e_linie_value.F
    l_g = e_linie_value.G
    l_h = e_linie_value.H

