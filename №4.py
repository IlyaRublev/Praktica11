a = 'In the hole in the ground there lived a hobbit'
a = a.replace('h','H', a.count('h')-1).replace('H', 'h', 1)
print(a)