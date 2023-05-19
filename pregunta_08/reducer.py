#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys 

if __name__ == "__main__":

        curkey = None
        suma = 0
        cont = 0
        prom = 0

        for line in sys.stdin:
                key, val = line.strip().split("\t")
                val = float(val)
                if curkey == key:
                        suma += val
                        cont += 1
                else:
                        if curkey is not None:
                                prom = suma/cont
                                sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, prom))
                        curkey = key
                        suma= float(val)
                        cont = 1
        prom = suma/cont
        sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, prom))  
