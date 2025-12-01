final_exam = int(input("Enter your final exam score: "))
weekly_exam = int(input("Enter your weekly exam score: "))
exercise = int(input("Enter your exercise score: "))
grade = 0.4 * final_exam + 0.4 * weekly_exam + 0.2 * exercise

print("Your grade is:", grade)