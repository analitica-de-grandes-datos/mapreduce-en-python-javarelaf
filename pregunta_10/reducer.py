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
    keys=[]
    total=[]
    total2=[]
    total3=[]
    total4=''
    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:
        key, val = line.split("\t")
        val = int(val)
        if key == curkey:
            #
            # No se ha cambiado de clave. Aca se acumulan los valores para la misma
            # clave.
            #
            total.append(val)
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
                for num in total:
                    bisect.insort(total2,num)
                total3=[str(x) for x in total2]
                total4 = ','.join(total3)
                sys.stdout.write("{}\t{}\n".format(curkey, total4))
                # inicializamos
                total=[]
                total2=[]
                total3=[]
                total4 = ''

            curkey = key
            total.append(val)
                        
    for num in total:
                    bisect.insort(total2,num)
    total3=[str(x) for x in total2]
    total4 = ','.join(total3)
                
    sys.stdout.write("{}\t{}\n".format(curkey, total4))