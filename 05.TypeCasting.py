#int 
age=23
#str
name='Aaman'
#bool
human=True
#decimal
height=5.11

# convert int into str
print(str(age))
print(str(human))
print(str(height));

# convert decimal into int
print(int(height));

# convert bool into int
print(int(human))

# convert int into decimal
print(float(age))

# string does't convert into int or other type
# print(int(name)) ValueError: invalid literal for int() with base 10: 'Aaman'