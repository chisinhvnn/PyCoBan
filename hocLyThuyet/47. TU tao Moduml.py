def green(n):
    i = 0
    while i < n:
        i = i+1
        print ("Heloo HOc Python")
def sumNums(*args):
    sum = 0
    for i in args:
        sum = sum+ i
        return sum

def myRange(starts, stop,step):
    i = starts
    while i <= stop:
        yield(i)
        i += step
               