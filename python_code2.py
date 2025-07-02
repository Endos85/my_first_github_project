
# Dieses Skript berechnet die Fakultät einer gegebenen Zahl mit Rekursion

def fakultaet(n):
    if n == 0 or n == 1:
        return 1
    return n * fakultaet(n - 1)

# Beispielanwendung
zahl = 5
print(f"Die Fakultät von {zahl} ist {fakultaet(zahl)}")