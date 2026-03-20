# default1.py
def say_myself(name,man=True,age):
    print("My name is %s."%name)
    print("My age is %d."%age)
    if man:
        print("I'm man.")
    else:
        print("I'm woman.")

say_myself("Park",27)
say_myself("Kim",30,False)
