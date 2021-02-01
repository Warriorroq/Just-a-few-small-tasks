import MyMathPy as MyMath
s = 0.0

for i in range(int(input())):
    s += MyMath.div(MyMath.inp(), MyMath.inp())

print(" 1 / " + str(s) +
      " = " + str(MyMath.div(1, s)))