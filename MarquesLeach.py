import random
import time

for i in range(random.randint(1, 50)):
  Table1 = []
  Table2 = []
  Table3 = []
  Table4 = []
  Table5 = []

  Students = [
      'Jeremias', 'Evy', 'Oscar', 'Yisellis', 'Kevin', 'Jasmine', 'Alice',
      'Sasha', 'Noelle', 'Simmiah', 'Ezra', 'Asher', 'Simone', 'Emily', 'Leo',
      'Polly', 'Hannah', 'Ernesto', 'Anne'
  ]

  for i in range(4):
    student = random.choice(Students)
    Table1.append(student)
    Students.remove(student)
  for i in range(4):
    student = random.choice(Students)
    Table2.append(student)
    Students.remove(student)
  for i in range(4):
    student = random.choice(Students)
    Table3.append(student)
    Students.remove(student)
  for i in range(4):
    student = random.choice(Students)
    Table4.append(student)
    Students.remove(student)
  for i in range(3):
    student = random.choice(Students)
    Table5.append(student)
    Students.remove(student)

  with open('seatsML.md', 'w') as s:
    s.write(
        f'| Table 1 | Table 2 | Table 3 | Table 4 | Table 5 |\n| - | - | - | - | - |\n|{Table1[0]}|{Table2[0]}|{Table3[0]}|{Table4[0]}|{Table5[0]}|\n|{Table1[1]}|{Table2[1]}|{Table3[1]}|{Table4[1]}|{Table5[1]}|\n|{Table1[2]}|{Table2[2]}|{Table3[2]}|{Table4[2]}|{Table5[2]}|\n|{Table1[3]}|{Table2[3]}|{Table3[3]}|{Table4[3]}||'
    )
  time.sleep(random.randint(1, 5) / 10)
