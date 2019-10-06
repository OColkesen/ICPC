import sys

def circuitmath():
    letters = ['A','B','C','D','E','F','G','H','I','J',
               'K','L','M','N','O','P','Q','R','S','T',
               'U','V','W','X','Y','Z']
    TF = []
    circuit = []
    nochange = ["*","+","-", True, False]
    
    f = sys.stdin
    contents =f.read()
    input_ = contents.split("\n")

    TF = input_[1].split()
    for i in range (len(TF)):
        if TF[i] == 'F':
            TF[i] = False
        else:
            TF[i] = True
    
    circuit = input_[2].split()
    for i in range (len(circuit)):
        if circuit[i] in letters:
            #getting the index of the letter in the 
            #alphabet and using that to find the letter's
            #boolean value
            index = letters.index(circuit[i])
            circuit[i] = TF[index]
    
    #if there's only one element, we want to print the
    #boolean value of that element.
    if len(circuit) == 1:
        if circuit[0] == False:
            print("F")
        else:
            print("T")
    
    else:
        i = 0
        while len(circuit) != 1:
            if circuit[i] == True or circuit[i] ==False:
                i += 1
                pass

            elif circuit[i] == '*':
                if circuit[i-1] and circuit[i-2]:
                    circuit[i] = True
                    circuit.pop(i-2)
                    circuit.pop(i-2)
                else:
                    circuit[i] = False
                    circuit.pop(i-2)
                    circuit.pop(i-2)
                i -= 1

            elif circuit[i] == '+':
                if circuit[i-1] or circuit[i-2]:
                    circuit[i] = True
                    circuit.pop(i-2)
                    circuit.pop(i-2)
                else:
                    circuit[i] = False
                    circuit.pop(i-2)
                    circuit.pop(i-2)
                i -= 1

            elif circuit[i] == '-':
                if circuit[i-1]:
                    circuit[i] = False
                    circuit.pop(i-1)
                else:
                    circuit[i] = True
                    circuit.pop(i-1)
                i -= 1
            
        if circuit[0] == False:
            print("F")
        else:
            print("T")
        
circuitmath()