import os, sys  # má ordenação (isort), F401 (sys não usado)

import json  # espaçamento errado (black)

def somar(a,b):   # espaçamento errado (black), vírgula sem espaço (flake8)
  print(a+b)  # indentação errada (black), uso de print (flake8-print)
  print('teste')  # uso de print (flake8-print)
    

somar(1,2)  # trailing whitespace  
