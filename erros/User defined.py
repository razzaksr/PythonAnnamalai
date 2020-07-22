# raise user defined error
from erros.OwnError import AnnamalaiError

try:
    pas = input("Set the password")
    con = input("Confirm password")
    if pas != con:
        raise AnnamalaiError
    else:
        print("Password was set successfully")
except AnnamalaiError as an:
    print(an)
    pas = input("Set the password")
    con = input("Confirm password")
    if pas==con:print("Password was set successfully")
    else:print("Chances are over")