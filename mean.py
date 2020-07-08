def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    
    return the_mean


monday_temp = [8.8, 2.3, 6.8, 7.2]
student_grades = {"marry": 9.1, "sim" : 8.8, "john" : 7.5}

print(mean(monday_temp))