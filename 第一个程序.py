print("######杨辉三角######")
temp = input("请输入行数:")
line_number =int(temp)



line_number_counts = 0 

number_of_columns_counts = 0

a = [[0] * line_number for line_number_counts in range(line_number)] #  定义一个数组储存杨辉三角里的数

while line_number_counts < line_number:
    if line_number_counts == 0:
        a[0][0]=1
    else:
        for number_of_columns_counts in range(line_number_counts+1):
            a[line_number_counts][0]=1 #每行最后一个数字均为一，先输出

            if number_of_columns_counts > 0:
                a[line_number_counts][number_of_columns_counts] = a[line_number_counts-1][number_of_columns_counts] + a[line_number_counts-1][number_of_columns_counts-1]
                # 杨辉三角公式，一个数为其肩上两数之合

            number_of_columns_counts=number_of_columns_counts+1
    line_number_counts=line_number_counts+1

k=0
j=0
for k in range(line_number):
    print(" "*(3*(line_number-k)-2),end="") 
    for j in range(k+1):
        print(a[k][j],end="")
        # 输出储存的杨辉三角，下面三个条件结构是编排数字位置，使输出的阵型好看
        if a[k][j]<10:
          print("     ",end="")

        if a[k][j]>9 and a[k][j]<100:
          print("    ",end="")

        if a[k][j]>99:
          print("   ",end="")
        j=j+1

    print("\n")
