from database.models import Question, db

import random

# poluchit voprosi
def get_questions_db(level):

    # esli level ne ukazan
    if level == 'all':
        questions = []

        # poluchaem vse voprosi iz bazi
        all_questions = Question.query.all()

        # 20 randomnih vorosov
        for i in range(20):
            questions.append(random.choice(all_questions))

        return questions

    # esli ukazal slojnost, to filtr po voprosam
    questions_from_level = Question.query.filter(level=level).all()
    questions = [random.choice(questions_from_level) for i in range(20)]

    return questions

# prverka otvetov polzovatelya
def check_user_answer_db(question_id, user_answer):
    current_question = Question.query.get(question_id)

    # proverka otveta polzovatelya s realnim otvetom v baze

    if current_question.correct_answer == user_answer:
        return True

    return False

# dobavlenie voprosov v bazu (DZ)