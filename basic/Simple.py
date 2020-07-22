'''
S e l e n i u m
S e l e n i u m
S e l e n i u m
S e l e n i u m
S e l e n i u m
S e l e n i u m
S e l e n i u m
S e l e n i u m
'''

word=input("Tell us word to print: ")
for row in range(len(word)):
    for col in range(len(word)):print(word[col],end=" ")
    print()

'''
S 
S e 
S e l 
S e l e 
S e l e n 
S e l e n i 
S e l e n i u 
S e l e n i u m
'''
for row in range(len(word)):
    for col in range(row+1):print(word[col],end=" ")
    print()

'''
S e l e n i u m
S e l e n i u 
S e l e n i 
S e l e n 
S e l e 
S e l 
S e 
S 
'''
for row in range(len(word),0,-1):
    for col in range(row):print(word[col],end=" ")
    print()