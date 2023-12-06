#3x3 Matrix with list comprehension
# i = int(input())
# j = int(input())
# k = int(input())

# list1 =[]
# list2 =[]
# for i in range(1,9,3):
#     for j in range(3):
#         list1.append(j+i)
#     list2.append(list1)
#     list1 =[]
# print(list2)

def matrixx():
    return [ [i, i+1, i+2] for i in range(1,9,3) ]
print(matrixx())





