# function with default argument

# def fun_Name(parameter='')

def register(name,location,prefix="Mr/Miss/Mrs"):
    if location == 'Salem': print(prefix,name," has approved in ",location)
    elif location == 'Chennai':
        print(prefix,name," has gone under waiting state since its ",location)
    else: print("Business not approved")

register("Zealous Tech Corp","Salem")
register("Annamalai automobiles","Chennai","Mr.")
