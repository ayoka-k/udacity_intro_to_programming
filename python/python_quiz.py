# -*- coding: utf-8 -*-

beginner = [['Anna _____ tired.', 'is'], 
['_____ is he? He is my friend from Japan.', 'Who'], 
['Today is Wednesday. Yesterday it _____ Tuesday.', 'was'], 
['Mary _____ English, Spanish and a bit of French.', 'speaks'],
['Where _____ Michael live?', 'does']]

intermediate = [['He made his children _____ their homework every afternoon.', 'do'], 
['Despite _____ hard, she failed the exam.', 'studying'], 
['If I _____, I would wait a while to begin investing.', 'were'],
['He will give you a call as soon as he _____.', 'arrives'],
['That is the man _____ grandfather founded Kentucky Root Beer.', 'whose']]

advanced = [['We haven’t got _____ Champagne.', 'much'],
['He goes to work _____ taxi.', 'by'],
['I’ve lost my keys. I can’t find them _____ .', 'anywhere'],
['She arrived _____ Victoria Station half an hour late.', 'at'],
['They weren’t invited to the party, and nor _____ I.', 'was']]

grammar_quiz = {
  'beginner' : beginner,
  'intermediate' : intermediate,
  'advanced' : advanced
}

def run_test(level):
  """Takes user's english level as input and runs the quiz
  """
  questions = grammar_quiz[level]
  for index_q in range(0, len(questions)):
    while True:
      answer_is_correct = ask_question(level, index_q)
      if answer_is_correct:
        break

def ask_question(level, index_q):
  """Shows questions to the user one by one and asks the user to type in an answer
  Takes user's english level and index of the question as inputs

  If user answers a question correctly it shows the next question
  If user gives a wrong answer it retries 
  """
  task = grammar_quiz[level][index_q]
  (answer, question) = (task[1], task[0])
  print question
  user_answer = raw_input('Type in your answer: ')
  if user_answer == answer:
    print question.replace('_____', user_answer)
    return True
  else:
    print 'Try again'
    return False

def choose_level():
  """Starts grammar quiz

  If user inputs non-existing level it retries
  """
  while True:
    level = raw_input('Type in your English level(Beginner, Intermediate or Advanced): ').lower()
    if level in grammar_quiz.keys():
      run_test(level)
      return 
    print 'Wrong level. Try again.'

print 'This is an English Grammar Test which offers you three levels of difficulty.' 
print 'Each level has five sentences with blank spaces. Your task is to fill in these blanks with only one word.'
print 'Good luck!'
choose_level()
