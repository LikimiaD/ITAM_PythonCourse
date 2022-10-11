def summation(start, end):
    x = 0
    if end > start:
        for i in range(start, end+1):
            x += i
    else:
        for i in range(end,start+1):
            x += i
    print(x)

summation(2,12)
summation(-4,4)
summation(3,2)