# Getting different type of inputs
# Here we get string, list and add it to a map
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_marks = list(student_marks.get(query_name))
    average_mark = sum(query_marks)/len(query_marks)
    print(f"{average_mark:.2f}")
