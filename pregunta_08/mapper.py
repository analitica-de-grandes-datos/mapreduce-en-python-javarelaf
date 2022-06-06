#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

#! /usr/bin/python3

#
# Se inicializa
#
import sys
if __name__ == "__main__":

    #
    # itera sobre cada linea de codigo recibida
    # a traves del flujo de entrada
    #
    for line in sys.stdin:
            #
            # escribe al flujo estandar de salida
            #
            sys.stdout.write("{},{}".format(line.split('   ')[0],line.split('   ')[2]))
