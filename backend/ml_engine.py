import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

from qiskit_aer import Aer
from qiskit.primitives import StatevectorSampler as Sampler
from qiskit.circuit.library import ZZFeatureMap, RealAmplitudes
from qiskit_machine_learning.kernels import FidelityQuantumKernel
from qiskit_machine_learning.algorithms import VQC
from qiskit_machine_learning.utils.loss_functions import CrossEntropyLoss
from qiskit_algorithms.optimizers import COBYLA

import os

# Base directory for data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(os.path.dirname(BASE_DIR), "ML-Models", "heart.csv")

class MLEngine:
    def __init__(self):
        self.data = pd.read_csv(DATA_PATH)
        self.X = self.data.drop("target", axis=1)
        self.y = self.data["target"]
        self.scaler = StandardScaler()
        self.X_scaled = self.scaler.fit_transform(self.X)
        
    def get_features(self):
        return self.X.columns.tolist()

    def predict_classical(self, model_type, input_data):
        # input_data is a dict of feature values
        df_input = pd.DataFrame([input_data])
        X_input_scaled = self.scaler.transform(df_input)
        
        X_train, X_test, y_train, y_test = train_test_split(
            self.X_scaled, self.y, test_size=0.2, random_state=42, stratify=self.y
        )
        
        if model_type == "logistic":
            model = LogisticRegression(max_iter=1000, solver="liblinear")
        elif model_type == "svm":
            model = SVC(kernel='rbf', probability=True, random_state=42)
        elif model_type == "random_forest":
            model = RandomForestClassifier(n_estimators=200, max_depth=5, random_state=42)
        else:
            raise ValueError("Invalid model type")
            
        model.fit(X_train, y_train)
        prediction = model.predict(X_input_scaled)[0]
        probability = model.predict_proba(X_input_scaled)[0][1] if hasattr(model, "predict_proba") else None
        
        return {
            "prediction": int(prediction),
            "probability": float(probability) if probability is not None else None,
            "model": model_type
        }

    def predict_quantum(self, model_type, input_data):
        df_input = pd.DataFrame([input_data])
        X_input_scaled = self.scaler.transform(df_input)
        
        # PCA for quantum models
        n_comp = 3 if model_type == "qsvm" else 2
        pca = PCA(n_components=n_comp)
        X_pca = pca.fit_transform(self.X_scaled)
        X_input_pca = pca.transform(X_input_scaled)
        
        # Reduced dataset for speed
        limit = 100 if model_type == "qsvm" else 40
        X_train_pca = X_pca[:limit]
        y_train = self.y[:limit]
        
        if model_type == "qsvm":
            feature_map = ZZFeatureMap(feature_dimension=3, reps=1)
            quantum_kernel = FidelityQuantumKernel(feature_map=feature_map)
            # Enable probability=True for SVC to get probability estimates
            model = SVC(kernel=quantum_kernel.evaluate, probability=True, random_state=42)
            model.fit(X_train_pca, y_train)
            
            raw_prediction = model.predict(X_input_pca)
            raw_probability = model.predict_proba(X_input_pca)
            
            # Robust indexing
            if hasattr(raw_prediction, "__len__") and len(raw_prediction.shape) > 0:
                prediction = raw_prediction[0]
            else:
                prediction = raw_prediction
                
            # Get probability for class 1
            if hasattr(raw_probability, "__len__") and len(raw_probability.shape) > 0:
                probability = raw_probability[0][1]
            else:
                probability = raw_probability[1] if len(raw_probability) > 1 else None

            return {
                "prediction": int(prediction),
                "probability": float(probability) if probability is not None else None,
                "model": "qsvm"
            }
            
        elif model_type == "vqc":
            feature_map = ZZFeatureMap(feature_dimension=2, reps=1)
            ansatz = RealAmplitudes(num_qubits=2, reps=1)
            optimizer = COBYLA(maxiter=20) # Reduced iter for speed
            sampler = Sampler() # Uses default local simulator
            model = VQC(
                feature_map=feature_map,
                ansatz=ansatz,
                optimizer=optimizer,
                loss=CrossEntropyLoss(),
                sampler=sampler
            )
            
            # One-hot encode or ensure categorical labels for VQC if needed.
            # VQC in qiskit-machine-learning usually expects labels to be integer or one-hot.
            # Since target is 0/1, we ensure it's a column vector if necessary or handle as-is.
            y_train_vqc = y_train.to_numpy()
            
            print(f"Fitting VQC with {len(X_train_pca)} samples...")
            model.fit(X_train_pca, y_train_vqc)
            
            print("Predicting with VQC...")
            raw_prediction = model.predict(X_input_pca)
            raw_probability = model.predict_proba(X_input_pca)
            
            # Handle the case where raw_prediction is a scalar or 0-d array
            if hasattr(raw_prediction, "__len__") and len(raw_prediction.shape) > 0:
                prediction = raw_prediction[0]
            else:
                prediction = raw_prediction
            
            # Handle probability result
            if hasattr(raw_probability, "__len__") and len(raw_probability.shape) > 0:
                probability = raw_probability[0][1]
            else:
                probability = None
                
            return {
                "prediction": int(prediction),
                "probability": float(probability) if probability is not None else None,
                "model": "vqc"
            }
        
        else:
            raise ValueError("Invalid quantum model type")
