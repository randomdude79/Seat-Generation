import random
import time

for i in range(random.randint(1, 50)):
  TableA = []
  TableB = []
  TableC = []
  TableD = []
  TableE = []
  TableF = []
  TableG = []

  Students = [
      'Sasha', 'Leo', 'Jeremias', 'Oscar', 'Polly', 'Hannah G', 'Jahkya',
      'Ezra T', 'Ernesto', 'Evy', 'Jasmine', 'Anne', 'Marisol', 'Asher',
      'Luke', 'Ezra W', 'Kevin', 'Genesis', 'Noelle', 'Laith', 'Simone',
      'Simmiah', 'Thomas', 'Alice', 'Yisselis'
  ]

  for i in range(4):
    student = random.choice(Students)
    TableA.append(student)
    Students.remove(student)
  for i in range(4):
    student = random.choice(Students)
    TableB.append(student)
    Students.remove(student)
  for i in range(4):
    student = random.choice(Students)
    TableC.append(student)
    Students.remove(student)
  for i in range(4):
    student = random.choice(Students)
    TableD.append(student)
    Students.remove(student)
  for i in range(3):
    student = random.choice(Students)
    TableE.append(student)
    Students.remove(student)
  for i in range(3):
    student = random.choice(Students)
    TableF.append(student)
    Students.remove(student)
  for i in range(3):
    student = random.choice(Students)
    TableG.append(student)
    Students.remove(student)
    with open('templates/seatsDM.md', 'w') as s:
      s.write(
        '| Table A | Table B | Table C | Table D |\n| --- | --- | --- | --- |\n'
        '|{}|{}|{}|{}|\n|{}|{}|{}|{}|\n|{}|{}|{}|{}|\n|{}|{}|{}|{}|\n\n'
        '| Table E | Table F | Table G |\n| --- | --- | --- |\n'
        '|{}|{}|{}|\n|{}|{}|{}|\n|{}|{}|{}|\n||||'.format(*TableA, *TableB, *TableC, *TableD, *TableE, *TableF, *TableG)
      )
  time.sleep(random.randint(1, 5) / 10)
