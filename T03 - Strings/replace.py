# Replaces '!' in a string with ' '.
# Changes the string to uppercase.
# Reverses the characters in the string.

sentence_string = "The!quick!brown!fox!jumps!over!the!lazy!dog!."
sentence_string = sentence_string.replace("!.", ".")
sentence_string = sentence_string.replace("!", " ")
print(sentence_string)

sentence_string = sentence_string.upper()
print(sentence_string)

print(sentence_string[::-1])  # reverse sentence