def grade(n):
    if n>=90:
        return "A"
    else:
        if 80<=n<90:
            return "B"
        else:
            if 70<=n<80:
                return "C"
            else:
                if 60<=n<70:
                   return "D"
                else:
                    return "F"

mark = 83
print( "Mark:", str(mark), "Grade:", grade(mark))
