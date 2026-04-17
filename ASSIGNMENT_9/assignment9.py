#1
def count_files(file_name):
    count = 0
    with open(file_name) as file:
        for line in file:
            if line.strip() != "":
                count += 1
    return count

#2
def find_keywords(file_name, keywords):
    result = []
    with open(file_name) as file:
        line_number = 1
        for line in file:
            if keywords in line:
                result.append(line_number)
            line_number += 1
    return result

#3
def uppercase_file(input_file):
    with open(input_file) as file:
        content = file.read()

    content = content.upper()

    with open(output.txt) as file:
        file.write(content)

#4
def average_score(file_name):
    total = 0
    count = 0

    with open(file_name) as file:
        for line in file:
            name, score = line.strip().spilt(',')
            total += float(score)
            count += 1

    if count == 0:
        return 0
    return total/count