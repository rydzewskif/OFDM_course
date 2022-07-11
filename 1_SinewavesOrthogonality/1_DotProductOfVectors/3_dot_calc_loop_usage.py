green = [ -1.23, -3.45]
blue  = [6.9,-2.46]

dot_product = 0
for i in range(len(green)): # i = 0,..len(green)-1 
    dot_product += green[i] * blue[i]

print(dot_product)

