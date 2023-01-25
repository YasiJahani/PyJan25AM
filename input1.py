# input() print() int() type()
# > < and <= == =
# str int

nb = input("Please enter a numeric value: ")

print(nb, type(nb))
nb=int(nb)
print(nb, type(nb))

if nb > 0 and nb < 100: # < <= > >= == != and or not
    print("nb in ]0,100[")  
    nb = nb - 1
elif nb <= 0:
    print("nb <= 0")
elif nb == 100:
    print("nb == 100")  
else:
    print("nb > 100")
    
print('the end', nb)

