def fizzbuzz(n):
    res = ""
    for i in range(1, n + 1):
        res = ""

        if i % 3 == 0:
            res += "Fizz"
        if i % 5 == 0:
            res += "Buzz"
        if i % 7 == 0:
            res += "Boom"

        print(res if res else i)
