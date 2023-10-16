from os import system


notes = "C C# D D# E F F# G G# A A# B"
notes = notes.split(' ')

Major = [2,2,1,2,2,2,1]
All = Major *3
Dorian = All[1:8]
Phrygian = All[2:9]
Lydian = All[3:10]
Mixolydian = All[4:11]
Minor = All[5:12]
Locrian = All[6:13]



def scaler(Scale):
    i=0 
    j=0
    tis = []
    while i in range(len(notes)):         #print(f'{j+1}. {notes[i]}')
         tis.append(notes[i])
         i=i+Scale[j]
         j=j+1
    return tis

def pArr(a):
    for i in range(len(a)):
        print(f'{i+1}. {a[i]}')

# pArr(scaler(Minor))

def ChordMaker4(Scale=Major,cp=[0,2,4,6], base=3,keys=7):
    #cp = chord pattern like 0,2,4,6 meaning 7th on base,   1) c e g b on first note c in Major 
    #                        0,2,4,8 meaning add9th         2) c d#g d on first note c in Minor   
    s = scaler(Scale) *3
    S = []
    #base = base key, noone wants to play on C1, C3 is gg for starters ig
    a=[base]*7 + [base+1]*7 + [base+2]*7
    for i in range(len(s)):
        S.append(str(s[i]) + str(a[i]))
    
    cs = 0

    for i in range(keys):
        print(f'{S[i+cp[0]]},{S[i+cp[1]]},{S[i+cp[2]]},{S[i+cp[3]]}\n')

# ChordMaker4(Locrian)

#cp list
sevenths = [0,2,4,6]
add9     = [0,2,4,8]
add11    = [0,2,4,10]
add69    = [0,2,5,8]
strong9  = [0,2,6,8]
wierd913 = [0,4,9,13]

# ChordMaker4 (Major,add9)

def FREE():
    print('FREE\n')

dCL =   [add11,add69,            
        sevenths,add9,
        sevenths,add9,
        strong9,wierd913]


def keyboardLayout(Scale=Major,CL=dCL):
    ChordMaker4(Scale,CL[0],4)
    ChordMaker4(Scale,CL[1],4,6)
    FREE()
    ChordMaker4(Scale,CL[2],4)
    ChordMaker4(Scale,CL[3],4,6)
    FREE()
    ChordMaker4(Scale,CL[4],3)
    ChordMaker4(Scale,CL[5],3,4)
    FREE()
    FREE()
    FREE()
    ChordMaker4(Scale,CL[6],4)
    ChordMaker4(Scale,CL[7],3,3)


# log = open("C:\Program Files\Image-Line\FL Studio 20\System\Config\Typing to piano\Chords\DorianDCL.scr", "a")
# log = open("C:\Program Files\Image-Line\FL Studio 21\System\Config\Typing to piano\PyChords\DorianDCL", "c")



log = open("C:\Program Files\Image-Line\FL Studio 21\System\Config\Typing to piano\PyChords\DorianDCL", "c")

print = log.write
keyboardLayout(Dorian)