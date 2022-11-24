import random


lis = [random.randint(0, 9) for x in range(10)]

print(lis)




l = len(lis)

ins = 1




while ins < l:

    temp = lis[ins]

    cmp = ins - 1


    while cmp >= 0:

        if temp < lis[cmp]:

            lis[cmp + 1] = lis[cmp]

            print(lis)

        else:

            break


        cmp = cmp - 1




    lis[cmp + 1] = temp

    print(lis)


    ins = ins + 1




