#C:\Users\DOLL\Desktop\PTest\Annamalai\fileprobs.txt
try:
    hai = open(input("Locate the file along with address: "), "r")
    data = hai.read()
    cnt = data.count(' ') + 1
    print(cnt)
except IOError as oi:
    print(oi)
    hai = open(input("Locate the file along with address: "), "r")
    data = hai.read()
    cnt = data.count(' ') + 1
    print(cnt)
else:hai.close()