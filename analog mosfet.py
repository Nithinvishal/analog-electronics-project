print("selection the configuration of MOSFET(depletion)")
b=int(input(" 1.fixed bias 2. voltage divider bias"))
def mosfet():
        if(b==1):
                print("enter the following values")
                Vgg=float(input("enter the Vgg value"))
                Idss=float(input("enter the Idss value in ampere only"))
                Vp=float(input("enter the Vp value"))
                Vdd=float(input("enter the Vdd value"))
                Rd=float(input("enter the Rd value"))
                Vgs= -Vgg
                Id= (Idss*((1-(Vgs/Vp))*(1-(Vgs/Vp))))*1000
                Vds= Vdd-((Id/1000)*Rd)
                return("the value of Vgs",round(Vgs,4),"volt",
               "the value of Id",round(Id,5),"milliampere",
               "the value of Vds",round(Vds,3),"volt") 

        elif(b==2):
                print("enter the following values")
                R1=float(input("enter the R1 value"))
                R2=float(input("enter the R2 value"))
                Vdd=float(input("enter the Vdd value"))
                Rs=float(input("enter the Rs value"))
                Rd=float(input("enter the Rd value")) 
                Vp=float(input("enter the Vp value"))
                Idss=float(input("enter the Idss value in ampere only"))
                Vgs=float(input("enter the Vgs value"))
                Vg= (R2*Vdd/(R1+R2))
                
                Id= (Idss*((1-(Vgs/Vp))*(1-(Vgs/Vp))))*1000
                Vds= Vdd-(Id/1000)*(Rd+Rs)
                return("the value of Vgs",round(Vgs,4),"volt",
               "the value of Id",round(Id,5),"milliampere",
               "the value of Vds",round(Vds,3),"volt",
               "the value of Vg",round(Vg,3))
        else:
                print("invalid input")
print(mosfet())        
     
                
                   
        
