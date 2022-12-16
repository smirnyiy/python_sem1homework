#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
def DayRecognition(dayNumber):
 if dayNumber == 6 or dayNumber == 7:
    print("Этот день выходной")
 elif dayNumber > 0 and dayNumber < 6:
    print("Этот день рабочий")
 elif dayNumber < 1 or dayNumber > 7:
    print("Некорректный номер дня недели, попробуйте снова!")

print("Please enter some day number and I'll try to recognize that it is a day off or a working day.")
dayNumber = int(input("Введите день недели: "))
DayRecognition(dayNumber)