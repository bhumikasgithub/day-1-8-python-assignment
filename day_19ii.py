#4
def index_of_caps(word):
    result = []  # We start with an empty list

    for i in range(len(word)):  # Go through every letter one by one
        if word[i].isupper():   # Check if the letter is a capital letter
            result.append(i)    # Save the position in the list

    return result  # Give the list back
print(index_of_caps("eDaBiT"))     # ➞ [1, 3, 5]
print(index_of_caps("eQuINoX"))    # ➞ [1, 3, 4, 6]
print(index_of_caps("determine"))  # ➞ []
print(index_of_caps("STRIKE"))     # ➞ [0, 1, 2, 3, 4, 5]
print(index_of_caps("sUn"))        # ➞ [1]


#5
def find_even_nums(num):
    return [i for i in range(1, num + 1) if i % 2 == 0]

user_input = input("enter the number")
even_number = find_even_nums(int(user_input))  # Convert input to int

print(f"the even numbers are: {even_number}")  # Fix f-string
