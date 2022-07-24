
##fizzbuzz
def fizzbuzz(): 
    for x in range (1, 101):
        l = []
        if x % 3 == 0:
            l.append("Fizz")
        if x % 5 == 0:
            l.append("Buzz")
        if x % 7 == 0:
            l.append("Bang")
        if x % 11 == 0:
            l = ("Bong")
        if l:
            print("".join(l))
        else:
            print(x)

##run fizzbuzz
fizzbuzz()