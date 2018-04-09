xl=[int(x) for x in input().split()]
customer_size=[int(x) for x in input().split()]
if (xl[0]>customer_size[0]):
    if (xl[1]>customer_size[1]):
        print("yes")
    else:
        print("no")
else:
    print("no")
