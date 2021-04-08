#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

ileliczb = None
maksliczba = None

while ileliczb == None:
    try:
        ileliczb = int(input("Podaj ilość typowanych liczb: "))
        break
    except ValueError:
        print("Musisz podać liczbę")


while maksliczba == None or maksliczba < ileliczb:
    try:
        maksliczba = int(input("Podaj maksymalną liczbę: "))
        if maksliczba < ileliczb:
            print("Maksymalna liczba nie może być mniejsza od ilości prób")
        else:
            break
    except ValueError:
        print("Musisz podać liczbę")


print("Wytypuj %s z %s liczb: " % (ileliczb, maksliczba))

#losowanie
liczbylosowe = []
i = 0
while i < ileliczb:
    losowanie = random.randint(1, maksliczba)
    if liczbylosowe.count(losowanie) == 0:
        liczbylosowe.append(losowanie)
        i = i + 1


print(liczbylosowe)

#typowanie
kupon = set()
i = 0
while i < ileliczb:
    try:
        typ = int(input("Podaj liczbę do skreślenia: "))
        if typ > maksliczba:
            print("maksymalna liczba to %s" % maksliczba)
        elif typ not in kupon:
            kupon.add(typ)
            i = i + 1
    except ValueError:
        print("Wytypuj liczbę")

