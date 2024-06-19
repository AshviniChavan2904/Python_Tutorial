#Here we will learn python for performing arithmatic operations
print(2+2)
print(3/2)  #Floating point division
print(3//2) #Integer division
print(5-2)
print(3*9)
print(2**3) #To calculate exponent
print(2**0.5) #To find square root multiply by0.5
print(3%2) #Calculates modulo means provides remainder value
print(round(2**0.5,2))

#Precedece rule
#Parenthesis>Exponent>*,/,//,%>+,-
#Parenthesis>Exponent(**) - R-L associativity
#*,/,//,% > +,- : Same precedence - Associativity is from L-R means we calculate from L-R
print((2+4)*3)
# (2+4)*3=6*3=18
print((8*2)/4*2%2)
# (8*2)/4*2%2 = 16/4*2%2 - Calculate from L-R as per associativity rule
# 16/4*2%2 = 4.0*2%2 = 8.0%2 = 0.0 # Here integer division is used hence we got answer in int format
