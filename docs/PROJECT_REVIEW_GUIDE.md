# Mini-Quantum: Project Review Guide

This document is a comprehensive guide prepared for tomorrow's mini-project review. It covers everything from your abstract and methodology to a detailed explanation of the application and the division of work among your team of 4 members.

---

## 1. Project Overview & Abstract

**Title:** Comparative Analysis of Classical and Quantum-Assisted Machine Learning Models for Early Heart Disease Prediction

**Abstract:**
Heart disease remains a leading cause of mortality worldwide, emphasizing the need for accurate and early risk prediction to support preventive healthcare. While traditional machine learning techniques are widely used for clinical decision-making, their ability to model complex, high-dimensional medical data is often limited. This mini project presents a comparative study of classical and quantum-assisted machine learning models for early heart disease risk prediction. 

Three classical classifiers—Logistic Regression, Random Forest, and Support Vector Machine (SVM)—are evaluated alongside two quantum-assisted models: the Quantum Support Vector Machine (QSVM) and Variational Quantum Classifier (VQC). Clinical and demographic data are pre-processed using normalization, feature scaling, and missing-value handling techniques. Quantum models are implemented in simulated quantum environments (Qiskit Aer), where classical features are encoded into quantum states using quantum feature maps and optimized through hybrid classical–quantum learning. Model performance is compared using accuracy, precision, recall, F1-score, and ROC-AUC. 

Results indicate that Random Forest performs strongly on full feature sets, while quantum-assisted models achieve competitive performance on reduced feature spaces by capturing non-linear feature relationships. Despite current hardware constraints, this study highlights the potential of quantum-assisted learning as a complementary approach for future intelligent healthcare prediction systems.

---

## 2. Work Splitting & Team Roles

This section clearly defines what each of the 4 team members contributed technically, as well as the 3 Literature Review papers they are responsible for presenting.

### Member 1: Frontend Architecture & UI/UX
**Technical Contribution:**
- Developed the complete Client-side interface using React and Vite.
- Designed the premium "Glassmorphism" UI with custom CSS for a modern, dark-mode aesthetic.
- Implemented real-time data visualization charts using Recharts.
- Handled API integration using Axios to securely send patient data payloads to the backend and parse prediction results.

**Literature Review Papers (Papers 1-3):**
1. **A hybrid framework for heart disease prediction using classical and quantum-inspired machine learning techniques (2025)**
   *Objective:* Develop a novel hybrid framework combining classical and quantum-inspired ML.
   *Research Gaps:* Existing models struggle with large numbers of features, which reduce interpretability, increase computational cost, and lower accuracy.
2. **Comparative analysis of heart disease prediction using logistic regression, SVM, KNN, and random forest (2025)**
   *Objective:* Preprocess heart disease data using imputation and normalization.
   *Research Gaps:* Optimal cross-validation strategies for robust prediction models are underexplored.
3. **QuCardio: Application of Quantum Machine Learning for Detection of Cardiovascular Diseases (2025)**
   *Objective:* Design QML models for multi-class classification using ECG images.
   *Research Gaps:* Limited prior work on multi-class QML classification on ECG image data.

### Member 2: Backend Architecture & Data Processing
**Technical Contribution:**
- Built the robust Python server using FastAPI and Uvicorn.
- Developed the `MLEngine` core that routes predictions to either Classical or Quantum domains.
- Implemented Data Preprocessing: handled data validation using Pydantic, Z-Score Normalization (`StandardScaler`), and dynamic data ingestion from `heart.csv`.

**Literature Review Papers (Papers 4-6):**
4. **Quantum K-means clustering method for detecting heart disease using quantum circuit approach (2025)**
   *Objective:* Propose and evaluate Quantum Enhanced Machine Learning (QuEML) methods.
   *Research Gaps:* Classical ML faces computational bottlenecks on larger data; limited tabular QML studies exist.
5. **Revolutionizing heart disease prediction with quantum-enhanced machine learning (2025)**
   *Objective:* Design QuEML models and compare them with traditional algorithms.
   *Research Gaps:* Classical models suffer from computational bottlenecks on large/complex datasets.
6. **Heart Disease Prediction Using GridSearchCV and Random Forest (2019)**
   *Objective:* Evaluate multiple ML algorithms using clinical data.
   *Research Gaps:* Models struggle with high-dimensional data and lack optimal hyperparameter tuning.

### Member 3: Classical ML Models Integration
**Technical Contribution:**
- Developed and integrated the Classical Machine Learning branch of the `MLEngine`.
- Implemented Scikit-Learn models: Logistic Regression, Random Forest, and Support Vector Machines (SVM).
- Designed the evaluation logic (Accuracy, Precision, Recall, F1-Score) to benchmark classical performance against quantum methods.

**Literature Review Papers (Papers 7-9):**
7. **Heart Disease Prediction Using Machine Learning Techniques (2022)**
   *Objective:* Develop early prediction systems using historical medical data.
   *Research Gaps:* Healthcare scalability issues and challenges in discrete medical data decision-making.
8. **Advancements In Heart Disease Prediction: A Machine Learning Approach (2017)**
   *Objective:* Assess 7 ML classifiers with hyperparameter tuning for accuracy.
   *Research Gaps:* Urgent need for efficient models to detect heart disease early amidst limited healthcare facilities.
9. **Quantum Machine Learning in Healthcare: Evaluating QNN and QSVM Models (2025)**
   *Objective:* Evaluate Quantum Neural Networks vs QSVMs on imbalanced healthcare datasets.
   *Research Gaps:* Classical ML struggles with biased minority classes; quantum models exploit higher-dimensional space better.

### Member 4: Quantum ML Models (QML) Integration
**Technical Contribution:**
- Spearheaded the Quantum Domain utilizing Qiskit, Qiskit-Aer, and Qiskit Machine Learning.
- Implemented Principal Component Analysis (PCA) to compress 13 clinical features into a smaller state space suitable for quantum registers.
- Developed the Variational Quantum Classifier (VQC) and Quantum Support Vector Machine (QSVM) simulated on local classical CPUs via Qiskit Aer.

**Literature Review Papers (Papers 10-12):**
10. **Heart Diseases Prediction System Using Quantum Technology (2025)**
    *Objective:* Integrate quantum computing with ML to improve diagnosis accuracy and efficiency.
    *Research Gaps:* Limited practical implementations evaluating quantum systems on real clinical datasets.
11. **AI-Based Preventive Healthcare Using Quantum Computing (2025)**
    *Objective:* Propose AI-driven preventive healthcare using quantum computing.
    *Research Gaps:* Classical AI struggles to capture complex feature interactions; limited empirical evaluation of QML on tabular data.
12. **Quantum Machine Learning in Healthcare: Evaluating QNN and QSVM Models (2025)**
    *Objective:* Evaluate QNN and QSVM specifically for imbalanced datasets (Heart Failure, Diabetes).
    *Research Gaps:* Classical models fail to capture complex non-linear patterns; highlights practical advantages of QSVM.

---

## 3. Methodology Review

When explaining the methodology to the review panel, break it down into the following flow:

1. **Data Preprocessing Phase:**
   - We utilize a standard heart disease dataset (`heart.csv`) with 13 key clinical features (e.g., age, cholesterol, BP).
   - We apply **Z-Score Normalization** via `StandardScaler` to ensure all numerical inputs are properly scaled—this is critical for distance-based models like SVM and QSVM.

2. **The Hybrid Branching Strategy (The Core Architecture):**
   - Our system uses a **Modular Router** via FastAPI that routes the prediction task into two computational domains:
     - **Classical Domain:** Trains algorithms (Logistic Regression, Random Forest, SVM) directly using the full 13-feature set.
     - **Quantum Domain:** Due to the hardware constraints of simulating qubits, we first compress the data using **Principal Component Analysis (PCA)** to a reduced 2D/3D space. This compressed data is then encoded into a quantum state vector.

3. **Model Implementations:**
   - **Classical:** Standard Scikit-learn pipelines. Random forest behaves as an ensemble method taking majority votes.
   - **Quantum:** We use **Variational Quantum Classifiers (VQC)** (using parameterized quantum circuits like `RealAmplitudes`) and **QSVM** (utilizing a `FidelityQuantumKernel` to map data into a higher-dimensional Hilbert space). Since we don't have a physical quantum computer, we use the `Qiskit Aer` simulator locally to perform these quantum state vector calculations.

4. **Evaluation & Consensus:**
   - Both domains yield predictions alongside standardized metrics (Accuracy, Precision, Recall). Our React dashboard displays a "Differential Diagnosis", allowing physicians to compare classical vs. quantum consensus simultaneously.

---

## 4. Application Explanation (Detailed Technical Guide)

If the panel asks you to explain the exact technology stack, how the app runs, and "what is what," use this section.

### A. What is What? (The Tech Stack)
- **VS Code:** Our primary development IDE.
- **Frontend (React + Vite + Node.js):** The visual dashboard. It runs in the user's browser, provides forms, and generates charts using `Recharts`.
- **Backend (FastAPI + Uvicorn):** The Python server acting as the "brain." It receives the data from the frontend, processes it, and returns the AI predictions.
- **Scikit-Learn:** The Python library powering our classical models (Random Forest, SVM, Logistic Regression).
- **Qiskit & Qiskit Aer:** IBM's open-source SDK for quantum computing. `Aer` is the simulator that mimics quantum hardware on our standard computers.

### B. Commands to Run the Application

The application requires two separate terminal windows (one for the Backend, one for the Frontend).

#### Step 1: Start the Backend (FastAPI + Machine Learning Engine)
The backend must run to process the predictions.

1. **Open a terminal and navigate to the backend folder:**
   ```bash
   cd path/to/mini-qunatum/backend
   ```
2. **Activate the Python Virtual Environment:** (This ensures we use the isolated packages installed for this project, avoiding version conflicts).
   ```bash
   venv\Scripts\activate   # (On Windows)
   ```
3. **Start the FastAPI Server:**
   ```bash
   python main.py
   ```
   *Explanation:* This command triggers `uvicorn` to spin up our FastAPI server on `http://localhost:8000`. The server loads `heart.csv`, initializes the classical and quantum model pipelines, and opens the `/predict` API endpoint to listen for incoming data.

#### Step 2: Start the Frontend (React Dashboard)
Leave the backend running, open a **second** terminal.

1. **Navigate to the frontend folder:**
   ```bash
   cd path/to/mini-qunatum/frontend
   ```
2. **Start the Vite Development Server:**
   ```bash
   npm run dev
   ```
   *Explanation:* This command starts the Node.js server that hosts our React application. It binds to `http://localhost:5173`. 
   
#### Step 3: How they connect
When you click "Predict" on the frontend, Axios (an HTTP client) sends a `POST` request to `http://localhost:8000/predict`. The backend processes this JSON payload through `MLEngine`, calculates the results (using either Scikit-learn or simulating Qiskit), and returns a JSON response which the React frontend parses to draw the Recharts visualizations.

*(Note: Quantum predictions simulated on classical hardware take slightly longer, which is why we have extended our API timeouts).*
