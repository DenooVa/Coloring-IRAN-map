class colour:
    def __init__(self):
        self.g = 1
        self.r = 1
        self.b = 1
        self.y = 1
        self.colour = "none"
    def setname(self,name):
        self.name = name
    def setcolourg(self):
        self.g = 1
        self.r = 0
        self.b = 0
        self.y = 0
        self.colour = "g"
    def setcolourr(self):
        self.g = 0
        self.r = 1
        self.b = 0
        self.y = 0
        self.colour = "r"
    def setcolourb(self):
        self.g = 0
        self.r = 0
        self.b = 1
        self.y = 0
        self.colour = "b"
    def setcoloury(self):
        self.g = 0
        self.r = 0
        self.b = 0
        self.y = 1
        self.colour = "y"
    def delcolourg(self): 
        self.g = 0
    def delcolourr(self):
        self.r = 0
    def delcolourb(self):
        self.b = 0
    def delcoloury(self):
        self.y = 0
#END OF CLASS COLOUR
####################
class hamsaye(colour):
    def inserttedad(self,n):
        self.tedad = n
        self.hamsayeha = []
    def insertnames(self,name):
            self.hamsayeha.append(name)
#END OF CLASS HAMSAYE
#####################
#main program

ox = []
#name of ostanha
ostanha = ["azg","azs","zan","kord","ard","gil","gaz","hamd","kermanshah","maz","teh","mark","lor","il","qom","khuz","alb",
           "4mahal","kohkil","esf","sem","gol","bush","fars","yazd","hormoz","kerman","systan","khr","khs","khg"]
#tedad hamsayeha
ot = [3,3,7,4,3,4,6,6,4,6,5,7,7,3,4,5,5,
      4,5,8,8,3,4,6,6,4,5,3,4,3,4]
#hamsayehaye ostan ha
#####################
i=0
while(i<31):
    ostan = hamsaye()
    ostan.setname(ostanha[i])
    ostan.inserttedad(ot[i])
    ox.append(ostan)
    i=i+1
#end of whille
##############
#list hamsayeha    
mo = ["azs","zan","kord",#3 azg 
      "azg","zan","ard",#3 azs 
      "hamd","kord","gaz","gil","ard","azs","azg",#7 zan 
      "kermanshah","hamd","zan","azg",#4 kord
      "gil","zan","azs",#3 ard
      "maz","gaz","zan","ard",#4 gil
      "hamd","mark","alb","maz","gil","zan",#6 gaz
      "lor","mark","gaz","zan","kord","kermanshah",#6 hamd
      "kord","hamd","lor","il",#4 kermanshah
      "gil","gaz","teh","sem","gol","alb",#6 maz
      "mark","maz","sem","alb","qom",#5 teh
      "lor","esf","qom","teh","gaz","hamd","alb",#7 mark
      "khuz","4mahal","esf","mark","hamd","kermanshah","il",#7 lor
      "kermanshah","lor","khuz",#3 il
      "esf","mark","sem","teh",#4 qom
      "bush","kohkil","4mahal","il","lor",#5 khuz
      "qom","mark","teh","maz","gaz",#5 alb
      "esf","kohkil","lor","khuz",#4 4mahal
      "bush","fars","esf","4mahal","khuz",#5 kohkil
      "kohkil","4mahal","lor","mark","qom","sem","yazd","fars",#8 esf
      "esf","qom","teh","maz","gol","khs","khr","yazd",#8 sem
      "khs","sem","maz",#3 gol
      "hormoz","fars","kohkil","khuz",#4 bush
      "bush","hormoz","kerman","yazd","esf","kohkil",#6 fars
      "fars","kerman","khr","khg","sem","esf",#6 yazd
      "fars","bush","kerman","systan",#4 hormoz
      "hormoz","systan","khg","yazd","fars",#5 kerman
      "hormoz","kerman","khg",#3 systan
      "sem","khs","khg","yazd",#4 khr
      "khr","sem","gol",#3 khs
      "systan","kerman","yazd","khr"]#4 khg
#####################################
i=0
j=0
k=0
while(k<31):
    j += ot[k]
    while(i<j):
        ox[k].insertnames(mo[i])
        i+=1
    k+=1 
#end of while
####################################
on = []
on = ot
j=0
t=0
while t<31:
    while j<31:   
        m = max(on)
        o1 = on.index(m)
        n1 = ox[o1].name
        h1 = ox[o1].hamsayeha
        i=0
        colour = []
################begin    
        while(i<31):
            if ox[i].name in h1:
                colour.append(ox[i].colour)
            i+=1
################end        
        if "g" in colour :
            ox[o1].delcolourg()
        else:
            ox[o1].setcolourg()
            on[o1] = 0
            j+=1
            break
#################
        if "r" in colour :
            ox[o1].delcolourr()
        else:
            ox[o1].setcolourr()
            on[o1] = 0
            j+=1
            break
#################
        if "b" in colour :
            ox[o1].delcolourb()
        else:
            ox[o1].setcolourb()
            on[o1] = 0
            j+=1
            break
#################
        if "y" in colour :
            ox[o1].delcoloury()
        else:
            ox[o1].setcoloury()
            on[o1] = 0
            j+=1
            break
#################
        on[o1] = 0
        j+=1
    t+=1    
#################
k=0
while k<31 :
    print("name is :",ox[k].name , " & colour is" , ox[k].colour)
    k+=1




    
    

        
