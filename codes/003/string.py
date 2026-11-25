name = "Python"
message = "Hello World"
print(name)
print(message)

# Escape character
print("Hello\nPython")

# Raw string
print(r"C:\this\name")

# Multi-line string
message = """Hello
Welcome to Python
Happy Coding!"""
print(message)

# String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

print(first_name * 3)

message = "Py" "thon"
print(message)

# String indexing
message = "Python"
print(message[0])  # Output: P
print(message[5])  # Output: n

print(message[-1])  # Output: n
print(message[-6])  # Output: P

# String slicing
message = "Python"
print(message[0:3])  # Output: Pyt
print(message[:2])
print(message[4:])
print(message[-2:])
print("J" + message[1:])

# Len
message = "Python"
print(len(message))  # Output: 6