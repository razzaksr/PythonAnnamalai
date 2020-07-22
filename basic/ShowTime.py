from basic.OwnRaise import TheatreError

for each in range(5):
    try:
        tic_type = input("Typical/ fan base")
        if tic_type != "fan base":
            raise TheatreError
        else:
            print(each,"You got seat")
    except TheatreError as te:
        print(te,each)
        tic_type = input("Typical/ fan base")
        if tic_type != "fan base":
            print(each,"Chances are over")
        else:
            print(each,"You got seat")
