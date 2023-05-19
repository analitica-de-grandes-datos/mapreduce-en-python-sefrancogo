#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

        for s in sys.stdin:
                let, date, val = s.strip().split()
                sys.stdout.write("{}\t1\n".format(let))
