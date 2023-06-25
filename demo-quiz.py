# Question 
class Question:
    def __init__(self, text, choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer

#print(q1.checkAnswer('python'))
#print(q2.checkAnswer('go'))
#print(q3.checkAnswer('c#'))

# Quiz

class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex+1}: {question.text}')

        for q in question.choices:
            print('-' + q)
        
        
        answer = input('cevap: ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()
        
        if question.checkAnswer(answer):
            self.score += 1
            
        
        self.questionIndex += 1
        
    
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
            
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        totalQuestion = len(self.questions)
        print(f'score= {self.score} out of {totalQuestion}', )

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex +1 

        if questionNumber > totalQuestion:
            print('Quiz Bitti')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(50,'*'))


q1 = Question('en iyi programlama dili hangisidir? ', ['c#', 'python', 'go', 'java'], 'python')
q2 = Question('en populer programlama dili hangisidir? ', [ 'python', 'go', 'c#', 'java'], 'python')
q3 = Question('en çok kazandıran programlama dili hangisidir? ', ['c#',  'go', 'java', 'python'], 'python')


questions = [q1,q2,q3]

quiz = Quiz(questions)
# question = quiz.getQuestion()

# print(question.text)

quiz.loadQuestion()