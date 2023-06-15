from flask import Blueprint

from typing  import Dict, List

leaders_bp = Blueprint('leaders', __name__)

# zapros na poluchenie top 5 uchastnikov

@leaders_bp.route('/leaders/<string:level>', method=['GET'])
def get_top_5_leaders(level: str = 'all') -> Dict[str, List[Dict[str, int]]]:
    pass