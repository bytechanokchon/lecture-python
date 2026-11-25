# List
numbers = [1, 2, 3, 4, 5, 6]
print(numbers)

# List indexing
numbers = [1, 2, 3, 4, 5, 6]
print(numbers[0])  # Output: 1
print(numbers[5])  # Output: 6
print(numbers[-1])
print(numbers[-3:])

# List concatenation
numbers = [1, 2, 3, 4, 5, 6]
new_numbers = numbers + [7, 8, 9]
print(new_numbers)

# List append
numbers = [1, 2, 3, 4, 5, 6]
numbers.append(7)
numbers.append(8)
print(numbers)

# List assignment
rgb = ["Red", "Green", "Blue"]
rgba = rgb
rgba.append("Alpha")
print(rgb)  # Output: ['Red', 'Green', 'Blue', 'Alpha']

# List copy
rgb = ["Red", "Green", "Blue"]
rgba = rgb[:]
rgba.append("Alpha")
print(rgba)  # Output: ['Red', 'Green', 'Blue', 'Alpha']
print(rgb)   # Output: ['Red', 'Green', 'Blue']

# List slicing
letters = ["a", "b", "c", "d", "e", "f"]
letters[2:4] = ["C", "D"]
print(letters)  # Output: ['a', 'b', 'C', 'D', 'e', 'f']

letters[2:4] = []
print(letters)  # Output: ['a', 'b', 'e', 'f']

letters[:] = []
print(letters)  # Output: []

# List len()
numbers = [1, 2, 3, 4, 5, 6]
print(len(numbers))  # Output: 6

# Nested list
a = [1, 2, 3]
b = [4, 5, 6]
x = [a, b]
print(x)  # Output: [[1, 2, 3], [4, 5, 6]]
print(x[0])  # Output: [1, 2, 3]
print(x[1][2])  # Output: 6