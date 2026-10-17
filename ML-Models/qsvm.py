import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score

from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit.circuit.library import ZZFeatureMap
from qiskit_machine_learning.kernels import QuantumKernel

# -----------------------
# Load Dataset
# -----------------------
data = pd.read_csv("heart.csv")

X = data.drop("target", axis=1)
y = data["target"]

# -----------------------
# Train-Test Split
# -----------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# -----------------------
# Scaling
# -----------------------
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# -----------------------
# PCA (Reduce to 3 features for faster quantum execution)
# -----------------------
pca = PCA(n_components=3)
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)

# -----------------------
# Reduce dataset size (IMPORTANT for quantum speed)
# -----------------------
X_train = X_train[:100]
y_train = y_train[:100]

X_test = X_test[:50]
y_test = y_test[:50]

# -----------------------
# Quantum Feature Map
# -----------------------
feature_map = ZZFeatureMap(feature_dimension=3, reps=1)

backend = Aer.get_backend("aer_simulator")
quantum_instance = QuantumInstance(backend)

quantum_kernel = QuantumKernel(
    feature_map=feature_map,
    quantum_instance=quantum_instance
)

# -----------------------
# QSVM Model
# -----------------------
model = SVC(kernel=quantum_kernel.evaluate)

print("Training QSVM... Please wait.")

model.fit(X_train, y_train)

print("Training completed.")

# -----------------------
# Prediction
# -----------------------
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred)

print("\nQSVM Accuracy:", accuracy)
print("QSVM ROC-AUC:", roc_auc)

print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
