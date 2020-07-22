class Hall:
    "Party Hall"
    hallType=""

print(Hall.__doc__)
h1=Hall()
setattr(h1,"location","Fairlands")
setattr(h1,"seats",90)
h1.hallType="AC"
print(h1.location,h1.seats,getattr(h1,'hallType'))
delattr(h1,'seats')
print(h1.location,hasattr(h1,'seats'),getattr(h1,'hallType'))

h2=Hall()
h2.hallType="Non-AC"
print(h2.hallType)

delattr(h2,'hallType')
print(hasattr(h2,'hallType'))
print("verifying ",getattr(h2,'hallType'))