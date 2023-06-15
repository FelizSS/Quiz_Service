from database.models import Result, db, Raiting


# poluchit reyting polzovateley

def get_rating_db(level):

    # esli po vsem napravleniyam
    if level == 'all':
        rating = Result.query.all()

        rating_user = []

# Dobvlenie otveta polzovatelya

def add_add_user_answer_db(user_id, user_answer, correctness):
    pass


# dobavlenie v reyting
def add_user_rating_db(user_id, correct_answers):

    # proverka est li polzovatel v tablice raiting
    pass