#Created an empty dictionary with the name dog and initially it is null
dog={}

#Adding name, color, breed, legs, age to the dog dictionary
dog={'name':'Rio','color':'White','breed':'Pug','legs':'4','age':'one year '}
print(dog)

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student={'first_name':'albert','last_name':'joshwa','gender':'male','age':'41','martial status':'married','skills':'python','country':'USA','city':'Texas','address':'Plano'}
print(student)

#Get the length of the student dictionary
print(len(student))

#Get the value of skills and check the data type, it should be a list
student_datatype = list(student)
print(student.get('skills'),type(student_datatype))

#Modify the skills values by adding one or two skills
student['skills']='java'
print(student)

#Get the dictionary keys as a list
print(list(student.keys()))

#Get the dictionary values as a list
print(list(student.values()))

