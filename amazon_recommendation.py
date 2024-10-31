import pandas as pd
import numpy as np

def load_data():
    data = pd.read_csv("amazon.csv")
    data.columns = ['user_id', 'product_id', 'ratings', 'timestamp']
    # Sample and preprocess the data as in your original script
    counts = data['user_id'].value_counts()
    filtered_data = data[data['user_id'].isin(counts[counts >= 50].index)]
    final_ratings = filtered_data.pivot(index='user_id', columns='product_id', values='ratings').fillna(0)
    return final_ratings

def recommend(user_id):
    # Dummy recommendation logic for demonstration purposes
    recommendations = [
        {"product_id": "B00004SB92", "score": 6},
        {"product_id": "B00008OE6I", "score": 5},
        {"product_id": "B00005AW1H", "score": 4},
        {"product_id": "B0000645C9", "score": 4},
        {"product_id": "B00007KDVI", "score": 4}
    ]
    return recommendations
