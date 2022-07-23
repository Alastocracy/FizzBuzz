
##fizzbuzz
def fizzbuzz(): 
    for x in range (1, 101):
        if x % 3 == 0 and x % 5 == 0 and x % 7 == 0:
            print("FizzBuzzBang")
            continue
        if x % 3 == 0 and x % 7 == 0:
            print("FizzBang")
            continue
        if x % 5 == 0 and x % 7 == 0:
            print("BuzzBang")
            continue
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
            continue
        elif x % 3 == 0:
            print("Fizz")
            continue
        elif x % 5 == 0:
            print("Buzz")
            continue
        elif x % 7 == 0:
            print("Bang")
            continue
        print(x)

##run fizzbuzz
fizzbuzz()