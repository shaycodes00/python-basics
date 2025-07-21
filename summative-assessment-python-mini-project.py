# Function to get letter grade from score
def get_grade(score):
    # Check score and return grade
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Function to print all students
def show_summary(students):
    # Show summary title
    print("\nStudent Summary:")
    # Print each student's info
    for student in students:
        print(f"{student['name']}: {student['score']} -> {student['grade']}")

# Function to save to file
def save_to_file(students):
    # Save to grades.txt
    with open("grades.txt", "w") as file:
        # Write each student's info
        for student in students:
            file.write(f"{student['name']}: {student['score']} -> {student['grade']}\n")

# Main part of program
def main():
    # Show welcome message
    print("Welcome to the Grade Tracker!")
    # Make empty list for students
    students = []

    # Loop to get student info
    while True:
        # Get name and score
        name = input("Enter student name: ")
        score = float(input("Enter score (0–100): "))
        # Get grade for score
        grade = get_grade(score)
        # Add student to list
        students.append({"name": name, "score": score, "grade": grade})
        # Ask to add more
        more = input("Add another student? (yes/no): ").lower()
        # Stop if not yes
        if more != "yes":
            break

    # Show all students
    show_summary(students)
    # Save to file
    save_to_file(students)
    # Say data is saved
    print("\nAll data saved to 'grades.txt'")

# Start the program
main()