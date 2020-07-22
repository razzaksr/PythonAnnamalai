# basic function
#define
def greet():
    ans=input("Tell us ur desired city: ")
    if ans == 'Chennai': print("Too dangerous to live to now")
    elif ans == 'Salem': print("Safe to go out")
    elif ans == 'Villupuram': print("Don't ever think to go")
    else: print("Stay where you are")

def ask(purpose):
    if purpose == 'Economy': print("Don't worry everything sold to corporate")
    elif purpose == 'Health': print("That's state govt business")
    elif purpose == 'Relief': print("lift the light")
    else: print('Bharat matha ki jay')

def prompt(qual,ref):
    if qual == 'ug' and ref == 'HR':print("You are in UK team")
    elif qual == 'diploma' and ref == 'TestLead':print("Test Associate")
    elif qual == 'engg': print("Get off here")
    else:print("You are hired")

# call
prompt('engg','Project Manager')
prompt('ug','HR')
prompt(ref='TestLead',qual='diploma')
#greet()
#ask('Health')
#ask('Economy')
#ask('Women safety')