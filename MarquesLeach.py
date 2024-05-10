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

  with open('templates/seatsML.md', 'w') as s:
    s.write(
        '| Table 1 | Table 2 | Table 3 | Table 4 | Table 5 |\n| - | - | - | - | - |\n'
        '|{}|{}|{}|{}|{}|\n|{}|{}|{}|{}|{}|\n|{}|{}|{}|{}|{}|\n|{}|{}|{}|{}||'.format(*Table1, *Table2, *Table3, *Table4, *Table5)
    )
  time.sleep(random.randint(1, 5) / 10)
