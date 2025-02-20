from flask import Blueprint, jsonify, request
from .models import YourModel  # Replace with your actual model

bp = Blueprint('api', __name__)

@bp.route('/your_endpoint', methods=['GET'])
def get_items():
    items = YourModel.query.all()  # Replace with your actual query
    return jsonify([item.to_dict() for item in items])  # Ensure to implement to_dict method in your model

@bp.route('/your_endpoint/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = YourModel.query.get(item_id)  # Replace with your actual query
    if item is None:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(item.to_dict())  # Ensure to implement to_dict method in your model

@bp.route('/your_endpoint', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = YourModel(**data)  # Ensure your model can accept this data
    new_item.save()  # Implement save method in your model
    return jsonify(new_item.to_dict()), 201

@bp.route('/your_endpoint/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = YourModel.query.get(item_id)  # Replace with your actual query
    if item is None:
        return jsonify({'error': 'Not found'}), 404
    data = request.get_json()
    for key, value in data.items():
        setattr(item, key, value)  # Update item attributes
    item.save()  # Implement save method in your model
    return jsonify(item.to_dict())

@bp.route('/your_endpoint/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = YourModel.query.get(item_id)  # Replace with your actual query
    if item is None:
        return jsonify({'error': 'Not found'}), 404
    item.delete()  # Implement delete method in your model
    return jsonify({'message': 'Deleted successfully'}), 204