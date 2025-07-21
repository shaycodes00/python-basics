### START

1. Define a function get_letter_grade(score)
1. IF score >= 90 → RETURN 'A'
1. ELSE IF score >= 80 → RETURN 'B'
1. ELSE IF score >= 70 → RETURN 'C'
1. ELSE IF score >= 60 → RETURN 'D'
1. ELSE → RETURN 'F'

### Define a function

1. print_summary(student_list)
1. PRINT "Student Summary:"
1. FOR each student in student_list:
1. PRINT student name, score, and letter grade

### Define a function

1. save_to_file(student_list)
1. OPEN "grades.txt" in write mode
1. FOR each student in student_list:
1. WRITE name, score, and grade to file (one per line)
1. CLOSE file

### Main Program

1. PRINT welcome message
1. CREATE empty list called students
1. WHILE user wants to continue:
1. ASK for student name
1. FORMAT name (capitalize properly)
1. ASK for score
1. CONVERT score to number (float or int)
1. VALIDATE input (optional error check)
1. CALL get_letter_grade(score) to get grade
1. ADD (name, score, grade) to students list
1. ASK user if they want to add another student
1. AFTER loop ends:
   1. CALL print_summary(students)
   1. CALL save_to_file(students)
   1. PRINT "Data saved" message
