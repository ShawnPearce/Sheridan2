list=[85,72,38,55,65,68,72,81,93,74]
for score in list:
    if score > 80:
        grade = "A"
    elif score >= 70:
        grade ="B"
    elif score >=60:
        grade="C"
    elif score >=50:
        grade="D"
    else:
        grade = "F"
    print(score,grade)