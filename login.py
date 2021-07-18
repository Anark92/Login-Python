import time
import os
import sys
import sqlite3
import getpass
 

 
registeredUser = ('Anark')
registeredPW = ('Anark')
 

def login(usuario,passw):
    if usuario in registeredUser:
        if passw in registeredPW:
            return 1
        else:
            print("\nLa contraseña no coincide\n")
    else:
        return 2
 
 
usuario=input('User:')
passw = getpass.getpass('Password: ')
 
if login(usuario,passw)==1:
    print('Bienvenido ',usuario)
else:
    print('Ups.. Usuario no registrado.')