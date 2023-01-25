# input() print() int() type()
# > < and <= == =
# str int

nb = input("Please enter a numeric value: ")

nb=int(nb)

while nb > 0:
    print("in the loop", nb)
    if nb > 10:
        nb = nb - 2
    else:
        nb = nb - 1
    
    
print('the end', nb)

