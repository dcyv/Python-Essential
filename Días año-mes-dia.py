#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Probar una función que toma tres argumentos (un año, un mes y un día del mes) y devuelve los días correspondiente del año
# Autor: Diana Yacchirema

def isYearLeap(year):
    return not year % 4 and (year % 100 or not year % 400)

def daysInMonth(year, month):
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isYearLeap(year) and month == 2:
        return 29
    return monthDays[month - 1]

def dayOfYear(year, month, day):
            if isYearLeap(year):
                K = 1
            else:
                K = 2
            N = int((275 * month) / 9.0) - K * int((month + 9) / 12.0) + day - 30
    #        print (N)
            return N

while True:    
    ano = int(input("Ingrese año:"))
    mes = int(input("Ingrese mes:"))
    dia = int(input("Ingrese dia:"))
    d=dayOfYear(ano,mes,dia)
    fecha=str(dia) + "-" + str(mes) + "-" + str(ano)
    print("La Fecha " + fecha + " tiene:" + str(d) + " dias")     
    


# In[ ]:





# In[ ]:





# In[ ]:




