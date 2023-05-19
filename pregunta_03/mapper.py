#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
        for line in sys.stdin:
                words= line.strip().split(',')
                sys.stdout.write("{},{}\n".format(words[1], words[0]))
