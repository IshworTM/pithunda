user_input = input("Enter a word/number:\n>> ").lower()

rev_str = user_input[::-1]
print(rev_str)
if user_input == rev_str:
    print(f'{user_input} is a palindrome.')
else:
    print(f'{user_input} is not a palindrome.')