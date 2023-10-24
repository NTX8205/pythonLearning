n = int(input("please input the value of N (N>3):"))
level = 1
space = n
for i in range(0,n):
    if i == 0:
        space-=1
        for j in range(0,space):
            print(" ",end="")
        print("*")
    else:
        level+=2
        space-=1
        for k in range(0,space):
            print(" ",end="")
        for l in range(0,level):
            print("=",end="")
        print("")

for m in range(0,(level+1)//2-2):
    print(" ",end="")
print("| |")