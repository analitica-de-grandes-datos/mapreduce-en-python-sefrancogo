#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys 

if __name__ == "__main__":
  
        for line in sys.stdin:
                num, letters = line.strip().split()
                letters= letters.split(',')
                if len(num) == 1:
                        num = "0" + num
                for l in letters:
                        sys.stdout.write("{}\t{}\n".format(l,num))
