original_str = input("Enter string : ? ")
remove_chr = int(input("Enter number of chr to remove :? "))
new_str = original_str[remove_chr:]
print(new_str)

original_str = input(" Enter string : ? ")
remove_chr = int(input("Enter number of chr to remove :? "))
new_str = list(original_str[remove_chr:])
print(new_str)

original_str = input(" Enter string : ? ")
remove_chr = int(input("Enter number of chr to remove :? "))
new_str = list(original_str)
new_str = new_str[remove_chr:]
print(new_str)