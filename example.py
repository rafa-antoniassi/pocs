import json  # espaçamento errado (black)
import logging
import os  # má ordenação (isort), F401 (sys não usado)
import sys


def somar(a, b):  # espaçamento errado (black), vírgula sem espaço (flake8)
    logging.info(a + b)  # indentação errada (black),
    # uso de print (flake8-print)
    logging.info(
        "testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
    )  # uso de print (flake8-print)


somar(1, 2)  # trailing whitespace
