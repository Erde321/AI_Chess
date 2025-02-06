from enum import Enum
        

# Diese Klasse dient als Enumeration der Positionen einer Schachfigur in der y-Achse auch Rang genannt (Zahlen 1 bis 8)
class e_zeile(Enum):
    r_1 = 0
    r_2 = 1
    r_3 = 2
    r_4 = 3
    r_5 = 4
    r_6 = 5
    r_7 = 6
    r_8 = 7

class e_spalte_value(Enum):
    a = 0 
    b = 1
    c = 2
    d = 3
    e = 4
    f = 5
    g = 6
    h = 7

# Diese Klasse dient als Enumeration der Positionen einer Schachfigur in der x-Achse auch Linie genannt (Zahlen A bis H)
class e_spalte(Enum):
    l_a = e_spalte_value.a
    l_b = e_spalte_value.b
    l_c = e_spalte_value.c
    l_d = e_spalte_value.d
    l_e = e_spalte_value.e
    l_f = e_spalte_value.f
    l_g = e_spalte_value.g
    l_h = e_spalte_value.h

class c_position():

    spalte = None
    zeile = None

    def __init__(self, spalte: e_spalte, zeile: e_zeile):
        
        self.zeile = zeile
        self.spalte = spalte