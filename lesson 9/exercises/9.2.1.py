#sam sosa
#per. 4
#11-23-15

#9.2.1

#gets name, grade, and greets

name = input ("What's your name?: ")
grade = int(input("What grade are you in?: "))

if grade == 9:
    print ("Hello %s, welcome to your first year of high school!" %(name))
elif grade == 10:
    print ("I hope to see you in class sometime %s." %(name))
elif grade == 11:
    print ("you're almost a senior now, keep trying.")
elif grade == 12:
    print ("you're in for home sprint don't give up %s!" %(name))
else:
    print ("sorry not an accteptable grade")
