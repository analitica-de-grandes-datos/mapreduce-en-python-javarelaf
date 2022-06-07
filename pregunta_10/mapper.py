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
        pares=list()
        line=line.replace('\n','')
        index,letras = line.split('\t')
        letras=letras.split(',')
        for letra in letras:
            pares.append([index,letra])
            #
            # escribe al flujo estandar de salida
            #
        for par in pares:
            sys.stdout.write(str(par[1])+'\t'+str(par[0])+'\n')