#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Probar una función que toma dos argumentos (un año y un mes) y devuelve el número de días para el par mes / año
# Autor: Diana Yacchirema

def isYearLeap(year):
    return not year % 4 and (year % 100 or not year % 400)

def daysInMonth(year, month):
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isYearLeap(year) and month == 2:
        return 29
    return monthDays[month - 1]

while True:
    mes = int(input("Ingrese mes:"))
    ano = int(input("Ingrese año:"))
    print(f"El mes {mes}/{ano} contiene {daysInMonth(ano, mes)}")


# In[ ]:




