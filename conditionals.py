# Conditionals

x = 4

# Basic If
# indentation for code blocks

if x < 6:
    print("this is true")

# if else

if x > 11:
    print("this is true")
else:
    print("this is false")

# elif
color = "red"
if color == 'red':
    print("color is red")
elif color == "blue":
    print("color is blue")
else:
    print("color is neither red nor blue")

# nest if statments

if color == "red":
    if x < 10:
        print("TRUE")

# but its better practice to use logical operators

if color == "red" and x < 10:
    print("DERP")