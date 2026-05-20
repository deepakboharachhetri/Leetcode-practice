

if __name__ == '__main__':
    python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

    second_highest=sorted(list({score for _,score in python_students}))[1]
    second_highest_names=sorted([name for name,score in python_students if score==second_highest])
    for i in second_highest_names:
        print(i)

    