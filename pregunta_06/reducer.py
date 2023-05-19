#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import math

if __name__ == '__main__':

        curkey = None
        mini = math.inf
        maxi = 0

        for line in sys.stdin:
                key, val = line.strip().split("\t")
                val= float(val)

                if curkey == key:
                        if val > maxi:
                                maxi= val
                        elif val < mini:
                                mini = val
                else:
                        if curkey is not None:
                                sys.stdout.write("{}\t{}\t{}\n".format(curkey, maxi, mini))
                        curkey = key
                        mini= float(val)
                        maxi = float(val)

        sys.stdout.write("{}\t{}\t{}\n".format(curkey, maxi, mini))  
