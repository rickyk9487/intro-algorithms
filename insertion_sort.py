def insertion_sort(x):
    # x is a list of type int
    for i in range(len(x) - 1):
        print "1.", x
        if x[i] < x[i + 1]:
            pass
        else:
            tmp = x[i]
            x[i] = x[i + 1]
            x[i + 1] = tmp
        print "2.", x
        for j in range(i):
            print "3.", x
            if x[i - j] < x[i - j - 1]:
                print "4.", i - j - 1, i - j, x[i - j - 1], x[i - j]
                tmp = x[i - j]
                x[i - j] = x[i - j - 1]
                x[i - j - 1] = tmp
            else:
                pass
    return x

print insertion_sort([15, 14, 13, 12, 11, 10])
