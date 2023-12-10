#Some list methods:-

#1. Indexing
my_list = ["Hi", 1, 2, 3, 4, 5, "oh no", "rip"]
#display oh no from the list using list indexing.
print( "The sixth item on my_list is:\n->", my_list[6])


#2. Updating
my_list2 = my_list.copy()
my_list2[6] = "oh yes"
#displaying the same item but after being updated
print("The sixth item on my_list after being updated is:\n->", my_list2[6])


#3. Nesting
my_list3 = [100, [10, 192], "hi" , ["hello", "bye"]]
#displaying first element from both of the nested lists
print("First item from the first nested list:\n->", my_list3[1][0])
print("Second item from the second nested list:\n->",my_list3[3][0])


#4. Deleting items from a list
#deleting the first item from my_list and displaying the list.
my_list4 = my_list.copy()
del my_list4[0]
print("After deleting the first item from my_list:\n->",my_list4)


#5. Iteration
print("\nPrinting every single item on the list:")
for item in my_list:
    print(item)


#6. Length
print(f"The length of the first list is: {len(my_list)}")


#7. Slicing
print(f"Displaying only the numbers from the list using list slicing:\n>> {my_list[1:6]}")


#8. Negative Indices in list
print(f"Displaying the last elemet of the lists using negative indices:\n>> {my_list[-1]}")


#9. Deleting slices from the list:
sliced_list = my_list.copy()
del sliced_list[1:6]
print(f"Displaying everything except numbers from the list:\n>> {sliced_list}")


#10. Check if an element is in the list:
in_list = "Hi" in my_list
print(f"Check if 'Hi' is in the list:\n>> {in_list}")

notIn_list = "Bye" not in my_list
print(f"Check if 'Bye' is in the list:\n>> {notIn_list}")