#create tuple
brothers=('Madhu','Chaitanya','Chandu')
sister=('Divya','sneha')

#Join brothers and sisters tuples and assign it to siblings
siblings=brothers+sister
print("siblings are :",siblings)

#How many siblings do you have?
print("total number of siblings :",len(siblings))

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents=('Nagamani','SriHari')

family_members=siblings+parents
print("adding mother and father to the tuple :",family_members)
