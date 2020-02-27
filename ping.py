"""
## ANALISIS DE CONEXIÓN
#Libreria para llamar al sistema operativo
import os
#Definir servidor a revisar
hostname = "www.itmorelia.edu.mx"
hostname = "11.0.6.0"
#Llamada a consola
respuesta = os.system("ping -c 1 " + hostname)
#Verificando respuesta
if respuesta==0:
    print(hostname + ": está en funcionamiento!")
else:
    print(hostname + ": No funciona")

"""

 ## DETECTAR COMPUTADORAS ACTIVAS
"""
import os
red = "200.33.171.0/24"
os.system("nmap -sn " + red)
"""


## DETECTAR PUERTOS ABIERTOS
"""
import os
computadora = "200.33.171.77"
os.system("nmap -sT " + computadora)
"""


##DETECTAR SISTEMA OPERATIVO
"""
import os
computadora = "200.33.171.77"
os.system("nmap -O " + computadora)
"""


##CICLO PARA VERIFICAR TODAS LAS COMPUTADORAS ENCENDIDAS EN EL TEC
import os
c=0
red="200.33.171."
for x in range(30):
    x = x + 1
    respuesta = os.system("ping -c 1 " + red + str(x))
    if respuesta == 0:
        c+=1

print("Numero de hosts encendidos: "+str(c))

