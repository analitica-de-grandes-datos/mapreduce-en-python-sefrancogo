#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

        curkey = None
        total = 0
        for s in sys.stdin:
                key, val=  s.split("\t")
                val= int(val)

                if key == curkey:
                        total += val       
                else:
                        if curkey is not None:
                                sys.stdout.write("{},{}\n".format(curkey, total))

                        curkey= key
                        total= val
        sys.stdout.write("{},{}\n".format(curkey, total))
