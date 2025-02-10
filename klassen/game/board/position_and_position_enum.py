from enum import Enum
        
class e_zeile(Enum):
    notdef = "x"
    r_1 = 0
    r_2 = 1
    r_3 = 2
    r_4 = 3
    r_5 = 4
    r_6 = 5
    r_7 = 6
    r_8 = 7

    def __add__(self, other: int):
            
        zahl = other % 8

        match self:
            case e_zeile.r_1:
                match zahl:
                    case 0:
                        new_value = e_zeile.r_1
                    case 1:
                        new_value = e_zeile.r_2
                    case 2:
                        new_value = e_zeile.r_3
                    case 3:
                        new_value = e_zeile.r_4
                    case 4:
                        new_value = e_zeile.r_5
                    case 5:
                        new_value = e_zeile.r_6
                    case 6:
                        new_value = e_zeile.r_7
                    case 7:
                        new_value = e_zeile.r_8
                    case _:
                        return NotImplemented
                      
            case e_zeile.r_2:
                match zahl:
                    case 0:
                        new_value = e_zeile.r_2
                    case 1:
                        new_value = e_zeile.r_3
                    case 2:
                        new_value = e_zeile.r_4
                    case 3:
                        new_value = e_zeile.r_5
                    case 4:
                        new_value = e_zeile.r_6
                    case 5:
                        new_value = e_zeile.r_7
                    case 6:
                        new_value = e_zeile.r_8
                    case 7:
                        new_value = e_zeile.r_1
                    case _:
                        return NotImplemented

            case e_zeile.r_3:
                match zahl:
                    case 0:
                        new_value = e_zeile.r_3
                    case 1:
                        new_value = e_zeile.r_4
                    case 2:
                        new_value = e_zeile.r_5
                    case 3:
                        new_value = e_zeile.r_6
                    case 4:
                        new_value = e_zeile.r_7
                    case 5:
                        new_value = e_zeile.r_8
                    case 6:
                        new_value = e_zeile.r_1
                    case 7:
                        new_value = e_zeile.r_2
                    case _:
                        return NotImplemented

            case e_zeile.r_4:
                match zahl:
                    case 0:
                        new_value = e_zeile.r_4
                    case 1:
                        new_value = e_zeile.r_5
                    case 2:
                        new_value = e_zeile.r_6
                    case 3:
                        new_value = e_zeile.r_7
                    case 4:
                        new_value = e_zeile.r_8
                    case 5:
                        new_value = e_zeile.r_1
                    case 6:
                        new_value = e_zeile.r_2
                    case 7:
                        new_value = e_zeile.r_3
                    case _:
                        return NotImplemented

            case e_zeile.r_5: 
                match zahl:
                    case 0:
                        new_value = e_zeile.r_5
                    case 1:
                        new_value = e_zeile.r_6
                    case 2:
                        new_value = e_zeile.r_7
                    case 3:
                        new_value = e_zeile.r_8
                    case 4:
                        new_value = e_zeile.r_1
                    case 5:
                        new_value = e_zeile.r_2
                    case 6:
                        new_value = e_zeile.r_3
                    case 7:
                        new_value = e_zeile.r_4
                    case _:
                        return NotImplemented

            case e_zeile.r_6:
                match zahl:
                    case 0:
                        new_value = e_zeile.r_6
                    case 1:
                        new_value = e_zeile.r_7
                    case 2:
                        new_value = e_zeile.r_8
                    case 3:
                        new_value = e_zeile.r_1
                    case 4:
                        new_value = e_zeile.r_2
                    case 5:
                        new_value = e_zeile.r_3
                    case 6:
                        new_value = e_zeile.r_4
                    case 7:
                        new_value = e_zeile.r_5
                    case _:
                        return NotImplemented

            case e_zeile.r_7:
                match zahl:
                    case 0:
                        new_value = e_zeile.r_7
                    case 1:
                        new_value = e_zeile.r_8
                    case 2:
                        new_value = e_zeile.r_1
                    case 3:
                        new_value = e_zeile.r_2
                    case 4:
                        new_value = e_zeile.r_3
                    case 5:
                        new_value = e_zeile.r_4
                    case 6:
                        new_value = e_zeile.r_5
                    case 7:
                        new_value = e_zeile.r_6
                    case _:
                        return NotImplemented

            case e_zeile.r_8:
                match zahl:
                    case 0:
                        new_value = e_zeile.r_8
                    case 1:
                        new_value = e_zeile.r_1
                    case 2:
                        new_value = e_zeile.r_2
                    case 3:
                        new_value = e_zeile.r_3
                    case 4:
                        new_value = e_zeile.r_4
                    case 5:
                        new_value = e_zeile.r_5
                    case 6:
                        new_value = e_zeile.r_6
                    case 7:
                        new_value = e_zeile.r_7
                    case _:
                        return NotImplemented

            case _:
                return NotImplemented
                
        try:
            return e_spalte(new_value) 
        except ValueError:
            raise ValueError(f"Kein passendes Enum-Mitglied für Wert {new_value}")

    def __sub__(self, other:int):
        zahl = other % 8

        match self:
            case e_zeile.r_1:
                match zahl:
                    case 0:
                        new_value = e_zeile.r_1
                    case 7:
                        new_value = e_zeile.r_2
                    case 6:
                        new_value = e_zeile.r_3
                    case 5:
                        new_value = e_zeile.r_4
                    case 4:
                        new_value = e_zeile.r_5
                    case 3:
                        new_value = e_zeile.r_6
                    case 2:
                        new_value = e_zeile.r_7
                    case 1:
                        new_value = e_zeile.r_8
                    case _:
                        return NotImplemented
                      
            case e_zeile.r_2:
                match zahl:
                    case 0:
                        new_value = e_zeile.r_2
                    case 7:
                        new_value = e_zeile.r_3
                    case 6:
                        new_value = e_zeile.r_4
                    case 5:
                        new_value = e_zeile.r_5
                    case 4:
                        new_value = e_zeile.r_6
                    case 3:
                        new_value = e_zeile.r_7
                    case 2:
                        new_value = e_zeile.r_8
                    case 1:
                        new_value = e_zeile.r_1
                    case _:
                        return NotImplemented

            case e_zeile.r_3:
                match zahl:
                    case 0:
                        new_value = e_zeile.r_3
                    case 7:
                        new_value = e_zeile.r_4
                    case 6:
                        new_value = e_zeile.r_5
                    case 5:
                        new_value = e_zeile.r_6
                    case 4:
                        new_value = e_zeile.r_7
                    case 3:
                        new_value = e_zeile.r_8
                    case 2:
                        new_value = e_zeile.r_1
                    case 1:
                        new_value = e_zeile.r_2
                    case _:
                        return NotImplemented

            case e_zeile.r_4:
                match zahl:
                    case 0:
                        new_value = e_zeile.r_4
                    case 7:
                        new_value = e_zeile.r_5
                    case 6:
                        new_value = e_zeile.r_6
                    case 5:
                        new_value = e_zeile.r_7
                    case 4:
                        new_value = e_zeile.r_8
                    case 3:
                        new_value = e_zeile.r_1
                    case 2:
                        new_value = e_zeile.r_2
                    case 1:
                        new_value = e_zeile.r_3
                    case _:
                        return NotImplemented

            case e_zeile.r_5: 
                match zahl:
                    case 0:
                        new_value = e_zeile.r_5
                    case 7:
                        new_value = e_zeile.r_6
                    case 7:
                        new_value = e_zeile.r_7
                    case 5:
                        new_value = e_zeile.r_8
                    case 4:
                        new_value = e_zeile.r_1
                    case 3:
                        new_value = e_zeile.r_2
                    case 2:
                        new_value = e_zeile.r_3
                    case 1:
                        new_value = e_zeile.r_4
                    case _:
                        return NotImplemented

            case e_zeile.r_6:
                match zahl:
                    case 0:
                        new_value = e_zeile.r_6
                    case 7:
                        new_value = e_zeile.r_7
                    case 6:
                        new_value = e_zeile.r_8
                    case 5:
                        new_value = e_zeile.r_1
                    case 4:
                        new_value = e_zeile.r_2
                    case 3:
                        new_value = e_zeile.r_3
                    case 2:
                        new_value = e_zeile.r_4
                    case 1:
                        new_value = e_zeile.r_5
                    case _:
                        return NotImplemented

            case e_zeile.r_7:
                match zahl:
                    case 0:
                        new_value = e_zeile.r_7
                    case 7:
                        new_value = e_zeile.r_8
                    case 6:
                        new_value = e_zeile.r_1
                    case 5:
                        new_value = e_zeile.r_2
                    case 4:
                        new_value = e_zeile.r_3
                    case 3:
                        new_value = e_zeile.r_4
                    case 2:
                        new_value = e_zeile.r_5
                    case 1:
                        new_value = e_zeile.r_6
                    case _:
                        return NotImplemented

            case e_zeile.r_8:
                match zahl:
                    case 0:
                        new_value = e_zeile.r_8
                    case 7:
                        new_value = e_zeile.r_1
                    case 6:
                        new_value = e_zeile.r_2
                    case 5:
                        new_value = e_zeile.r_3
                    case 4:
                        new_value = e_zeile.r_4
                    case 3:
                        new_value = e_zeile.r_5
                    case 2:
                        new_value = e_zeile.r_6
                    case 1:
                        new_value = e_zeile.r_7
                    case _:
                        return NotImplemented

            case _:
                return NotImplemented
                
        try:
            return e_spalte(new_value) 
        except ValueError:
            raise ValueError(f"Kein passendes Enum-Mitglied für Wert {new_value}")


class e_spalte_value(Enum):
    a = 7
    b = 6
    c = 5
    d = 4
    e = 3
    f = 2
    g = 1
    h = 0

# Diese Klasse dient als Enumeration der Positionen einer Schachfigur in der x-Achse auch Linie genannt (Zahlen A bis H)
class e_spalte(Enum):
    notdef = "x"
    l_a = e_spalte_value.a
    l_b = e_spalte_value.b
    l_c = e_spalte_value.c
    l_d = e_spalte_value.d
    l_e = e_spalte_value.e
    l_f = e_spalte_value.f
    l_g = e_spalte_value.g
    l_h = e_spalte_value.h

    def __add__(self, other: int):
            
        zahl = other % 8

        match self:
            case e_spalte.l_a:
                match zahl:
                    case 0:
                        new_value = e_spalte.l_a
                    case 1:
                        new_value = e_spalte.l_b
                    case 2:
                        new_value = e_spalte.l_c
                    case 3:
                        new_value = e_spalte.l_d
                    case 4:
                        new_value = e_spalte.l_e
                    case 5:
                        new_value = e_spalte.l_f
                    case 6:
                        new_value = e_spalte.l_g
                    case 7:
                        new_value = e_spalte.l_h
                    case _:
                        return NotImplemented
                      
            case e_spalte.l_b:
                match zahl:
                    case 0:
                        new_value = e_spalte.l_b
                    case 1:
                        new_value = e_spalte.l_c
                    case 2:
                        new_value = e_spalte.l_d
                    case 3:
                        new_value = e_spalte.l_e
                    case 4:
                        new_value = e_spalte.l_f
                    case 5:
                        new_value = e_spalte.l_g
                    case 6:
                        new_value = e_spalte.l_h
                    case 7:
                        new_value = e_spalte.l_a
                    case _:
                        return NotImplemented

            case e_spalte.l_c:
                match zahl:
                    case 0:
                        new_value = e_spalte.l_c
                    case 1:
                        new_value = e_spalte.l_d
                    case 2:
                        new_value = e_spalte.l_e
                    case 3:
                        new_value = e_spalte.l_f
                    case 4:
                        new_value = e_spalte.l_g
                    case 5:
                        new_value = e_spalte.l_h
                    case 6:
                        new_value = e_spalte.l_a
                    case 7:
                        new_value = e_spalte.l_b
                    case _:
                        return NotImplemented

            case e_spalte.l_d:
                match zahl:
                    case 0:
                        new_value = e_spalte.l_d
                    case 1:
                        new_value = e_spalte.l_e
                    case 2:
                        new_value = e_spalte.l_f
                    case 3:
                        new_value = e_spalte.l_g
                    case 4:
                        new_value = e_spalte.l_h
                    case 5:
                        new_value = e_spalte.l_a
                    case 6:
                        new_value = e_spalte.l_b
                    case 7:
                        new_value = e_spalte.l_c
                    case _:
                        return NotImplemented

            case e_spalte.l_e: 
                match zahl:
                    case 0:
                        new_value = e_spalte.l_e
                    case 1:
                        new_value = e_spalte.l_f
                    case 2:
                        new_value = e_spalte.l_g
                    case 3:
                        new_value = e_spalte.l_h
                    case 4:
                        new_value = e_spalte.l_a
                    case 5:
                        new_value = e_spalte.l_b
                    case 6:
                        new_value = e_spalte.l_c
                    case 7:
                        new_value = e_spalte.l_d
                    case _:
                        return NotImplemented

            case e_spalte.l_f:
                match zahl:
                    case 0:
                        new_value = e_spalte.l_f
                    case 1:
                        new_value = e_spalte.l_g
                    case 2:
                        new_value = e_spalte.l_h
                    case 3:
                        new_value = e_spalte.l_a
                    case 4:
                        new_value = e_spalte.l_b
                    case 5:
                        new_value = e_spalte.l_c
                    case 6:
                        new_value = e_spalte.l_d
                    case 7:
                        new_value = e_spalte.l_e
                    case _:
                        return NotImplemented

            case e_spalte.l_g:
                match zahl:
                    case 0:
                        new_value = e_spalte.l_g
                    case 1:
                        new_value = e_spalte.l_h
                    case 2:
                        new_value = e_spalte.l_a
                    case 3:
                        new_value = e_spalte.l_b
                    case 4:
                        new_value = e_spalte.l_c
                    case 5:
                        new_value = e_spalte.l_d
                    case 6:
                        new_value = e_spalte.l_e
                    case 7:
                        new_value = e_spalte.l_f
                    case _:
                        return NotImplemented

            case e_spalte.l_h:
                match zahl:
                    case 0:
                        new_value = e_spalte.l_h
                    case 1:
                        new_value = e_spalte.l_a
                    case 2:
                        new_value = e_spalte.l_b
                    case 3:
                        new_value = e_spalte.l_c
                    case 4:
                        new_value = e_spalte.l_d
                    case 5:
                        new_value = e_spalte.l_e
                    case 6:
                        new_value = e_spalte.l_f
                    case 7:
                        new_value = e_spalte.l_g
                    case _:
                        return NotImplemented

            case _:
                return NotImplemented
                
        try:
            return e_spalte(new_value) 
        except ValueError:
            raise ValueError(f"Kein passendes Enum-Mitglied für Wert {new_value}")

    def __sub__(self, other: int):
        zahl = other % 8

        match self:
            case e_spalte.l_a:
                match zahl:
                    case 0:
                        new_value = e_spalte.l_a
                    case 7:
                        new_value = e_spalte.l_b
                    case 6:
                        new_value = e_spalte.l_c
                    case 5:
                        new_value = e_spalte.l_d
                    case 4:
                        new_value = e_spalte.l_e
                    case 3:
                        new_value = e_spalte.l_f
                    case 2:
                        new_value = e_spalte.l_g
                    case 1:
                        new_value = e_spalte.l_h
                    case _:
                        return NotImplemented
                      
            case e_spalte.l_b:
                match zahl:
                    case 0:
                        new_value = e_spalte.l_b
                    case 7:
                        new_value = e_spalte.l_c
                    case 6:
                        new_value = e_spalte.l_d
                    case 5:
                        new_value = e_spalte.l_e
                    case 4:
                        new_value = e_spalte.l_f
                    case 3:
                        new_value = e_spalte.l_g
                    case 2:
                        new_value = e_spalte.l_h
                    case 1:
                        new_value = e_spalte.l_a
                    case _:
                        return NotImplemented

            case e_spalte.l_c:
                match zahl:
                    case 0:
                        new_value = e_spalte.l_c
                    case 7:
                        new_value = e_spalte.l_d
                    case 6:
                        new_value = e_spalte.l_e
                    case 5:
                        new_value = e_spalte.l_f
                    case 4:
                        new_value = e_spalte.l_g
                    case 3:
                        new_value = e_spalte.l_h
                    case 2:
                        new_value = e_spalte.l_a
                    case 1:
                        new_value = e_spalte.l_b
                    case _:
                        return NotImplemented

            case e_spalte.l_d:
                match zahl:
                    case 0:
                        new_value = e_spalte.l_d
                    case 7:
                        new_value = e_spalte.l_e
                    case 6:
                        new_value = e_spalte.l_f
                    case 5:
                        new_value = e_spalte.l_g
                    case 4:
                        new_value = e_spalte.l_h
                    case 3:
                        new_value = e_spalte.l_a
                    case 2:
                        new_value = e_spalte.l_b
                    case 1:
                        new_value = e_spalte.l_c
                    case _:
                        return NotImplemented

            case e_spalte.l_e: 
                match zahl:
                    case 0:
                        new_value = e_spalte.l_e
                    case 7:
                        new_value = e_spalte.l_f
                    case 6:
                        new_value = e_spalte.l_g
                    case 5:
                        new_value = e_spalte.l_h
                    case 4:
                        new_value = e_spalte.l_a
                    case 3:
                        new_value = e_spalte.l_b
                    case 2:
                        new_value = e_spalte.l_c
                    case 1:
                        new_value = e_spalte.l_d
                    case _:
                        return NotImplemented

            case e_spalte.l_f:
                match zahl:
                    case 0:
                        new_value = e_spalte.l_f
                    case 7:
                        new_value = e_spalte.l_g
                    case 6:
                        new_value = e_spalte.l_h
                    case 5:
                        new_value = e_spalte.l_a
                    case 4:
                        new_value = e_spalte.l_b
                    case 3:
                        new_value = e_spalte.l_c
                    case 2:
                        new_value = e_spalte.l_d
                    case 1:
                        new_value = e_spalte.l_e
                    case _:
                        return NotImplemented

            case e_spalte.l_g:
                match zahl:
                    case 0:
                        new_value = e_spalte.l_g
                    case 7:
                        new_value = e_spalte.l_h
                    case 6:
                        new_value = e_spalte.l_a
                    case 5:
                        new_value = e_spalte.l_b
                    case 4:
                        new_value = e_spalte.l_c
                    case 3:
                        new_value = e_spalte.l_d
                    case 2:
                        new_value = e_spalte.l_e
                    case 1:
                        new_value = e_spalte.l_f
                    case _:
                        return NotImplemented

            case e_spalte.l_h:
                match zahl:
                    case 0:
                        new_value = e_spalte.l_h
                    case 7:
                        new_value = e_spalte.l_a
                    case 6:
                        new_value = e_spalte.l_b
                    case 5:
                        new_value = e_spalte.l_c
                    case 4:
                        new_value = e_spalte.l_d
                    case 3:
                        new_value = e_spalte.l_e
                    case 2:
                        new_value = e_spalte.l_f
                    case 1:
                        new_value = e_spalte.l_g
                    case _:
                        return NotImplemented

            case _:
                return NotImplemented
                
        try:
            return e_spalte(new_value) 
        except ValueError:
            raise ValueError(f"Kein passendes Enum-Mitglied für Wert {new_value}")

class c_position():

    def __init__(self, spalte: e_spalte, zeile: e_zeile):
        
        self._zeile = zeile
        self._spalte = spalte