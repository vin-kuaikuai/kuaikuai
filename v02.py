#define function
def basic(parameter,filename):
    with open(filename) as fx:
        Htext=fx.read()
        chars=len(Htext)
        sentence=0
        danci=0
        words= Htext.split()
        danci=len(words)
        for ch in Htext:
            if (ch=='.'):
                sentence=sentence+1
        if parameter=='c':
            return chars
        elif parameter=='w':
            return danci
        elif parameter=='s':
            return sentence
parameter=input("parameter is:")
print
filename=input("filename is:")
print
a=basic(parameter,filename)
print(a)
parameter=input("parameter is:")
print
filename=input("filename is:")
print
b=basic(parameter,filename)
print(b)
parameter=input("parameter is:")
print
filename=input("filename is:")
print
c=basic(parameter,filename)
print(c)

