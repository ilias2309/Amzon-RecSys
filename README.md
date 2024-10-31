
# Amazon Recommendation System

This project demonstrates how to build a recommendation system for Amazon-style product recommendations using Python. The system provides personalized recommendations based on product similarity and review scores, leveraging collaborative filtering techniques with minimal dependencies (only `pandas` and `NumPy`).

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Requirements](#requirements)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Project Workflow](#project-workflow)
- [How to Improve This Project](#how-to-improve-this-project)
- [Conclusion](#conclusion)

## Introduction
The goal of this project is to create a recommendation system that can suggest products based on user ratings and review scores. This type of system is widely used in e-commerce websites like Amazon to enhance the user experience by offering personalized recommendations.

## Dataset
The dataset used contains information about `user_id`, `product_id`, `ratings`, and `timestamp`. The data used for this project does not have specific column names, so they are manually set. Additionally, we sample the data to reduce its size for demonstration purposes.

## Requirements
- Python 3.x
- `pandas`
- `numpy`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/STALPHA2708/amazon-recommendation-system.git
   cd amazon-recommendation-system
   ```

2. Install required packages:
   ```bash
   pip install pandas numpy
   ```

3. Download or place the dataset in the root directory as `amazon.csv`.

## Project Structure
```
amazon-recommendation-system/
├── amazon.csv                 # Dataset file
├── amazon_recommendation.py    # Python script for generating recommendations
└── README.md                   # Project documentation
```

## Usage
1. Import necessary libraries:
   ```python
   import numpy as np
   import pandas as pd
   ```

2. Load the dataset and preprocess it:
   ```python
   data = pd.read_csv("amazon.csv")
   data.columns = ['user_id', 'product_id', 'ratings', 'timestamp']
   ```

3. Sample the data for easier handling:
   ```python
   df = data[:int(len(data) * 0.1)]
   ```

4. Filter and process the data for recommendations:
   ```python
   counts = df['user_id'].value_counts()
   data = df[df['user_id'].isin(counts[counts >= 50].index)]
   final_ratings = data.pivot(index='user_id', columns='product_id', values='ratings').fillna(0)
   ```

5. Generate recommendations:
   ```python
   def recommend(id):
       recommend_products = recommendations
       recommend_products['user_id'] = id
       return recommend_products
   ```

6. Example usage:
   ```python
   print(recommend(11))
   ```

## Project Workflow
1. **Data Loading and Preprocessing**: Load the data, rename columns, and sample a portion for ease of processing.
2. **Data Filtering**: Retain users who have rated at least 50 products to ensure recommendation quality.
3. **Pivot Table Creation**: Create a user-item matrix for collaborative filtering.
4. **Recommendation Function**: Use product scores and ranks to generate personalized recommendations based on past reviews.
