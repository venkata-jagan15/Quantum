from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List
from ml_engine import MLEngine
import uvicorn

app = FastAPI(title="Mini-Quantum API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = MLEngine()

class PredictionRequest(BaseModel):
    model_type: str
    features: Dict[str, float]

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/models")
async def get_models():
    return {
        "classical": ["logistic", "svm", "random_forest"],
        "quantum": ["qsvm", "vqc"]
    }

@app.get("/features")
async def get_features():
    return {"features": engine.get_features()}

@app.post("/predict")
async def predict(request: PredictionRequest):
    try:
        print(f"Prediction request for model: {request.model_type}")
        if request.model_type in ["logistic", "svm", "random_forest"]:
            result = engine.predict_classical(request.model_type, request.features)
        elif request.model_type in ["qsvm", "vqc"]:
            result = engine.predict_quantum(request.model_type, request.features)
        else:
            raise HTTPException(status_code=400, detail="Invalid model type")
        return result
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    print("--- Starting Mini-Quantum API with Auto-Reload ---")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
