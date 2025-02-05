# Python Cheat Sheet

## Grundlagen
```python
# Variablen: Speicherung von Werten
x = 10        # Integer (Ganzzahl)
pi = 3.14     # Float (Gleitkommazahl)
name = "Max"  # String (Text)
ist_aktiv = True  # Boolean (Wahrheitswert)

# Datentypen prüfen
print(type(x))  # Ausgabe: <class 'int'>
```

## Operatoren
```python
# Arithmetische Operatoren
5 + 3   # Addition
5 - 3   # Subtraktion
5 * 3   # Multiplikation
5 / 3   # Division
5 // 3  # Ganzzahldivision (Ergebnis ohne Nachkommastellen)
5 % 3   # Modulo (Rest der Division)
5 ** 3  # Potenzierung (5 hoch 3)

# Vergleichsoperatoren (geben einen booleschen Wert zurück)
x == y  # Gleich
x != y  # Ungleich
x > y   # Größer als
x < y   # Kleiner als
x >= y  # Größer oder gleich
x <= y  # Kleiner oder gleich

# Logische Operatoren
True and False  # UND: Beide müssen True sein
True or False   # ODER: Mindestens einer muss True sein
not True        # NICHT: Negation
```

## Kontrollstrukturen
```python
# If-Else Bedingung
x = 10
if x > 5:
    print("Größer als 5")
elif x == 5:
    print("Gleich 5")
else:
    print("Kleiner als 5")

# Schleifen
# For-Schleife mit range (erzeugt Zahlen von 0 bis 4)
for i in range(5):
    print(i)

# While-Schleife (läuft solange Bedingung True ist)
while x > 0:
    print(x)
    x -= 1  # x um 1 verringern
```

## Listen & Dictionaries
```python
# Listen (Sammlung von Elementen)
zahlen = [1, 2, 3, 4, 5]
print(zahlen[0])    # Erstes Element
zahlen.append(6)    # Element hinzufügen
zahlen.remove(3)    # Element entfernen

# Dictionary (Schlüssel-Wert-Paare)
person = {"name": "Max", "alter": 25}
print(person["name"])  # Zugriff auf Wert
person["stadt"] = "Berlin"  # Neuer Schlüssel-Wert
```

## Funktionen
```python
# Definieren einer Funktion
def begruessung(name):
    return f"Hallo, {name}!"

print(begruessung("Max"))
```

## Klassen & Objekte
```python
# Objektorientierte Programmierung (OOP)
class Auto:
    def __init__(self, marke="VW", modell):  # Konstruktor
        self.marke = marke
        self.modell = modell
    
    def details(self):
        return f"{self.marke} {self.modell}"

mein_auto = Auto("BMW", "X5")
print(mein_auto.details())
```

## Dateioperationen
```python
# Datei schreiben
with open("test.txt", "w") as file:
    file.write("Hallo Welt!")

# Datei lesen
with open("test.txt", "r") as file:
    print(file.read())
```

## Fehlerbehandlung
```python
# Fehler abfangen mit try-except-finally
try:
    x = 1 / 0  # Fehler: Division durch Null
    raise ValueError("Ungültiger Wert eingegeben!")
except ZeroDivisionError:
    print("Division durch Null!")
finally:
    print("Fertig!")
```


## Lambda-Funktionen
```python
# Anonyme (kurze) Funktion
def quadrat(x): return x**2

# Oder als Lambda-Funktion
quadrat = lambda x: x**2
print(quadrat(4))
```

## Dekoratoren
```python
# Funktionen als Argumente einer anderen Funktion
def dekorator(funktion):
    def wrapper():
        print("Vor der Funktion")
        funktion()
        print("Nach der Funktion")
    return wrapper

@dekorator  # Anwendung des Dekorators auf die Funktion hallo()
def hallo():
    print("Hallo Welt!")

hallo()
```

## Threading
```python
# Mehrere Prozesse gleichzeitig ausführen
import threading

def print_zahlen():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_zahlen)
thread.start()
thread.join()  # Warten, bis Thread beendet ist
```

## Iteratoren und Generatoren
```python
# Einfache Iteratoren
zahlen = iter([1, 2, 3])
print(next(zahlen))  # 1
print(next(zahlen))  # 2

# Generator-Funktion (liefert Werte nach Bedarf)
def mein_generator():
    for i in range(3):
        yield i  # speichert Zustand und gibt Wert zurück

for zahl in mein_generator():
    print(zahl)
```

## Reguläre Ausdrücke
```python
import re

# Suche nach Mustern in Strings
text = "Meine Nummer ist 123-4567"
muster = r"\d{3}-\d{4}"

# Überprüfung, ob Muster im Text ist
if re.search(muster, text):
    print("Muster gefunden!")

# Alle Treffer finden
print(re.findall(muster, text))
```

## Tupel durchgehen
```python
x = (1, "Hallo", 3.14, True)

typen = tuple(type(element) for element in x)
print(typen)
```

## Enums (Aufzählungstypen)
```python
from enum import Enum

# Ein Enum ist eine spezielle Klasse zur Definition von konstanten Werten
class Farbe(Enum):
    ROT = 1
    GRUEN = 2
    BLAU = 3

print(Farbe.ROT)  # Ausgabe: Farbe.ROT
print(Farbe.ROT.value)  # Ausgabe: 1
``` 

## Vererbung
```python
# Eine Klasse kann Eigenschaften und Methoden einer anderen Klasse erben
class Fahrzeug:
    def __init__(self, marke):
        self.marke = marke
    
    def info(self):
        return f"Fahrzeug von {self.marke}"

# Auto erbt von Fahrzeug
class Auto(Fahrzeug):
    def __init__(self, marke, modell):
        super().__init__(marke)  # Super ruft den Konstruktor der Elternklasse auf
        self.modell = modell
    
    def info(self):
        return f"Auto: {self.marke} {self.modell}"

mein_auto = Auto("BMW", "X5")
print(mein_auto.info())
```

## Abstrakte Klassen
```python
from abc import ABC, abstractmethod

# Eine abstrakte Klasse kann nicht direkt instanziiert werden
class Tier(ABC):
    @abstractmethod
    def geraeusch(self):
        pass  # Muss in Unterklassen implementiert werden

class Hund(Tier):
    def geraeusch(self):
        return "Wuff!"

mein_hund = Hund()
print(mein_hund.geraeusch())  # Ausgabe: Wuff!
```

## Metaklassen
```python
# Eine Metaklasse ist eine Klasse, die Klassen erzeugt
class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['neue_methode'] = lambda self: "Hallo von Metaklasse!"
        return super().__new__(cls, name, bases, dct)

class MeineKlasse(metaclass=Meta):
    pass

obj = MeineKlasse()
print(obj.neue_methode())  # Ausgabe: Hallo von Metaklasse!
```

## Property-Decorator
```python
# Ermöglicht das sichere Setzen und Holen von Werten mit Validierung
class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, wert):
        if len(wert) > 2:
            self._name = wert
        else:
            raise ValueError("Name zu kurz!")

p = Person("Max")
p.name = "Tom"
print(p.name)
```

## Kontextmanager
```python
# Kontextmanager erlauben das sichere Öffnen/Schließen von Ressourcen
class MeinKontext:
    def __enter__(self):
        print("Betrete Kontext")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Verlasse Kontext")

with MeinKontext():
    print("Innerhalb des Kontextes")
```

## Mehrfachvererbung
```python
# Eine Klasse kann von mehreren Klassen erben
class A:
    def methode_a(self):
        return "Methode von A"

class B:
    def methode_b(self):
        return "Methode von B"

class C(A, B):
    pass

obj = C()
print(obj.methode_a())  # Von A geerbt
print(obj.methode_b())  # Von B geerbt
```

## Dekoratoren mit Parametern
```python
# Ein Dekorator kann Parameter annehmen

def wiederhole(n):
    def dekorator(funktion):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                funktion(*args, **kwargs)
        return wrapper
    return dekorator

@wiederhole(3)
def hallo():
    print("Hallo Welt!")

hallo()
```

## Fortgeschrittene Generatoren
```python
# Ein Generator erzeugt Werte bei Bedarf

def zahlen_generator():
    n = 0
    while True:
        yield n  # Speichert den Zustand
        n += 1

zahlen = zahlen_generator()
print(next(zahlen))  # 0
print(next(zahlen))  # 1
```

## Funktions-Dekoratoren mit functools
```python
# functools lru_cache speichert vorherige Ergebnisse für schnelleren Zugriff
from functools import lru_cache

@lru_cache(maxsize=5)
def fakultaet(n):
    if n == 0:
        return 1
    return n * fakultaet(n - 1)

print(fakultaet(5))
```

## Async & Await
```python
# Async/Await ermöglicht asynchrone Programmierung
import asyncio

async def begruessung():
    await asyncio.sleep(1)  # Simuliert eine Verzögerung
    print("Hallo Async!")

asyncio.run(begruessung())
```
