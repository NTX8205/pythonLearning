coin_list = [50, 10, 5, 1]


def function_Vender(All_price):
    Cola = 30
    Black_tea = 20
    Water = 15

    if All_price >= 30:
        print("Which drink you want? (Cola=>30 Black_tea=>20 Water=>15)")
    elif All_price >= 20:
        print("Which drink you want? (Black_tea=>20 Water=>15)")
    elif All_price >= 15:
        print("Which drink you want? (Water=>15)")
    else:
        print("Your coin isn't enough to buy!!\n")
        return 0

    while (True):
        choice = input("choice => ")

        if choice == 'Cola':
            if All_price >= Cola:
                print("\nYour drink => Cola")
                return Cola
            else:
                print("Your coin isn't enough to buy!!\n")
                continue
        elif choice == 'Black_tea':
            if All_price >= Black_tea:
                print("\nYour drink => Black_tea")
                return Black_tea
            else:
                print("Your coin isn't enough to buy!!\n")
                continue
        elif choice == 'Water':
            if All_price >= Water:
                print("\nYour drink => Water")
                return Water
            else:
                print("Your coin isn't enough to buy!!\n")
                continue
        else:
            print("\nNo this option! Please choice again!!")
            continue
        break


def function_coin():
    print("Please give me coin(you can give 1,5,10,50)")
    ft = int(input("50 => "))
    ten = int(input("10 => "))
    fi = int(input("5  => "))
    one = int(input("1  => "))
    countCoin = ft*50 + ten*10 + fi*5 + one*1
    print("=> 50*%d + 10*%d + 5*%d + 1*%d" % (ft, ten, fi, one))
    print("All price => %d\n" % (countCoin))
    return countCoin


def function_remain(choice, All_price):

    total = All_price - choice
    count = [0, 0, 0, 0]

    if total > 0:
        while (True):
            if total >= 50:
                count[0] = total / 50
                total = total % 50
            elif total >= 10:
                count[1] = total / 10
                total = total % 10
            elif total >= 5:
                count[2] = total / 5
                total = total % 5
            elif total >= 1:
                count[3] = total / 1
                total = total % 1
                break
            else:
                break

    print("------- Remain -------")
    for i in range(len(count)):
        if count[i] > 0:
            print(str(coin_list[i]) + "*%d" % (count[i]))


All_price = function_coin()
function_remain(function_Vender(All_price), All_price)
