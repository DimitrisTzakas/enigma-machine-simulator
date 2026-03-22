# ENIGMA MACHINE I - WEHRMACHT VARIANT - 1940
# 5 ROTORS (I,II,III,IV,V)
# 2 REFLECTORS (B,C)
# PLUGBOARD

def charFromPlugBoard(x):
    L=[[],[]]
    for i in range(len(plugBoard)):
        L[0].append(plugBoard[i][0])
        L[1].append(plugBoard[i][1])
    if x in L[0]:
        x=L[1][L[0].index(x)]
    elif x in L[1]:
        x=L[0][L[1].index(x)]
    return x

#'AV','BS','CG','DL','FU','HZ','IN','KM','OW','RX'  SAMPLE PLUGSETTINGS

def initialize():
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    rotor_I=[alphabet[:],['E','K','M','F','L','G','D','Q','V','Z','N','T','O','W','Y','H','X','U','S','P','A','I','B','R','C','J']]
    rotor_II=[alphabet[:],['A','J','D','K','S','I','R','U','X','B','L','H','W','T','M','C','Q','G','Z','N','P','Y','F','V','O','E']]
    rotor_III=[alphabet[:],['B','D','F','H','J','L','C','P','R','T','X','V','Z','N','Y','E','I','W','G','A','K','M','U','S','Q','O']]
    rotor_IV=[alphabet[:],['E','S','O','V','P','Z','J','A','Y','Q','U','I','R','H','X','L','N','F','T','G','K','D','C','M','W','B']]
    rotor_V=[alphabet[:],['V','Z','B','R','G','I','T','Y','U','P','S','D','N','H','L','X','A','W','M','J','Q','O','F','E','C','K']]
    reflector_B=[alphabet[:],['Y','R','U','H','Q','S','L','D','P','X','N','G','O','K','M','I','E','B','F','Z','C','W','V','J','A','T']]
    reflector_C=[alphabet[:],['F','V','P','J','I','A','O','Y','E','D','R','Z','X','W','G','C','T','K','U','Q','S','B','N','M','H','L']]

    plugBoard=[]   #default plugboard = null
    rotorsInstall=[2,4,5]  #default rotor installation I II III from left to right
    rotorsRing=[2,21,12]     #default rotor ring setting from left to right
    rotorsSetting=[2,12,1]  #default rotor setting from left to right
    reflector=reflector_B  #default reflector to B

    reflectors=[reflector_B,reflector_C]
    rotors=[rotor_I,rotor_II,rotor_III,rotor_IV,rotor_V]
    rotorTurnover=['Q','E','V','J','Z']

    # calculate rotor configuration from right to left for encryption
    # ROTOR DISPLAYS ARE FROM LEFT TO RIGHT!!!!
    rotor1=rotors[rotorsInstall[2]-1]
    for i in range(rotorsSetting[2]-1): rotateRotorUp(rotor1)
    for i in range(rotorsRing[2]-1): rotateRotorDown(rotor1)
    rotor3Display=rotorsSetting[2]
    rotor2=rotors[rotorsInstall[1]-1]
    for i in range(rotorsSetting[1]-1): rotateRotorUp(rotor2)
    for i in range(rotorsRing[1]-1): rotateRotorDown(rotor2)
    rotor2Display=rotorsSetting[1]
    rotor3=rotors[rotorsInstall[0]-1]
    for i in range(rotorsSetting[0]-1): rotateRotorUp(rotor3)
    for i in range(rotorsRing[0]-1): rotateRotorDown(rotor3)
    rotor1Display=rotorsSetting[0]
    globals().update(locals())

def rotateRotorUp(R): #A-->B-->C
    first0=R[0][0]
    first1=R[1][0]
    for i in range(25):
        R[0][i]=R[0][i+1]
        R[1][i]=R[1][i+1]
    R[0][25]=first0
    R[1][25]=first1

def rotateRotorDown(R): #C-->B-->A
    last0=R[0][25]
    last1=R[1][25]
    for i in range(25,-1,-1):
        R[0][i]=R[0][i-1]
        R[1][i]=R[1][i-1]
    R[0][0]=last0
    R[1][0]=last1

def reducedOrd(x):
    return ord(x)-65

def charFromReducedOrd(x):
    return chr(x+65)

def setRotorsInstall(r1,r2,r3): # from left to right
    global rotorsInstall
    rotorsInstall=[r1,r2,r3]
    
def setRotorsSetting(s1,s2,s3): # from left to right
    global rotorsSetting
    rotorsSetting=[s1,s2,s3]

def setRotorsRing(s1,s2,s3): # from left to right
    global rotorsRing
    rotorsRing=[s1,s2,s3]

def setReflector(r):
    global reflector
    reflector=reflectors(Ord(r)-66) # 'B' is ord->66

def advanceRotors(r1,r2,r3): # from right to left
    global rotor1Display, rotor2Display, rotor3Display
    t1=reducedOrd(rotorTurnover[rotorsInstall[2]-1])+1 # farmost right rotot's turnover position
    t2=reducedOrd(rotorTurnover[rotorsInstall[1]-1])+1 # middle rotot's turnover position
    if rotor2Display==t2:
        rotateRotorUp(r2)
        rotor2Display=rotor2Display % 26 + 1
        rotateRotorUp(r3)
        rotor1Display=rotor1Display % 26 + 1
    elif rotor3Display==t1:
        rotateRotorUp(r2)
        rotor2Display=rotor2Display % 26 + 1
    rotateRotorUp(r1)
    rotor3Display=rotor3Display % 26 + 1
    
def encryptChar(x):
    x=charFromPlugBoard(x)
    advanceRotors(rotor1,rotor2,rotor3)
    # encrypt from right to left
    charAtEnentryPosition1=rotor1[1][reducedOrd(x)]
    exitPosition1=rotor1[0].index(charAtEnentryPosition1)
    charAtEnentryPosition2=rotor2[1][exitPosition1]
    exitPosition2=rotor2[0].index(charAtEnentryPosition2)
    charAtEnentryPosition3=rotor3[1][exitPosition2]
    exitPosition3=rotor3[0].index(charAtEnentryPosition3)
    # bounce off the reflector
    charAtReflectrorEntryPosition=reflector[1][exitPosition3]
    exitReflectorPosition=reflector[0].index(charAtReflectrorEntryPosition)
    # encrypt fron left to right
    charAtEnentryPosition3=rotor3[0][exitReflectorPosition]
    exitPosition3=rotor3[1].index(charAtEnentryPosition3)
    charAtEnentryPosition2=rotor2[0][exitPosition3]
    exitPosition2=rotor2[1].index(charAtEnentryPosition2)
    charAtEnentryPosition1=rotor1[0][exitPosition2]
    exitPosition1=rotor1[1].index(charAtEnentryPosition1)
    encryptedX=charFromReducedOrd(exitPosition1)
    return charFromPlugBoard(encryptedX)

# MAIN PROGRAM    
initialize()
'''
phrase=raw_input('enter message:').upper()
out=''
for i in range(len(phrase)):
    if i % 5 == 0 and i!=0 : out+=' '
    out+=encryptChar(phrase[i])
print out
'''
