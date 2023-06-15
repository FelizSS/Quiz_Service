from flask import Blueprint

from typing import Dict, List

registration_bp = Blueprint('registration', __name__)

# zapros na registraciyu
@registration_bp.route('/register/<string:name>/<int:number>', methods=['POST'])

def register_user(name:str, number:int) -> Dict[str, int]:
    pass

