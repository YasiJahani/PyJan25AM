

nb=12
# "Nb is 12 nb*10 is 120"

text=f"Nb is {nb} nb*10 is {nb*10}" # >= 3.6

print(text)

text="Nb is {} nb*10 is {}".format(nb, nb*10) # >=2.5

print(text)

text="Nb is %d nb*10 is %d" % (nb, nb*10) # deprecated

print(text)


