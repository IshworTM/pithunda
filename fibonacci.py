no_of_els = int(input("How many number of elements do you want?\n>> "))

fibo_series = [0,1]
def fibo(num1, num2):
    while len(fibo_series) < no_of_els:
        num3 = num1+num2
        fibo_series.append(num3)
        fibo(num2,num3)
fibo(0,1)
print(fibo_series)



