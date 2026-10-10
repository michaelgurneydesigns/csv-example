import csv  # We will need modules from csv


students = []  # creating variable

with open("students.csv", "r") as file:  # we are opening and reading this file
    reader = csv.DictReader(file)  # this is a variable
    for row in reader: # uses first row value for each column as key
        row["score"] = int(row["score"]) # convert score value to integer
        students.append(row)  # add student row to list

print(f"Loaded {len(students)} student records")  # "Loaded (XX) student records"

subjects = {} 

for student in students:  # create a new dictionary
    subject = student["subject"]  # we have create 3 keys w/ subject
    if subject not in subjects:  # this is a conditional
        subjects[subject] = []  # if no value for subject
    subjects[subject].append(student["score"])

print("\n === Subject Averages ===")  # this is a heading
for subject, scores in subjects.items():  # for loop
    avg = sum(scores) / len(scores)  # create variable called "avg"
    print(f'{subject}: {avg:.1f} ({len(scores)} students)') # subject avg


    all_scores = [s["score"] for s in students]  # create variable called "all_scores"

    with open("grade_report.txt", "w") as file:  # create a new file and "write" not "read"
        file.write("GRADE REPORT\n")  # write heading to file
        file.write("=" * 40 + "\n\n")  # write separator to file
        file.write(f"Total students: {len(students)}\n")
        file.write(f"Overall average: {sum(all_scores) / len(all_scores):.1f}\n")
        file.write(f"Highest score: {max(all_scores)} \n")  # write the highest score
        file.write(f"Lowest score: {min(all_scores)} \n")  # write the lowest score

        file.write("BY SUBJECT\n")
        for subject, scores in subjects.items():
            avg = sum(scores) / len(scores)  # create variable called "avg"
            file.write(f" {subject}: {avg:.1f} avg ({len(scores)} students)")

print("\nReport written to grade_report.txt") 