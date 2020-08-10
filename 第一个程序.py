print("######杨辉三角######")
temp = input("请输入行数:")
guess = int(temp)



i = 0
j = 0
a = [[0] * guess for i in range(guess)]

while i < guess:
    if i == 0:
        a[0][0]=1
    else:
        for j in range(i+1):
            a[i][0]=1
            if j > 0:
                a[i][j] = a[i-1][j] + a[i-1][j-1]
            j=j+1
    i=i+1

k=0
j=0
for k in range(guess):
    print(" "*(3*(guess-k)-2),end="")
    for j in range(k+1):
        print(a[k][j],end="")
        if a[k][j]<10:
          print("     ",end="")
        if a[k][j]>9 and a[k][j]<100:
          print("    ",end="")
        if a[k][j]>99:
          print("   ",end="")
        j=j+1
    print("\n")
