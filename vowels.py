# count the no of strings in the given strings

my_string = input("Please enter the String: ")

vowels = ["a", "e", "i", "o", "u"]

cnt = 0
for char in my_string:
    if char in vowels:
        cnt += 1
    else:
        pass

print(f"Vowels in the string: {cnt}")