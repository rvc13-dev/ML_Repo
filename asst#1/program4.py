it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
print("length o fhe set it_companies :",len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add('twitter')
print("adding twitter to the it_companies ",it_companies)

#Insert multiple IT companies at once to the set it_companies
list1 = ['Wipro','Qualcomm','dxc']
it_companies.update(list1)
print('set after adding multiple it companies at once :',it_companies)
#it_companies.add('Qualcomm')
#it_companies.add('dxc')
#print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove('Microsoft')
print('set after removing microsoft :',it_companies)

#Join A and B
print('join A and B',A.union(B))

#Find A intersection B
print('A intersection b',A.intersection(B))

#Is A subset of B
print('A subset of b',A.issubset(B))

#Are A and B disjoint sets
print('Are A and B disjoint sets :',A.isdisjoint(B))

#Join A with B and B with A
print('Join A with B:',A.union(B))
print('join B with A ',B.union(A))

#Symmetric difference between A and B
print(A.difference(B))

#Delete the sets completely
A.clear()
print(A)
B.clear()
print(B)


#Convert the ages to a set and compare the length of the list and the set.
print(set(age))
