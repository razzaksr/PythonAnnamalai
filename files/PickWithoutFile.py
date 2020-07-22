# pickling/ unpickling without file
#from pickle import *
import pickle as pic
stu={'annamalai':'python','meguraj':11000,7000:'Core Python',8000:'java',7000:'JavaEE'}
# pickle
data=90
hai=pic.dumps(data)
print(hai)
greet=pic.dumps(stu)
print(greet)
#unpickle
print(pic.loads(hai))
for an,ban in pic.loads(greet).items():
    print(an,ban)