# api.py
from fastapi import FastAPI, HTTPException
from amazon_recommendation import recommend

app = FastAPI()

@app.get("/recommend")
def get_recommendations(user_id: int):
    if not user_id:
        raise HTTPException(status_code=400, detail="user_id parameter is required")
    recommendations = recommend(user_id)
    return recommendations

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
