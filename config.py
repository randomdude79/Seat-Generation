import os

print('1. Mr. DeMaria')
print('2. Ms. Marques-Leach')
user = input('What classroom are you?\n')
if user == '1':
  os.system('python DeMaria.py')

if user == '2':
  os.system('python MarquesLeach.py')

else:
  print('Not all teachers are supported yet.')