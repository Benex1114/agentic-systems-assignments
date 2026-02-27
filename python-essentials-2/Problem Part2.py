class StudentScores:
    def highest_last_two(self, scores):
        try:
            if(scores[-1] > scores[-2]):
                return scores[-1]
            else:
                return scores[-2]
        except:
            return "Not enough scores to find highest value"

studentScores = StudentScores()

scores = list(map(int, input("Enter scores separated by space: ").split()))

result = studentScores.highest_last_two(scores)
print("Highest score among the last two is: ", result)