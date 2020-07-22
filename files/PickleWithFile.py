# Pickling and unpickling
import pickle as pik

drives={1000:['sony','hp'],500:['transcend','sandisk'],2000:['Hp','toshiba','iBall'],
        700:'Sony',2100:['Hp','micromax']}
#pickle
megu=open("Hari.txt","ab")
pik.dump(drives,megu)
megu.close()

megu=open("Hari.txt","rb")
for hai,bye in pik.load(megu).items():
        print(hai,bye)
megu.close()