
## function for fizzbuzz
def fizzbuzz(): 
    for x in range (1, 301):
        ## create an empty list to then populate with the replacement message
        l = []

        ## for multiples of 3, 5 and 7 append the appropriate value to the list
        if x % 3 == 0:
            l.append("Fizz")
        if x % 5 == 0:
            l.append("Buzz")
        if x % 7 == 0:
            l.append("Bang")

        ## for multiples of 11 set the list to just have Bong
        if x % 11 == 0:
            l = ["Bong"]

        ## for multiples of 13 if the list contains Fizz add Fezz after, if not add it at the start
        if x % 13 == 0:
            if "Fizz" in l:
                l.insert(1, "Fezz")
            else: l.insert (0, "Fezz")

        ## if there is a value in the list, output the values
        if l:
            ## for multiples of 17 reverse before outputting
            if x % 17 == 0:
                l.reverse()
                print("".join(l))
            else: print("".join(l))  
        ## else print the value of x
        else:
            print(x)

## run fizzbuzz
fizzbuzz()