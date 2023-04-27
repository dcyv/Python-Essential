#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Probar una función que toma un argumento (un año) y devuelve Verdadero si el año es bisiesto o Falso de lo contrario.
# Autor: Diana Yacchirema


def isYearLeap(year):
    return not year % 4 and (year % 100 or not year % 400)

print("Verificando año bisiesto" + "\n")
print("Ingrese el año a verificar")
year = input()
isYearLeap(int(year))

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




