# Mini-Quantum: Hybrid Machine Learning Dashboard

This project is a web-based dashboard and API that compares the performance of Classical Machine Learning models against Quantum Machine Learning models for disease prediction based on patient features.

## 🚀 Tech Stack

### Frontend (Client)
- **Framework:** React + Vite
- **Routing:** React Router DOM
- **Data Visualization:** Recharts
- **Icons:** Lucide React
- **HTTP Client:** Axios
- **Styling:** Vanilla CSS (Custom modern Glassmorphism UI)

### Backend (Server & ML Engine)
- **Framework:** FastAPI
- **Server:** Uvicorn
- **Classical ML Models:** Scikit-Learn (`LogisticRegression`, `RandomForestClassifier`, `SVC`)
- **Quantum ML Models:** Qiskit, Qiskit-Aer, Qiskit Machine Learning (`FidelityQuantumKernel`, `VQC`, `RealAmplitudes`, `ZZFeatureMap`)
- **Data Processing:** Pandas, NumPy
- **Dataset:** Heart disease dataset (`heart.csv`)

---

## 🛠️ Step-by-Step Guide to Run the Project

You will need to run both the Backend API and the Frontend React app simultaneously in two separate terminal windows.

### 1. Running the Backend (FastAPI + Quantum ML)

Open your first terminal and follow these steps:

1. **Navigate to the backend directory:**
   ```bash
   cd path/to/mini-qunatum/backend
   ```

2. **Create a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **Mac/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install the required Python dependencies:**
   ```bash
   pip install fastapi uvicorn pydantic scikit-learn pandas numpy qiskit qiskit-aer qiskit-machine-learning qiskit-algorithms
   ```

5. **Start the FastAPI server:**
   ```bash
   python main.py
   ```
   *The backend will now be running at `http://localhost:8000`.*

---

### 2. Running the Frontend (React + Vite)

Open a **second** terminal window and follow these steps:

1. **Navigate to the frontend directory:**
   ```bash
   cd path/to/mini-qunatum/frontend
   ```

2. **Install Node.js dependencies:**
   ```bash
   npm install
   ```
   *(Wait for all the `node_modules` to finish downloading)*

3. **Start the Vite development server:**
   ```bash
   npm run dev
   ```
   *The frontend will typically be accessible at `http://localhost:5173`. Open this URL in your browser to access the application.*

---

## 💡 Notes
- The Vite frontend is configured to automatically proxy `/api` requests to `http://localhost:8000`, so you do not need to worry about CORS issues during local development.
- Quantum models (like VQC) are simulated on classical hardware, meaning their initial training/prediction phase may take longer than classical models. We have configured the API timeout to 5 minutes to accommodate this.

---

## 📚 Technical Documentation
For a deep dive into the system architecture and individual model logic, refer to the following guides:

- **[System Architecture](docs/ARCHITECTURE.md)**: High-level overview of the multi-tier hybrid engine.
- **[Model Workflows](docs/MODEL_WORKFLOWS.md)**: Detailed step-by-step logic and flowcharts for each of the 5 ML models.
- **[Academic Flowcharts (Horizontal)](docs/ACADEMIC_HORIZONTAL_GALLERY.md)**: Professional, horizontal PNG diagrams for research papers.
- **[Algorithm Visual Gallery](docs/ALGORITHM_GALLERY.md)**: High-fidelity visualizations of each model's internal logic.
- **[Prediction Data Flow](docs/DATA_FLOW.md)**: Lifecycle of a single prediction request from frontend to backend.
