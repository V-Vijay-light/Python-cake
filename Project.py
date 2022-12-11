
#N is taken as input for number of cake pieces
shape=int(input("Select chape of cake: 1.Round, 2.Square; "))
N=int(input("Number of pieces N = "))
print(" ")

#The function equal_size() is defined to find if the cake can be cut into equal pieces or not
if shape==1:
    def equal_size(n):
        if n%2==0:
            print("The cake can be cut into equal sized pieces")
            print(" ")
        else:
            print("The cake cannot be cut into equal sized pieces")
            print("Since the cake has to be cut from one end to the other end through the center the cake cannot be cut into odd numbered pieces")
            print(" ")
elif shape==2:
        def equal_size(n):
            if n%4==0 or n==2:
                print("The cake can be cut into equal sized pieces")
                print(" ")
            else:
                print("The cake cannot be cut into equal sized pieces")
                print("Since the cake has to be cut from one end to the other end through the center the cake cannot be cut into odd numbered pieces")
                print(" ")
else:
    print("Select Valid Shape")


#The cake can be cut into equal number of pieces for N is any positive even integer.

#The function any_size() is defined to find if the cake can be cut into pieces of any size or not
if shape==1 or shape==2:
    def any_size(n):
        if n%2==0:
            print("The cake can be cut into pieces any size")
            print(" ")
        else:
            print("The cake cannot be cut into pieces of any size")
            print("Since the cake has to be cut from one end to the other end through the center the cake cannot be cut into odd numbered pieces")
            print(" ")
else:
    pass

#The cake can be cut into pieces of any size for N is any positive even integer

#The function no_equal() is defined to find if the cake can be cut such that no two pieces are equal or not
if shape==1 or shape==2:        
    def no_equal(n):
        if n%2==0:
            print("It is not possible to cut the cake such that no two pieces are equal")
            print("NOTE:")
            print("Since the angles of the opposite cake pieces are vertically opposite angles the opposite pieces in the cake are equal")
        else:
            print("Since the cake has to be cut from one end to the other end through the center the cake cannot be cut into odd numbered pieces")
#The cake cannot be cut such that no two pieces are equal, because the angle of opposite cake pieces are vertically opposite angles. 

#The defined functions are called with N as input
        
equal_size(N)
any_size(N)
no_equal(N)
