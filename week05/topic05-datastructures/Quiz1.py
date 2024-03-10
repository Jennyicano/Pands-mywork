# Author Jennifer Ibanez Cano

# This program shows a quiz where 
# I'll give the asnwer to the below questions:

numberOfQuestions = 5
averageAge = 23.4
debugMode = True
name = "joe"
ages = []
months = ('Jan', 'Feb', 'Mar')
book = {}
stuff = [ 12 , 'Fred', False, {}]
someone = dict(firstname = "joe")
me = {
    "firstName" : "Andrew",
    "teaching"  : [{
        "courseName" : "programming",
        "semester" : 1
    },{
        "courseName" : "Data Representation",
        "semester" : 2
    }
] }

# What are the variable types of:
    # a. numberOfQuestions 
    # b. averageAge
    # c. debugMode
    # d. name
    # e. ages
    # f. months
    # g. months[1]
    # h. book
    # i. stuff
    # j. stuff[2]
    # k. someone
    # l. someone["firstname"]
    # m. me
    # n. me["teaching"]
    # o. me["teaching"][0]["semester"]
    # p. me["teaching"][0]["coursename"]

print (type(numberOfQuestions))
print (type(averageAge))
print (type(debugMode))
print (type(name))
print (type(ages))
print (type(months))
print (type(months [1]))
print (type(book))
print (type(stuff))
print (type(stuff [2]))
print (type(someone))
print (type(someone ["firstname"]))
print (type(me))
print (type(me ["teaching"]))
print (type(me ["teaching"], [0], ["semester"]))
print (type(me ["teaching"], [0], ["courseName"]))