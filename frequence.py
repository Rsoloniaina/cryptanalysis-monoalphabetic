#!/usr/bin/python3
import sys

alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
dicoLettres = {c: 0 for c in alphabet}
nbLettres = 0

# Lecture fichier ou stdin
if len(sys.argv) > 1:
    with open(sys.argv[1], 'r') as fichier:
        contenu = fichier.read()
else:
    contenu = sys.stdin.read()

# Comptage sécurisé
for lettre in contenu:
    if lettre in dicoLettres:
        dicoLettres[lettre] += 1
        nbLettres += 1

# Affichage dans l'ordre
for lettre in alphabet:
    freq = dicoLettres[lettre] / nbLettres if nbLettres > 0 else 0.0
    print(lettre, freq)

