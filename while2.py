# input() print() int() type()
# > < and <= == =
# str int

nb = input("Please enter a numeric value: ")

nb=int(nb)

while True:
    print("in the loop", nb)
    nb = nb - 1
    if nb == 0:
        break
    
    
print('the end', nb)

