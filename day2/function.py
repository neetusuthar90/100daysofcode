# # Define function
# def fun(name,age):
#     print("%s's age is %d year old!" %(name,age))
# #Call function
# fun("Neetu",25)

# def multiply(a,b):
#     return a*b

# for n in range(1,10):
#     for m in range(1,10,2):
#         print(multiply(n,m))
        

# Modify this function to return a list of strings as defined above
def list_benefits():
    p = "More organized code"
    q = "More readable code"
    r = "Easier code reuse"
    t = "Allowing programmers to share and connect code together"
    return [p,q,r,t]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(b):
    return("%s is a benefit of functions!" %b)

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()