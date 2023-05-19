#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys 

if __name__ ==  '__main__':

        curkey = None
        for line in sys.stdin:
                key, val = line.strip().split("\t")
                val = int(val)
                if curkey == key: sys.stdout.write(",{}".format(val)) 
                else:
                        if curkey is not None: sys.stdout.write("\n") 
                        sys.stdout.write("{}\t{}".format(key,val))    
                        curkey = key
        sys.stdout.write("\n")
