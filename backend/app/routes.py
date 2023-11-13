# backend/app/routes.py
from . import app, mongo
from flask import jsonify

# Sample route to get brewery details
@app.route('/api/breweries/<brewery_id>', methods=['GET'])
def get_brewery_details(brewery_id):
    brewery_details = mongo.db.breweries.find_one({'_id': brewery_id})
    if brewery_details:
        return jsonify({"breweryDetails": brewery_details})
    else:
        return jsonify({"error": "Brewery not found"}), 404

# Sample route to get all reviews for a specific brewery
@app.route('/api/breweries/<brewery_id>/reviews', methods=['GET'])
def get_reviews(brewery_id):
    reviews = mongo.db.reviews.find({'brewery_id': brewery_id})
    reviews_list = [{"username": review['username'], "comment": review['comment']} for review in reviews]
    return jsonify(reviews_list)

# Sample route to add a review for a specific brewery
@app.route('/api/breweries/<brewery_id>/reviews', methods=['POST'])
def add_review(brewery_id):
    data = request.json
    new_review = {
        'brewery_id': brewery_id,
        'username': data['username'],
        'comment': data['comment']
    }
    mongo.db.reviews.insert_one(new_review)
    return jsonify({"message": "Review added successfully"})
