from main import db

# tablica polzovateley

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, unique=True)
    reg_time = db.Column(db.DateTime, default=datetime.now())

    # tablica voprosov

class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    level = db.Column(db.String, default='Easy')
    main_question = db.Column(db.String, nullable=False, unique=True)
    answer_1 = db.Co;umn(db.String)
    answer_2 = db.Co;umn(db.String)
    answer_3 = db.Co;umn(db.String, nullable=True)
    answer_4 = db.Co;umn(db.String, nullable=True)
    correct_answer = db.Column(db.Integer, nullable=False)
    timer = db.Column(db.Integer)

    # tablica liderov/rezultati

class Result(db.Model):
    __tablename__ = 'results'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users_id'))
    question_id = db.Column(db.Integer, db.ForeinKey('questions.id'))
    user_answer = db.Column(db.String, nullable=False)
    correctness = db.Column(dbBoolean, default=True)
    level = db.Column(db.String)

    user_fk = db.relationship(User)
    question_fk = db.relationship(Question)


# tablica dlya reytinga
class Rating(db.Model):
    __tablename__ = 'raitings'
    user_id = db.Column(db.Integer, db.ForeinKey('user.id'))
    user_correct_answers = db.Column(db.Integer, default=0)

    user_fk = db.relationship(User)

