# прога выведет результаты в консоль,
# а также создаст txt файлик

import sys

original_stdout = sys.stdout

# формулы
Rrange = [0, 10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5000]


def results(list):
    Rrange = list

    for R in Rrange:
        E = 2.4
        r = 320
        print("Дано:\n E={0}В\n r = {1}Ом\n R={2}Ом\n\n".format(E, r, R))

        I = E / (r + R)
        print("I = E / (r + R)")
        print("I = {1} / ({2} + {3}) = {0}A = {4}мА\n".format(I, E, r, R, I * 1000))
        Un = I * R
        print("Un = I*R")
        print("Un = {0}*{1} = {2}В\n".format(I, R, Un))
        Pr = (I ** 2) * r
        print("Pr = (I^2) * r")
        print("PR = {1} * {2} = {0}Вт\n".format(Pr, I ** 2, r))
        Pn = (I ** 2) * R
        print("Pn = (I^2) * R")
        print("Pn = {0} * {1} = {2}Вт\n".format(I ** 2, R, Pn))
        Pi = E * I
        print("Pi = E * I")
        print("Pi = {0} * {1} = {2}Вт\n".format(E, I, Pi))
        n = Pn / Pi
        print("n = Pn / Pi")
        print("n = {0} / {1} = {2}%\n\n\n".format(Pn, Pi, n))





with open('results.txt', 'w') as f:
    sys.stdout = f
    results(Rrange)
