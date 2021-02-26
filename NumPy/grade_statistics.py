import numpy as np


def main():
    """
    Demonstrate NumPy axis and ndarray functions
    """

    #---------------------------------------------------------------------------
    # Data
    #---------------------------------------------------------------------------
    exercises = ["Homework 1", "Homework 2", "Exam 1", "Exam 2"]
    students = ["John", "Tom", "Bob"]

    grades = np.array([[100., 98, 100., 90.],
                       [100.,  0., 70., 90.],
                       [100., 70., 90., 80.]])

    #---------------------------------------------------------------------------
    # Statistics by Student
    #---------------------------------------------------------------------------
    avg_by_student = grades.mean(axis=1)
    min_by_student = grades.min(axis=1)
    max_by_student = grades.max(axis=1)

    print("| {:^8} | {:^4} | {:^4} | {:^5} |".format("Name", "Avg", "Min", "Max"))
    print("|:---------|-----:|-----:|------:|")

    grade_data = zip(students, avg_by_student, min_by_student, max_by_student)

    for name, avg, g_min, g_max in grade_data:
        print(f"| {name:<8} | {avg:>4.1f} | {g_min:>4.1f} | {g_max:>5.1f} |")

    print()

    #---------------------------------------------------------------------------
    # Statistics by Exercise
    #---------------------------------------------------------------------------
    avg_by_exercise = grades.mean(axis=0)
    max_by_exercise = grades.max(axis=0)
    std_by_exercise = grades.std(axis=0)

    print("| {:^12} | {:^5} | {:^5} | {:^8} |".format("Exercise", "Avg", "Max", "Std Dev"))
    print("|:-------------|------:|------:|---------:|")

    grade_data = zip(exercises, avg_by_exercise, max_by_exercise, std_by_exercise)

    for exercise, avg, g_max, g_stddev in grade_data:
        print(f"| {exercise:<12} | {avg:>5.1f} | {g_max:>5.1f} | {g_stddev:>8.1f} |")


if __name__ == "__main__":
    main()
