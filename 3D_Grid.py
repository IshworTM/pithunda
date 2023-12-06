print("\nYou are given three integers x,y and z representing the dimensions of a cuboid along with an integer n.\nPrint a list of all possible coords given by (i,j,k) on a 3D grid, where the sum of i+j+k is not equal to n.\nHere, 0 <= i <= x;\n0 <= j <= y;\n0 <= k <= z.")


x = int(input("Enter x:\n>> "))
y = int(input("Enter y:\n>> "))
z = int(input("Enter z:\n>> "))
n = int(input("Enter n:\n>> "))

lst = [[num1 , num2, num3] for num1 in range(x+1) for num2 in range(y+1) for num3 in range(z+1) if (num1+num2+num3)!=n]

print(lst)