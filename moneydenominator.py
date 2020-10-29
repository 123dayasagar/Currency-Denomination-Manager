print("Enter the number of notes available in the cash counter")       #Number of notes available in the Cash counter

onen = int(input("1 X "))
twon = int(input("2 X "))
fiven = int(input("5 X "))
tenn = int(input("10 X "))
twentyn = int(input("20 X "))
fiftyn = int(input("50 X "))
hundredn = int(input("100 X "))
twohundredn = int(input("200 X "))
fivehunderedn = int(input("500 X "))
twothousandn = int(input("2000 X "))

while True:
    while True:
       x = int(input("Enter the user bill amount in numbers"))     #Bill Amount
       y = int(input("Enter the amount paid by the user in numbers")) #Amount paid
       if x<0 or y<0:                                                          #To check whether amount is positive or negative
           print("entered amount is negative, please add valid amount again")
       else:
          remainder=y-x
          if remainder<= 0:                                   #To determine whether the paid amount is not lesser than the bill amount
            print("Insufficient amount added. The Least Amount that has to be added in the bill is:",-remainder)
          else:
            break

    print("Enter the number of notes given ")     #Notes given while paying the bill
    m = int(input("2000 X "))
    twothousandn += m
    m = int(input("500 X "))
    fivehunderedn += m
    m = int(input("200 X "))
    twohundredn += m
    m = int(input("100 X "))
    hundredn += m
    m = int(input("50 X "))
    fiftyn += m
    m = int(input("20 X "))
    twentyn += m
    m = int(input("10 X "))
    tenn += m
    m = int(input("5 X "))
    fiven += m
    m = int(input("2 X "))
    twon += m
    m = int(input("1 X "))
    onen += m

    reminder = y - x
    one = 0
    two = 0
    five = 0
    ten = 0
    twenty = 0
    fifty = 0
    hundred = 0
    twohundred = 0
    fivehundered = 0
    twothousand = 0

    while (reminder != 0):
        if reminder >= 500:
            if fivehunderedn != 0:
                reminder = reminder - 500
                fivehundered += 1
                fivehunderedn -= 1

        elif reminder >= 2000:
            if twothousandn != 0:
                reminder = reminder - 2000
                twothousand += 1
                twothousandn -= 1
        elif reminder >= 200:
            if twohundredn != 0:
                reminder = reminder - 200
                twohundred += 1
                twohundredn -= 1
        elif reminder >= 100:
            if hundredn != 0:
                reminder = reminder - 100
                hundred += 1
                hundredn -= 1
        elif reminder >= 50:
            if fiftyn != 0:
                reminder = reminder - 50
                fifty += 1
                fiftyn -= 1
        elif reminder >= 20:
            if twentyn != 0:
                reminder = reminder - 20
                twenty += 1
                twentyn -= 1
        elif reminder >= 10:
            if tenn != 0:
                reminder = reminder - 10
                ten += 1
                tenn -= 1
        elif reminder >= 5:
            if fiven != 0:
                reminder = reminder - 5
                five += 1
                fiven -= 1
        elif reminder >= 2:
            if twon != 0:
                reminder = reminder - 2
                two += 1
                twon -= 1
        elif reminder >= 1:
            if onen != 0:
                reminder = reminder - 1
                one += 1
                onen -= 1
    print("Change of Rupees",y-x,end=" ")
    print("has to be given back")
    print("Therefore, Displayed below is the number of notes that should be given back:")    #Amount of note that has to be returned back
    print("2000 X", twothousand)
    print("500 X", fivehundered)
    print("200 X", twohundred)
    print("100 X", hundred)
    print("50 X", fifty)
    print("20 X", twenty)
    print("10 X", ten)
    print("5 X", five)
    print("2 X", two)
    print("1 X", one)