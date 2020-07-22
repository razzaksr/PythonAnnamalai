
class Projects:
    "This class refers resource person"
    def __init__(self):self.__name="";self.__domain=[]
    def show(self):
        print(self.__name, " has done projects of following")
        for all in self.__domain:
            print(all)
    def setting(self,nm="",org=[]):
        self.__name=nm
        self.__domain=org


print(Projects.__doc__)
print(Projects.__name__)

p1 = Projects()
p1.setting("Annamalai",["Java","Python","C++"])

p2 = Projects()
p2.setting("Raji",["Python","C"])

p2.show()
p1.show()