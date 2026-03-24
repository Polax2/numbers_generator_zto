import math
import sys
import os

class RandomNumberGenerator:
    def __init__(self, seedVaule=None):
        self.__seed=seedVaule
    def nextInt(self, low, high):
        m = 2147483647
        a = 16807
        b = 127773
        c = 2836
        k = int(self.__seed / b)
        self.__seed = a * (self.__seed % b) - k * c;
        if self.__seed < 0:
            self.__seed = self.__seed + m
        value_0_1 = self.__seed
        value_0_1 =  value_0_1/m
        return low + int(math.floor(value_0_1 * (high - low + 1)))
    def nextFloat(self, low, high):
        low*=100000
        high*=100000
        val = self.nextInt(low,high)/100000.0
        return val

def gen_int(rng, low, high):
    return rng.nextInt(low, high)

def gen_vector(rng, n, low, high):
    return [rng.nextInt(low, high) for _ in range(n)]

def gen_matrix(rng, n, m, low, high):
    return [[rng.nextInt(low, high) for _ in range(m)] for _ in range(n)]

def save_dat(filename, data):
    with open(filename, "w") as f:
        for name, value in data:
            if isinstance(value, list):
                if isinstance(value[0], list):
                    f.write(name + " = [\n")
                    for i, row in enumerate(value):
                        f.write("  [" + ", ".join(map(str, row)) + "]")
                        if i < len(value) - 1:
                            f.write(",")
                        f.write("\n")
                    f.write("];\n")
                else:
                    f.write(name + " = [" + ", ".join(map(str, value)) + "];\n")
            else:
                f.write(name + " = " + str(value) + ";\n")


rng = RandomNumberGenerator(2137)
n = int(sys.argv[1])
C = gen_vector(rng, n, 0, 10)
W = gen_vector(rng, n, 0, 10)
S = sum(W)
B = rng.nextInt(S // 4, S // S)

BASE_DIR = "C:\\Users\\polan\\opl\\ZTO_lab3"
FILE_NAME = "data2.5.dat"

save_dat(os.path.join(BASE_DIR, FILE_NAME), [
    ("n", n),
    ("C", C),
    ("W", W),
    ("B", B)
])