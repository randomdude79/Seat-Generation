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
  with open('seatsDM.md', 'w') as s:
    s.write(
        f'| Table A | Table B | Table C | Table D |\n| --- | --- | --- | --- |\n|{TableA[0]}|{TableB[0]}|{TableC[0]}|{TableD[0]}|\n|{TableA[1]}|{TableB[1]}|{TableC[1]}|{TableD[1]}|\n|{TableA[2]}|{TableB[2]}|{TableC[2]}|{TableD[2]}|\n|{TableA[3]}|{TableB[3]}|{TableC[3]}|{TableD[3]}|\n\n| Table E | Table F | Table G |\n| --- | --- | --- |\n|{TableE[0]}|{TableF[0]}|{TableG[0]}|\n|{TableE[1]}|{TableF[1]}|{TableG[1]}|\n|{TableE[2]}|{TableF[2]}|{TableG[2]}|\n||||'
    )
  time.sleep(random.randint(1, 5) / 10)
