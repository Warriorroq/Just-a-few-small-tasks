import MyMathPy as math
sum = 0.0

for i in range(int(input())):
    sum += math.add(math.inp(), math.inp())

print(" 1 / " + str(sum) + " = " + str(math.div(1, sum)))