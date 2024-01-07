
### Dictionary
# { key: value}
# { "Bug": "an Error in a programs",

#}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",

    }


# Dictionaries are run by keys, and if you print it gives you the value
print(programming_dictionary["Bug"])


# Adding new items to dictionary:
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

#Create an empty dictionary
empty_dictionary = {}


#wipe an existing dictionary
#programming_dictionary = {}

#Edit an item in a dictonary
programming_dictionary["Bug"] = "A moth in your computer"

#Loop through a dictionary
for something in programming_dictionary:
    print(something)
    
    # This code just give you the keys not the values

for key in programming_dictionary:
    print(key) # To print the keys
    print(programming_dictionary[key]) # To print the values


#########################
    # Grading Program ###
#########################
    student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = student_scores
for key in student_scores:
  if  student_scores[key] >= 91:
    student_grades[key] =  "Outstanding"
  elif student_scores[key] >= 81:
    student_grades[key] =  "Exceeds Expectations"
  elif student_scores[key] >= 71:
    student_grades[key] =  "Acceptable"
  else:
    student_grades[key] =  "Fail"


    ### nesting lists and citionaries

    capitals = {
       "France": "Paris",
       "Germany":"Berlin",
      
   }
    #### Nesting a list in a dictionary
    travel_log = {
       "France": ["Paris","Lille","Dijon"],
    }


### nesting a dictrionary in a dictionary
    travel_log2 = {
       "France": {"cities_visited":["Paris","Lille","Dijon"], "total_visits": 12},   
    }

### Nesting a dictionary in a list
    dictList = [
       {"country": "France", "cities_visited":["Paris","Lille","Dijon"], "total_visits": 12},   
    ]