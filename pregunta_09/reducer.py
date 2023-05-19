#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':
        cont =0
        while cont < 6:
                cont +=1
                num, letter, date = sys.stdin.readline().strip().split(",")

                num= int(num)

                sys.stdout.write("{}   {}   {}\n".format(letter, date, num))
