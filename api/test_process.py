from flask import Blueprint

from typing import Dict, List

from pydantic import BaseModel

test_bp = Blueprint('test_process', __name__)

# validator voprosov
class Questions(BaseModel):
    timer: int
    question: List[Dict[int, Dict[str, List[str]]]]

@test_bp.route('/get-questions/<string:level>', methods=['GET'])
def get_user_questions(level: str) -> Questions:
    pass

# zapros na proverku otveta ot polzovatelya

@test_bp.route('/check-answer/<int:question_id>/<string:user_answer>', methods=['POST'])
def check_current_user_answer(question_id: imt, user_answer: str) -> Dict[str, int]:
    pass

# zapros na vivod rezultata

@test_bp.route('/done/<int:user_id>', methods=['POST'])
def user_done_test(user_id: int) -> Dict[str, int]:
    pass

