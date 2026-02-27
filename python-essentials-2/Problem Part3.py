class StudentPerformance:
    def score_difference(self, scores):
        try:
            return (scores[-1] - scores[0])
        except:
            return "No scores available to calculate difference"

studentPerformance = StudentPerformance()

scores = list(map(int, input("Enter scores separated by space: ").split()))

result = studentPerformance.score_difference(scores)

print("Difference between last and first score is: ", result)