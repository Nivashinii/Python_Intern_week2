def get_grade_and_message(marks):
    if 90 <= marks <= 100:
        return "A", "Excellent work! Keep shining!"
    elif 80 <= marks <= 89:
        return "B", "Very Good! Keep it up!"
    elif 70 <= marks <= 79:
        return "C", "Good job! You can do even better!"
    elif 60 <= marks <= 69:
        return "D", "Nice effort! Try to improve further!"
    else:
        return "F", "Don't worry! Practice more and you'll improve!"


def get_valid_marks():
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid input! Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    name = input("Enter student name: ")
    marks = get_valid_marks()

    grade, message = get_grade_and_message(marks)

    print("\nRESULT FOR {}:".format(name.upper()))
    print("Marks: {}/100".format(marks))
    print("Grade:", grade)
    print("Message:", message)


if __name__ == "__main__":
    main()