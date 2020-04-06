username = input ("Username : ")
password = input ("Password : ")
if username == "s3009343243" and password == "ffs0d9h4jdf" :
    print ("--------Welcome-------")
    print ("----- Shop ------")
    print ("1. iPhone 11 Pro : 30000 THB")
    print ("2. iPhone X      : 20000 THB")
    whattobuy = int(input("Which Products Will You Purchase (1-2) : "))
    if whattobuy == 1:
        howmany = int(input("How Many : "))
        price1 = 30000 * howmany
        vat = 7
        result1 = price + (price*vat/100)
        more = int(input("Anymore? Yes or No : "))
        if more == Yes:
                howmany = int(input("How Many : "))
                price2 = 20000 * howmany
                vat = 7
                result2 = price + (price * vat / 100)
                print (result1 + result2)
        elif more == No:
                print(result1)

    elif whattobuy == 2:
        howmany = int(input("How Many : "))
        price = 20000 * howmany
        vat = 7
        result = price + (price * vat / 100)
        print(result)
