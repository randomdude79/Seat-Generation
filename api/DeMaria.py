import random

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

random.shuffle(Students)

TableA, TableB, TableC, TableD, TableE, TableF, TableG = Students[:4], Students[4:8], Students[8:12], Students[12:16], Students[16:19], Students[19:22], Students[22:]

with open('templates/seatsDM.md', 'w') as s:
    s.write(
        f'| Table A | Table B | Table C | Table D |\n'
        f'| --- | --- | --- | --- |\n'
        f'|{TableA[0]}|{TableB[0]}|{TableC[0]}|{TableD[0]}|\n'
        f'|{TableA[1]}|{TableB[1]}|{TableC[1]}|{TableD[1]}|\n'
        f'|{TableA[2]}|{TableB[2]}|{TableC[2]}|{TableD[2]}|\n'
        f'|{TableA[3]}|{TableB[3]}|{TableC[3]}|{TableD[3]}|\n\n'
        f'| Table E | Table F | Table G |\n'
        f'| --- | --- | --- |\n'
        f'|{TableE[0]}|{TableF[0]}|{TableG[0]}|\n'
        f'|{TableE[1]}|{TableF[1]}|{TableG[1]}|\n'
        f'|{TableE[2]}|{TableF[2]}|{TableG[2]}|\n'
        f'||||'
    )
