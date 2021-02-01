import MyMathPy as MyMath

s = 0.0

for i in range(int(input())):
    s += MyMath.div(MyMath.inp(), MyMath.inp())

if s == 0:
    print(MyMath.error)
else:
    print(" 1 / " + str(s) + " = " + str(MyMath.div(1, s)))
