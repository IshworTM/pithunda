def factorial(num):
    if num == 0 or num ==1 :
        return 1
    else:
        return num* factorial(num-1)

print(factorial(int(input("Enter a number:\n>> "))))