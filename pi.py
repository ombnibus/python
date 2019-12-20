def GetPi(n):
    sum = 0
    count = 1
    while count <= n:
        if count % 2 == 0:
            sum -= 1 / count**2
        else:
            sum += 1 / count**2
        count += 1
    print("%1.40f" %((6 / 3**0.5) * sum**0.5))
GetPi(1000000000)
