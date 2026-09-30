import random

#Currently, choosing the level of diffculty of a subject is subjective, and many students face diffculties with making these decisions.
#This program is intended to aid the students and make the decision-making process easier.
#Having a "class" ensures the code can be imported efficiently, and overall makes the code more organized.
class SubjectsRecommender:
  #This initializes all the variables, ensuring we don't have to set values to it in every function.
  def __init__(self):
    self.BASIC = 0    #These are similar to global variables but at a "class" level.
    self.HONORS= 1
    self.ADVANCED=2
    self.grade_9_geometry = Grade_9_Geometry()
    self.grade_9_physics = Grade_9_Physics()

  #This procedure contains questions that vary in difficulty levels and gauge the student's current ability with respect to the geometry aspect of 8th grade math.
  #This procedure recommends the level of geometry the student could take.
  def getGeometryRecommendation(self):
    grade_9_geometry = self.grade_9_geometry.get_grade_9_geometry_levels()
    geometry_quiz_questions=self.grade_9_geometry.get_geometry_quiz_questions()
    geometry_options = self.grade_9_geometry.get_geometry_answer_options()
    geometry_answers=  self.grade_9_geometry.get_geometry_answers()
    q_list=[]
    #This takes an input from the user asking them their overall math score from 8th grade.
    grade8_score= int(input('''You will be asked 4 questions in total. After this next question, you will be asked to answer 3 questions
    please type 1, 2, or 3 depending on which answer option you think is the correct one. What's your overall Grade 8 Math score in percentage?'''))
    #This counts the number of questions and shuffles it eventually, to ensure that students get different questions every time.
    for i in range(len(geometry_quiz_questions)):
        q_list.append(i)

    random.shuffle(q_list)
    #The quiz score is initially 0.
    quiz_score =0
    #This asks the user the questions and checks if their answers match the correct answers.
    for i in q_list:
      print(geometry_quiz_questions[i])
      option = input(geometry_options[i])
      if(option == geometry_answers[i]):
        quiz_score+=33
    print(quiz_score)
    #This is checking the user's final score out of 100. The user's final score consists of their grade 8 final score + the amount of points they secure on our quiz.
    #70% of weightage is given to their grade 8 final score and 30% of weightage is given to the amount of points they secure on our quiz.
    final_score = 0.7 * grade8_score + 0.3 * quiz_score
    if(0<= final_score <= 30):
      print(grade_9_geometry[self.BASIC])
    elif(30< final_score <= 60):
      print(grade_9_geometry[self.HONORS])
    else:
      print(grade_9_geometry[self.ADVANCED])

  #This procedure contains questions that vary in difficulty levels and gauge the student's current ability with respect to the physics aspect of 8th grade science.
  #This procedure recommends the level of physics the student could take.
  def getPhysicsRecommendation(self):
    grade_9_physics = self.grade_9_physics.get_grade_9_physics_levels()
    physics_quiz_questions=self.grade_9_physics.get_physics_quiz_questions()
    physics_options = self.grade_9_physics.get_physics_answer_options()
    physics_answers=  self.grade_9_physics.get_physics_answers()
    q_list=[]
    #This takes an input from the user asking them their overall science score from 8th grade.
    grade8_score= int(input('''You will be asked 4 questions in total. After this next question, you will be asked to answer 3 questions,
please type 1, 2, or 3 depending on which answer option you think is the correct one. What's your Grade 8 Science score? '''))
    #This counts the number of questions and shuffles it eventually, to ensure that students get different questions every time.
    for i in range(len(physics_quiz_questions)):
        q_list.append(i)
    #The quiz score is initially 0.
    quiz_score =0
    #This asks the user the questions and checks if their answers match the correct answers.
    for i in q_list:
      print(physics_quiz_questions[i])
      option = input(physics_options[i])
      if(option == physics_answers[i]):
        quiz_score+=33
    print(quiz_score)
    #This is checking the user's final score out of 100. The user's final score consists of their grade 8 final score + the amount of points they secure on our quiz.
    #70% of weightage is given to their grade 8 final score and 30% of weightage is given to the amount of points they secure on our quiz.
    final_score = 0.7 * grade8_score + 0.3 * quiz_score
    if(0<= final_score <= 30):
      print(grade_9_physics[self.BASIC])
    elif(30< final_score <= 60):
      print(grade_9_physics[self.HONORS])
    else:
      print(grade_9_physics[self.ADVANCED])

#This is to ensure an abstraction. All the Geometry related functions, lists, and attributes are stored in this class.
#In the future, all changes related to Geometry can be made in this class without changing the main program which is SubjectsRecommender.
class Grade_9_Geometry():
  def get_grade_9_geometry_levels(self):
    return  ['Geometry', 'Geometry Honors', 'Geometry Advanced']

  def get_geometry_quiz_questions(self):
    return ['If two angles of a triangle are 45 and 60 degrees, what is the measure of the third angle?',\
           'If two angles are complementary, and one angle is 30 degrees, what is the measure of the other angle?',\
                'What is the sum of the interior angles of a quadrilateral? ']

  def get_geometry_answer_options(self):
    return [['85 degrees','90 degrees','75 degrees'],['60 degrees','150 degrees','90 degrees'],['200 degrees','360 degrees','180 degrees']]

  #This function consists of the correct answers to the geometry questions.
  def get_geometry_answers(self):
    return ['3','1','2']

#This is to ensure an abstraction. All the Physics related functions, lists, and attributes are stored in this class.
#In the future, all changes related to Physics can be made in this class without changing the main program which is SubjectsRecommender.
class Grade_9_Physics():
  def get_grade_9_physics_levels(self):
    return  ['Physics I', 'Physics I Honors', 'Physics Advanced (AP Physics)']

  def get_physics_quiz_questions(self):
    return ['The correct equation to calculate speed is:','Bob cycles at an average speed of 8km/h. How far has he travelled if he cycles for 4 hours?',\
                            'You walk 10 meters to math class in 20 seconds. Your average speed is:']

  def get_physics_answer_options(self):
    return [['time/distance','distance/time','distance*time'],['43 km','55 km','32 km'],['0.5 m/s','5 m/s','1 m/s']]

  #This function consists of the correct answers to the physics questions.
  def get_physics_answers(self):
    return ['2','3','1']

subjectsRecommender = SubjectsRecommender()

subjectsRecommender.getGeometryRecommendation()