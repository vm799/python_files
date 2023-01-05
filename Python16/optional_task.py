# write and create a program that has 2 compilation errors
#   create a logical error and a runtime error

person = ("giant")
heads = "303"
head_count = heads[2]
worrying_head_count = int(head_count)
print(worrying_head_count)

print("My name is {Dave} and I'm a (person) and I have {head_count} heads")

if worrying_head_count > 4 and worrying_head_count - 5 == 0:
    print("YOU MUST RUN NOW!!!!") 
elif worrying_head_count == 1:
    print("You got this, take each head at a time!  ")
