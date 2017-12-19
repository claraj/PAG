from grade_calculator import grade_calculator

points, messages = grade_calculator.calc('Lab_1')

print('Total points =', points)

for msg in messages:
    print(msg)
