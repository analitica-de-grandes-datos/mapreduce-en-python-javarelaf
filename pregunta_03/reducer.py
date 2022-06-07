#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#! /usr/bin/python3
registros=[]
import sys
import bisect
if __name__ == "__main__":

    #
    # itera sobre cada linea de codigo recibida
    # a traves del flujo de entrada
    #
    for line in sys.stdin:
        key,val=line.split('\t')  
        val=int(val)
        bisect.insort(registros,(val,key))
        
    for n in registros: 
      sys.stdout.write("{},{}\n".format(n[1],n[0]))