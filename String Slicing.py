# Example String
txt = "Hello, Python!"

# String Indexing
print("Original String:", txt)
print("First Character:", txt[0])   # H
print("Last Character:", txt[-1])  # !
print("Fifth Character:", txt[4])  # o

# String Slicing
print("Substring from index 0 to 5:", txt[0:5])  # Hello
print("Substring from index 7 to end:", txt[7:])  # Python!
print("Substring from start to index 5:", txt[:5])  # Hello
print("Substring with step 2:", txt[::2])  # Hlo Pto!
print("Reverse the string:", txt[::-1])  # !nohtyP ,olleH
