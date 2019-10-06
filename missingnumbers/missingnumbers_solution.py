import sys

def find_missing():
    correct = []
    kids_counting = []
    missing = []
    
    filename = input()
    
    f = sys.stdin
    contents =f.read()
    kids_counting = contents.split()
    
    for i in range (1, int(kids_counting[-1])):
        correct.append(str(i))
        
    for i in correct:
        if i not in kids_counting:
            missing.append(i)
    
    if len(missing) == 0:
        print ("good job")
        
    for i in missing:
        print (i)
        
find_missing()