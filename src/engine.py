# ENIGMA MACHINE I - WEHRMACHT(5 ROTORS) and KREIGSMARINE(8 ROTORS) VARIANT - 1940
# 5 ROTORS (I,II,III,IV,V) -- 8 ROTORS (I,II,III,IV,V,VI,VII,VIII)
# 2 REFLECTORS (B,C)
# PLUGBOARD
import msvcrt
import os
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
    rotor_VI=[alphabet[:],['J','P','G','V','O','U','M','F','Y','Q','B','E','N','H','Z','R','D','K','A','S','X','L','I','C','T','W']]
    rotor_VII=[alphabet[:],['N','Z','J','H','G','R','C','X','M','Y','S','W','B','O','U','F','A','I','V','L','P','E','K','Q','D','T']]
    rotor_VIII=[alphabet[:],['F','K','Q','H','T','L','X','O','C','B','J','S','P','D','Z','R','A','M','E','W','N','I','U','Y','G','V']]
    reflector_B=[alphabet[:],['Y','R','U','H','Q','S','L','D','P','X','N','G','O','K','M','I','E','B','F','Z','C','W','V','J','A','T']]
    reflector_C=[alphabet[:],['F','V','P','J','I','A','O','Y','E','D','R','Z','X','W','G','C','T','K','U','Q','S','B','N','M','H','L']]

    plugBoard=[]            #default plugboard = null
    rotorsInstall=[1,2,3]   #default rotor installation I II III from left to right
    rotorsRing=[1,1,1]      #default rotor ring setting from left to right
    rotorsSetting=[1,1,1]   #default rotor setting from left to right
    reflector=reflector_B   #default reflector to B

    reflectors=[reflector_B,reflector_C]
    rotors=[rotor_I,rotor_II,rotor_III,rotor_IV,rotor_V,rotor_VI,rotor_VII,rotor_VIII]
    rotorTurnover=['QQ','EE','VV','JJ','ZZ','ZM','ZM','ZM']

    # calculate rotor configuration from right to left for encryption
    # ROTOR DISPLAYS ARE FROM LEFT TO RIGHT!!!!
    rotor1=rotors[rotorsInstall[2]-1]
    rotateRotor(rotor1,rotorsSetting[2]-1)      #rotor1 up (rotorsSetting[2]-1)times
    rotateRotor(rotor1,-(rotorsRing[2]-1))      #rotor1 down (rotorsRing[2]-1)times
    rotor3Display=rotorsSetting[2]
    rotor2=rotors[rotorsInstall[1]-1]
    rotateRotor(rotor2,rotorsSetting[1]-1)      #rotor2 up (rotorsSetting[1]-1)times
    rotateRotor(rotor2,-(rotorsRing[1]-1))      #rotor2 down (rotorsRing[1]-1)times
    rotor2Display=rotorsSetting[1]
    rotor3=rotors[rotorsInstall[0]-1]
    rotateRotor(rotor3,rotorsSetting[0]-1)      #rotor3 up (rotorsSetting[0]-1)times
    rotateRotor(rotor3,-(rotorsRing[0]-1))      #rotor3 down (rotorsRing[0]-1)times
    rotor1Display=rotorsSetting[0] 
    globals().update(locals())

def rotateRotor(R,s):
    #A-->B-->C rotate up
    if s<0: s=26+s          #make s positive, example: s=-3 ---> s=23 (-3 steps <==> +23 steps)
    for k in range(s):
        first0=R[0][0]
        first1=R[1][0]
        for i in range(25):
            R[0][i]=R[0][i+1]
            R[1][i]=R[1][i+1]
        R[0][25]=first0
        R[1][25]=first1

def reducedOrd(x):
    return ord(x)-65

def charFromReducedOrd(x):
    return chr(x+65)

def setRotorsInstall(rotor,selection):      # from left to right
    global rotor1,rotor2,rotor3
    rotorsInstall[rotor]=selection + 1
    rotor1=rotors[rotorsInstall[2]-1]
    rotor2=rotors[rotorsInstall[1]-1]
    rotor3=rotors[rotorsInstall[0]-1]
    
    
def setRotorsSetting(rotor,s):              # from left to right
    global rotor1Display, rotor2Display, rotor3Display
    if rotor==0:
        rotateRotor(rotor3,s)
        rotor1Display=(rotor1Display -1 + s) % 26 + 1
    elif rotor==1:
        rotateRotor(rotor2,s)
        rotor2Display=(rotor2Display -1 + s) % 26 + 1
    elif rotor==2:
        rotateRotor(rotor1,s)
        rotor3Display=(rotor3Display -1 + s) % 26 + 1

def setRotorsRing(rotor,s): # from left to right
    if rotor==0:
        rotateRotor(rotor3,-s)
    elif rotor==1:
        rotateRotor(rotor2,-s)
    elif rotor==2:
        rotateRotor(rotor1,-s)

def setReflector(r):
    global reflector
    reflector=reflectors(Ord(r)-66) # 'B' is ord->66

def advanceRotors(r1,r2,r3): # from right to left
    global rotor1Display, rotor2Display, rotor3Display
    t11=reducedOrd(rotorTurnover[rotorsInstall[2]-1][0])+1 # farmost right rotot's turnover position
    t12=reducedOrd(rotorTurnover[rotorsInstall[2]-1][1])+1 # farmost right rotot's turnover position
    t21=reducedOrd(rotorTurnover[rotorsInstall[1]-1][0])+1 # middle rotot's turnover position
    t22=reducedOrd(rotorTurnover[rotorsInstall[1]-1][1])+1 # middle rotot's turnover position
    if rotor2Display==t21 or rotor2Display==t22:
        rotateRotor(r2,1)
        rotor2Display=rotor2Display % 26 + 1
        rotateRotor(r3,1)
        rotor1Display=rotor1Display % 26 + 1
    elif rotor3Display==t11 or rotor3Display==t12:
        rotateRotor(r2,1)
        rotor2Display=rotor2Display % 26 + 1
    rotateRotor(r1,1)
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
    encryptedChar=charFromReducedOrd(exitPosition1)
    encryptedChar=charFromPlugBoard(encryptedChar)
    return encryptedChar

def encryptPhrase(text):
    text=text.upper()
    out=''
    k=0
    for i in range(len(text)):
        if text[i] in alphabet:
            if k % 4 == 0 and i!=0 : out+=' '
            out+=encryptChar(text[i])
            k+=1
    return out

# MAIN PROGRAM    
initialize()
if __name__=='__main__':
    phrase=input('enter message:')
    print(encryptPhrase(phrase))
    os.system("pause")

