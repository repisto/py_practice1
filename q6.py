# q6.py
user_input = input("Enter the content: ")
f = open("test.txt",'a')
f.write(user_input)
f.write("\n")
f.close()
