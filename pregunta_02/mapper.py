#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
        a=0
        for line in sys.stdin:
                a= a+1
                words= line.split(',')
                if( len(words) >2 and a>1):
                        sys.stdout.write("{}\t{}\n".format(words[3], words[4]))
