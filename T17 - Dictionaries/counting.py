# Count the number of times a character occurs (character frequency) in a string.
# Store each letter followed by the number of occurrences in a dictionary and print it out.

Str_1 = "Pineapples"
Str_1 = Str_1.lower()  # Make everything lowercase so letter frequency count is not messed up by capital P

freq = {}  # Create empty dictionary.

for i in Str_1:
    if freq.get(i):  # If a letter has already been added to the dictionary, +1 to the freq of that letter
        freq[i] += 1
    else:
        freq[i] = 1  # Else add the new letter to the dictionary

print(freq)