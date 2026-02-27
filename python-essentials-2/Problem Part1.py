class StudentMarks:
    def last_three_avg(self, marks):
        try:
            sum=0
            i=-1
            while i>=-3:
                sum += marks[i]
                i-=1
            return sum/3
        except:
            return "Not Enough marks to calcuate average"


studentMarks = StudentMarks()

marks = list(map(int, input("Enter marks separated by space: ").split()))

result = studentMarks.last_three_avg(marks)
print("Average of last 3 marks is: ", result)