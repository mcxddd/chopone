from flask import jsonify

def create_response(success: bool, message: str, data: any = None):
    response = jsonify({
        'success': success,
        'message': message,
        'data': data
    })
    response.headers['Content-Type'] = 'application/json'
    return response 