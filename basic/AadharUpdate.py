# updating aadhar
from basic.OwnRaising import InvalidProofError

base={96775292:{"aadharNum":987667876,"name":"Razak","address":"Ponnammapet"},
      9876567876:{"aadhar":876567678,"name":"Raji","address":"Vincent"},
      567456776:{"aadhar":8765456776,"name":"annamalai","address":"Gugai"}}
proofs=["driving license", "Family card", "EB bill", "Gas booking"]

try:
    mob = int(input("Tell us mobile number: "))
    newad = input("Tell us new address")
    auth = input("Tell us address proof")
    if auth in proofs:
        base[mob]["address"] = newad
        print("Aadhar updated")
    else:
        print("Not updated")
except ValueError as ve:
    try:
        print(ve, "\nenter only numeric")
        mob = int(input("Tell us mobile number: "))
        newad = input("Tell us new address")
        auth = input("Tell us address proof")
        if auth in proofs:
            base[mob]["address"] = newad
            print("Aadhar updated")
    except KeyError as key:
        try:
            print(key)
            mob = int(input("Tell us mobile number: "))
            newad = input("Tell us new address")
            auth = input("Tell us address proof")
            if auth in proofs:
                base[mob]["address"] = newad
                print("Done")
            else:raise InvalidProofError
        except InvalidProofError as inv:
            print(inv)
            auth = input("Tell us address proof")
            if auth in proofs:
                base[mob]["address"] = newad
                print("Done")
            else:
                raise InvalidProofError