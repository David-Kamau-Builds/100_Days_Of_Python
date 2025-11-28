list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(n) for n in list_of_strings]
print(numbers)
result = [num for num in numbers if num % 2 == 0]
print(result)
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]


students_scores = {student:random.randint(1, 100) for student in names}

print(students_scores)

passed_students = {student:score for (student, score)  in students_scores.items() if score > 60}
print(passed_students)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()
print(words)
result = {word:len(word) for word in words }
print(result)



weather_c = {
    "Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24
}

weather_f = {day: int(temp_c * 9/5) + 32 for day, temp_c in weather_c.items()}
print(weather_f)
