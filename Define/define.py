# def test(name,family):
#      print(f"my name is {name} and last name is {family}")
#      if name.isdigit() or family.isdigit():
#          print("please insert your name and family")
#          exit()
#      else:
#          pass
# while True:
#      d=input("insert your Name:")
#      z=input("inser your Family:")
#      test(d , z)
     
###############################################################################

# if you write a parameter to has a default value you can't write another parameter after that without default value
# for example:
# def test(name,family=""): 
#     pass
# def test(name="",family):
#     pass
# the above codes are wrong
# but you can write like this:
# def test(name="",family=""):
#     pass
# def test(name,family):
#     pass
# the above codes are correct
#########################################################################################

# def narouk(*names):
#     for name in names:
#         print(name)
#     L=input("insert your name:") 
#     if L in names:
#         print(f"the name {L} is in the list")
#     else:
#         print(f"the name {L} is not in the list")
# narouk("Mohammad","Ali","Reza","Hassan","Hossein")

#########################################################################################



def houli(**Cars):
    for key, value in Cars.items():
        print(f"{key} : {value}")
name = "Toyota"
model = "Corolla"
houli(name=name, model=model)

############################################################################################
# if behind a parameter write * it means that the parameter is a tuple
# for example:  def narouk(n, *names):  the names is a tuple
# if behind a parameter write ** it means that the parameter is a dictionary
# for example:  def narouk(n, **names):  the names is a dictionary
# if you write * and ** in one parameter you should write * first and then **
# for example:  def narouk(n, *names, **family):  the names is a tuple and the family is a dictionary
# if you write * and ** in one parameter you should write * first and then **
# for example:  def narouk(n, **family, *names):  the names is a tuple and the family is a dictionary
# if you write * and ** in one parameter you should write * first and then **   