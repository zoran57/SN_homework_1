#fizzbuzz

"""
fizzbuzz = int(input("unesi broj od 1 do 100:"))
"""

for fizzbuzz in range(1,101):
# ako izostavimo liniju 10 ispisuje se za prvih 100brojeva
    """
    fizzbuzz = int(input("unesi broj od 1 do 100:"))
    """
    if fizzbuzz % 3 == 0 and fizzbuzz % 5  == 0:
        print("fizzbuzz")
        continue

    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue

    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
