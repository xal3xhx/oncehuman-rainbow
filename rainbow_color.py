Red = "#ce81416"
Orange = "#cffa500"
Yellow = "#cfaeb36"
Green = "#c79c314"
Blue = "#c487de7"
Indigo = "#c4b369d"
Violet = "#c70369d"

# gets input from user
text = input("exter text: ")

output = ""

# adds a color text for each letter in the input
# in the order of the rainbow
# shifted by one so that the first letter is red

for i in range(len(text)):
    if i % 7 == 0:
        output += Red + text[i]
    elif i % 7 == 1:
        output += Orange + text[i]
    elif i % 7 == 2:
        output += Yellow + text[i]
    elif i % 7 == 3:
        output += Green + text[i]
    elif i % 7 == 4:
        output += Blue + text[i]
    elif i % 7 == 5:
        output += Indigo + text[i]
    elif i % 7 == 6:
        output += Violet + text[i]

# print everything as one string

print(output)