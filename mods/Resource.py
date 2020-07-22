# resource where the models and spec stored

models={}

def report():
    for x,y in models.items():
        print(x,y)
def filter(min=0,max=0):
    print("Showing results between",min,"and",max)
    for x,y in models.items():
        if y>=min and y<=max:print(x,y)

