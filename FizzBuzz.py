
##fizzbuzz
def fizzbuzz(): 
    for x in range (1, 301):
        l = []
        if x % 3 == 0:
            l.append("Fizz")
        if x % 5 == 0:
            l.append("Buzz")
        if x % 7 == 0:
            l.append("Bang")
        if x % 11 == 0:
            l = ["Bong"]
        if x % 13 == 0:
            if "Fizz" in l:
                l.insert(1, "Fezz")
            else: l.insert (0, "Fezz")
        if l:
            print("".join(l))
        else:
            print(x)

##run fizzbuzz
fizzbuzz()