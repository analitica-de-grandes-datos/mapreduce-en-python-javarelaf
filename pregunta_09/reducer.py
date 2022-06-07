#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

#! /usr/bin python3

import sys
import bisect
#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    curkey = None
    registros=[]
    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:
        key,fecha, val = line.split("\t")
        val = int(val)
        bisect.insort(registros,(val,fecha,key))
        
    for n in range(0,6):            
     sys.stdout.write("{}   {}   {}\n".format(registros[n][2],registros[n][1],registros[n][0]))
     