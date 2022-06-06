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
        # genera las tuplas palabra \tabulador 1
        # ya que es un conteo de palabras
        #
        
            #
            # escribe al flujo estandar de salida
            #
            sys.stdout.write("{}\t{}\n".format(str(line.split('   ')[0]),float(line.split('   ')[2])))