from flask import Blueprint, jsonify
api_bp = Blueprint('api', __name__)

@api_bp.route('/notes')
def get_notes():
    return jsonify({
        'message': 'notes api working'
    })