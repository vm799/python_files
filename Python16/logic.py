# design a program that has and shows a logical error
# a logical error is usually found with loops/control statements

cats = 4
dogs = 2
budgies = 6
toxic_spiders =3

is_my_home_a_zoo = False

if cats + dogs + budgies == 13:
    print("Yep, you are a zoo, you probably should start charging admission!")

elif toxic_spiders > -2:
    print("You may get bitten and become spiderman- Go Spidey!")
    
elif toxic_spiders == 3 and is_my_home_a_zoo == True:
    print("All good here Dr Dolittle")