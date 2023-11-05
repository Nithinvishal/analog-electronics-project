print("select the BJT configuration")
a=int(input("1.fixed bias 2.emitter bias 3. voltage divider bias 4.collector feedback "))
def bjt():
    if(a==1):
        print("enter the following values")
        Vcc=int(input(" enter Vcc value"))
        Rb=int(input(" enter Rb value"))
        beta=int(input(" enter beta value"))
        Rc=int(input(" enter Rc value"))
        b1= beta+1       
        Ib= ((Vcc-0.7)/Rb)*1000000      
        Ic= (beta*Ib)/1000
        Ie= b1*Ib
        Vcez= Ic*Rc
        Vce= Vcc-((Ic/1000)*Rc)
        return("the value of Ic",round(Ic,4),"milliampere",
               "the value of Ib",round(Ib,5),"microampere",
               "the value of Vce",round(Vce,3),"volt")
    elif(a==2):
        print("enter the following values")
        Vcc=float(input(" enter vcc value"))
        Rb=float(input(" enter Rb value"))
        Re=float(input(" enter Re value"))
        beta=float(input(" enter beta value"))
        Rc=float(input(" enter Rc value"))
        b1= beta+1         
        Ib= ((Vcc-0.7)/(Rb+(b1*Re)))*1000000      
        Ic= (beta*Ib)/1000
        Ie= (b1*Ib)/1000
        Vce= Vcc-((Ic/1000)*(Re+Rc))
        return("the value of Ic",round(Ic,4),"milliampere",
               "the value of Ib",round(Ib,5),"microampere",
               "the value of Vce",round(Vce,3),"volt") 
    elif(a==3):
        print("enter the following values")
        R1=float(input(" enter R1 value"))
        R2=float(input(" enter R2 value"))
        Vcc=float(input(" enter vcc value"))
        beta=float(input(" enter beta value"))
        Re=float(input(" enter Re value"))
        Rc=float(input(" enter Rc value"))
        b1= beta+1
        Rth= (R1*R2)/(R1+R2)
        Eth= (R2*Vcc)/(R1+R2)
        Ib= ((Eth-0.7)/(Rth+(beta*Re)))*1000000
        Ic= (beta*Ib)/1000
        Ie= (b1*Ib)/1000
        Vce= Vcc-((Ic/1000)*(Rc+Re))
        return("the value of Ic",round(Ic,4),"milliampere",
               "the value of Ib",round(Ib,5),"microampere",
               "the value of Vce",round(Vce,3),"volt") 
    elif(a==4):
        print("enter the following values")
        Vcc=float(input(" enter vcc value"))
        beta=float(input(" enter beta value"))
        Rb=float(input(" enter Rb value"))
        Re=float(input(" enter Re value"))
        Rc=float(input(" enter Rc value"))
        b1= beta+1
        Ib= ((Vcc-0.7)/(Rb+(beta*(Rc+Re))))*1000000
        Ic= (beta*Ib)/1000
        Ie= (b1*Ib)/1000
        Vce= (Vcc-(Ic/1000)*(Rc+Re))
        return("the value of Ic",round(Ic,4),"milliampere",
               "the value of Ib",round(Ib,5),"microampere",
               "the value of Vce",round(Vce,3),"volt")                  
    else:
         print("invaild input")
print(bjt())    
