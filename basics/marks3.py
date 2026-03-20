# marks3.py
marks = [90,25,67,45,80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d student, congratualtions! You passed."%(number+1))
