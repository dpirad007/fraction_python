class fraction(object):
    def __init__(self,num,deno):
        assert type(num)==int and type(deno)==int
        self.num=num
        self.deno=deno
    def __str__(self):
        return str(self.num)+"/"+str(self.deno)
    def __add__(self,other):
        top=self.num*other.deno+self.deno*other.num
        bot=self.deno*other.deno
        return fraction(top,bot)#returns the fraction as a frcation object so that the same methods can be used for the new fraction 
    def __sub__(self,other):
        top=self.num*other.deno-self.deno*other.num
        bot=self.deno*other.deno
        return fraction(top,bot)
    def __float__(self):
        return self.num/self.deno
    def inverse(self):
        return fraction(self.deno,self.num)
a=fraction(1,4)
b=fraction(3,4)
c=a+b
print(c)
print(float(c))
print(fraction.__float__(c))#same as above but calls class...then float...then passes c
print(b.inverse())#this is like that list.append() statement 
    