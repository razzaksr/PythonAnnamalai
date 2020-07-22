# create and write the file

var=open("Annamalai.doc","a")
print(var.name)
print(var.mode)
ins=input("Tell us something to record: ")
var.write(ins)
var.close()
print(var.closed)

vary=open("C:/Users/DOLL/Desktop/PTest/Annamalai/Meguraj.txt","a")
vary.write("Hello megu")
vary.close()