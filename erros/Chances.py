# multiple chances
def upload(yet,times=2):
    if times>3:print("Chances are over");return
    else:
        try:
            file=open(yet,"r")
            print(file.read())
            return
        except IOError as io:
            print(io,"\nMention valid file")
            times+=1
            upload(input("tell us File name"),times)

upload(input("tell us File name"))