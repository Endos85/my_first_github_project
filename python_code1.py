
# code begrüßt den Benutzer und fragt nach seinem Namen und Alter
print()
print("Hallo benutzer!")
print("Willkommen zu meinem Python-Skript.")
print("Dieses Skript wird dich nach deinem Namen und Geburtsdatum fragen.")
print("Bitte gib deine Informationen ein, wenn du dazu aufgefordert wirst.")
print()
# Beispiel: Benutzereingabe für Name und Geburtsdatum, alter wird errechnet
import datetime

name = input("Wie heißt du? ")
geburtsjahr = input("In welchem Jahr bist du geboren? ")
geburtsmonat = input("In welchem Monat bist du geboren? (Zahl, z.B. 7 für Juli) ")
geburtstag = input("An welchem Tag bist du geboren? (Zahl) ")

heute = datetime.datetime.now()
try:
    geburtsjahr = int(geburtsjahr)
    geburtsmonat = int(geburtsmonat)
    geburtstag = int(geburtstag)
    geburtstag_datum = datetime.date(geburtsjahr, geburtsmonat, geburtstag)
    alter = heute.year - geburtsjahr
    # Prüfen, ob der Geburtstag dieses Jahr schon war
    if (heute.month, heute.day) < (geburtsmonat, geburtstag):
        alter -= 1
    print(f"\n\nHallo {name}, du bist {alter} Jahre alt.")
except ValueError:
    print("Bitte gib gültige Zahlen für Jahr, Monat und Tag ein.")
except Exception as e:
    print(f"Fehler: {e}")
