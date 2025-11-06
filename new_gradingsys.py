all_students = []  # all individual students are stored here as independent lists
class_sum = 0  # total GPA sum
class_average = 0


def grading_system():
    global class_sum  # so we can update it inside the function

    try:
        while True:
            student = []  # individual student list containing [name, gpa, remark]
            student_name = input("Enter Student Name (or type 'exit' to finish): ")
            if student_name.lower() == 'exit':  # prints the top student and rankings if available
                break

            student.append(student_name)  # 'append' means to insert a value to a list

            # enter 5 grades, and separate each number -> (actually strings) from one another using 'split'
            # use 'map' for converting separated numbers into integers
            grades = list(map(int, input("Enter five grades separated by spaces: ").split()))
            if len(grades) != 5:
                print("Please enter exactly five grades.")
                continue  # skip the rest of the code inside the current loop and reset

            # compute GPA
            def compute_gpa(grades):
                return sum(grades) / len(grades)

            # remark logic
            def remark(gpa):
                if gpa >= 95:
                    return 'Outstanding'
                elif gpa >= 85:
                    return 'Satisfactory'
                else:
                    return 'Unsatisfactory'

            final_grade = compute_gpa(grades)
            final_remark = remark(final_grade)

            student.append(final_grade)
            student.append(final_remark)

            # add GPA to class sum
            class_sum += final_grade

            # display
            print(f"\nStudent Name: {student_name}")
            print("Grades:", *grades)  # '*' to unpack a list
            print(f"GPA: {final_grade:.2f} | Remark: {final_remark}\n")

            all_students.append(student)

            # list so far
            print("All students so far:")
            for stud in all_students:
                print(f"{stud[0]}: GPA = {stud[1]:.2f}, Remark = {stud[2]}\n")

    except ValueError:
        print("INVALID INPUT")
        grading_system()  # call main function AGAIN to not exit automatically


grading_system()  # main function calling

# the following only executes if the user exits
if all_students:
    # compute class average
    class_average = class_sum / len(all_students)

    # take 'x' as the individual student list containing [name, gpa, remark]
    # each item on the list have their own index [0 -> NAME, 1 -> GPA, 2 -> REMARK]
    # find top student, 'max' function returns the biggest GPA
    top_student = max(all_students, key=lambda x: x[1])

    print("")
    print("=" * 50)
    # .2f format is rounding up the number to two decimal places
    print(f"CLASS AVERAGE: {class_average:.2f} | Top Student: {top_student[0]} | "
          f"GPA: {top_student[1]} | Remark: {top_student[2]}")

    print("=" * 50)

    print("\nALL STUDENTS RANKED:")

    sorted_students = sorted(all_students, key=lambda x: x[1], reverse=True)  # Compares GPA only ((INDEX number 1))
    for i, student in enumerate(sorted_students, 1):
        print(f"{i}. {student[0]}: GPA = {student[1]:.2f}, Remark = {student[2]}")
else:
    print("No student data entered.")
