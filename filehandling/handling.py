def calculate(mark):
    if mark >= 70:
	    return "disctinction"
    elif mark >= 60:
            return "merit"
    elif mark >= 50:
            return "pass"
    else:
        return "fail"
def main():
    input_file = "names.txt"
    output_file = "result.txt"

    students = {}
    with open(input_file, "r") as f:
        for line in f:
            name, _, mark, weight = line.strip().split (",")
            mark, weight = float(mark), float(weight)

            if name not in students:
                students[name] = 0

            students[name] += mark * (weight / 100)

    with open(output_file, "w") as f:
        for name, final_mark in students.items():
            grade = calculate(final_mark)
            f.write(f"{name}  {final_mark:} {grade}\n")
