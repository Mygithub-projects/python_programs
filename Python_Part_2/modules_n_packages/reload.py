import calculator
import time
import imp


x=22
y=11

print("sum of {} and {} = {}".format(x,y,calculator.add(x,y)))
time.sleep(10)
imp.reload(calculator)
print("difference between {} and {} = {}".format(x,y,calculator.diff(x,y)))

