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
        
        if key == curkey:
            #
            # No se ha cambiado de clave. Aca se acumulan los valores para la misma
            # clave.
            #
            bisect.insort(registros,(val,fecha,key))
        else:
            #
            # Se cambio de clave. Se reinicia el acumulador.
            #
            if curkey is not None:
                #
                # una vez se han reducido todos los elementos
                # con la misma clave se imprime el resultado en
                # el flujo de salida
                #
                for n in registros:
                 sys.stdout.write("{}   {}   {}\n".format(n[2],n[1],n[0]))
                # inicializamos
                registros=[]
                

            curkey = key
            bisect.insort(registros,(val,fecha,key))
                        
    
    for n in registros:            
     sys.stdout.write("{}   {}   {}\n".format(n[2],n[1],n[0]))
     