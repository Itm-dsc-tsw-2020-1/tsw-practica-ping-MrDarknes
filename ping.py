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

import os
red = "200.33.171.0/24"
os.system("nmap -sn " + red)



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
"""
import os
c=0
red="200.33.171."
for x in range(30):
    x = x + 1
    respuesta = os.system("ping -c 1 " + red + str(x))
    if respuesta == 0:
        c+=1

print("Numero de hosts encendidos: "+str(c))
"""


""" 
RESULTADOS DEL NMAP PARA VERIFICAR CUANTAS COMPUTADORAS HAY ENCENDIDAS EN EL TEC:

Nmap scan report for delfin2.itmorelia.edu.mx (200.33.171.11)
Host is up (0.018s latency).
Nmap scan report for 200.33.171.13
Host is up (0.026s latency).
Nmap scan report for dsc.itmorelia.edu.mx (200.33.171.20)
Host is up (0.0030s latency).
Nmap scan report for 200.33.171.50
Host is up (0.032s latency).
Nmap scan report for libra.itmorelia.edu.mx (200.33.171.54)
Host is up (0.022s latency).
Nmap scan report for 200.33.171.66
Host is up (0.017s latency).
Nmap scan report for denebvirtual.itmorelia.edu.mx (200.33.171.77)
Host is up (0.0094s latency).
Nmap scan report for sappp.itmorelia.edu.mx (200.33.171.80)
Host is up (0.037s latency).
Nmap scan report for 200.33.171.86
Host is up (0.010s latency).
Nmap scan report for 200.33.171.99
Host is up (0.0040s latency).
Nmap scan report for 200.33.171.115
Host is up (0.088s latency).
Nmap scan report for 200.33.171.120
Host is up (0.015s latency).
Nmap scan report for vinculacion.itmorelia.edu.mx (200.33.171.124)
Host is up (0.25s latency).
Nmap scan report for 200.33.171.125
Host is up (0.010s latency).
Nmap scan report for 200.33.171.127
Host is up (0.061s latency).
Nmap scan report for 200.33.171.254
Host is up (0.034s latency).
Nmap done: 256 IP addresses (16 hosts up) scanned in 214.23 seconds
"""
