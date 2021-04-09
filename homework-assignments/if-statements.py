# Comparing input parameters
# Written by Franz A. Tapia Chaca
# on 13 January 2021

def AreTwoOrMoreEqual(par1, par2, par3):
    equality = False

    if type(par1) == str:
        # print(par1)           # Commented lines to check type conversion
        # print(type(par1))
        par1 = int(par1)
        # print(type(par1))
    elif type(par2) == str:
        # print(par2)
        # print(type(par2))
        par2 = int(par2)
        # print(type(par2))
    elif type(par3) == str:
        # print(par3)
        # print(type(par3))
        par3 = int(par3)
        # print(type(par3))

    # if 2 or more values are equal, equality = True
    if par1 == par2 or par1 == par3 or par2 == par3:
        equality = True
    return equality


print(AreTwoOrMoreEqual(6, 5, "5"))
