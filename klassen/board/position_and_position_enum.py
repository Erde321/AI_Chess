from enum import Enum

class c_position():

    rang = None
    linie = None

    def __init__(self, rang, linie):
        if (not (isinstance(rang, e_rang)) or not(isinstance(linie, e_linie))):
            raise TypeError("Ungültige Position eingegeben")
        
        self.rang = rang
        self.linie = linie
        

# Diese Klasse dient als Enumeration der Positionen einer Schachfigur in der x-Achse auch Rang genannt (Zahlen 1 bis 8)
class e_rang(Enum):
    r1 = 1
    r2 = 2
    r3 = 3
    r4 = 4
    r5 = 5
    r6 = 6
    r7 = 7
    r8 = 8

# Diese Klasse dient als Enumeration der Positionen einer Schachfigur in der y-Achse auch Linie genannt (Zahlen A bis H)
class e_linie(Enum):
    l_a = "A"
    l_b = "B"
    l_c = "C"
    l_d = "D"
    l_e = "E"
    l_f = "F"
    l_g = "G"
    l_h = "H"

    
    