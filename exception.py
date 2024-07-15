result = int(input("Enter"))

try:
    result // 0

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("This block always executes.")