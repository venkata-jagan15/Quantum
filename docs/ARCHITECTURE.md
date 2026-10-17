# Mini-Quantum: Master System Architecture

This document outlines the high-level architecture of the **Mini-Quantum** hybrid ML platform, showing the interaction between the React frontend, FastAPI service, and the dual-stream machine learning engine.

## 1. High-Level Technical Architecture

```mermaid
graph TD
    subgraph "Frontend Layer (React + Vite)"
        UI["Visual Dashboard"]
        Recharts["Recharts (Visualization)"]
        Axios["Axios (HTTP Client)"]
        Lucide["Lucide Icons (UI Elements)"]
    end

    subgraph "Service Layer (FastAPI)"
        API["FastAPI Entrypoint"]
        Cors["CORS Middleware"]
        Pydantic["Data Validation"]
    end

    subgraph "Hybrid Science Engine (Python)"
        Engine["MLEngine Orchestrator"]
        Preprocessor["PCA Dimensionality Reduction"]
        
        subgraph "Classical Pipeline (Scikit-Learn)"
            M1["Logistic Regression"]
            M2["Random Forest (200 Trees)"]
            M3["SVM (RBF Kernel)"]
        end
        
        subgraph "Quantum Subsystem (Qiskit)"
            M4["QSVM (Kernel Feature Mapping)"]
            M5["VQC (Variational Learning)"]
            Sim["Aer Simulator (Local CPU)"]
        end
    end

    %% Flow of Data
    UI --> Recharts
    UI --> Axios
    Axios -- "Parallel POST /predict" --> API
    API --> Pydantic
    Pydantic --> Engine
    Engine --> Preprocessor
    
    %% Processing Paths
    Preprocessor -- "13 Features (Scaled)" --> M1 & M2 & M3
    Preprocessor -- "Reduced 2D/3D (PCA)" --> M4 & M5
    M4 & M5 --> Sim

    %% Results
    M1 & M2 & M3 & M4 & M5 -- "Prediction + Prob" --> Engine
    Engine --> API
    API -- "JSON Response (200 OK)" --> Axios
    Axios --> UI
```

## 2. Tiered System Breakdown

### A. Presentation Tier
- **Technology**: React v18, Vite.
- **Responsibility**: User interface, data input for patient features, and data visualization.
- **Parallelization Strategy**: Axios fires all model prediction requests simultaneously to prevent the slow quantum simulations from blocking the fast classical models.

### B. Logic Tier (MLEngine)
- **Technology**: Python, FastAPI.
- **Responsibility**: Orchestrating the "Hybrid Split." 
- **PCA Dimensionality Reduction**: Crucial for quantum algorithms, which cannot yet handle high-dimensional data (13 features) on classical hardware/simulators.

### C. Science Tier (The Models)
- **Classical**: Logistic Regression, Random Forest (200 trees, max depth 5), SVM.
- **Quantum**: QSVM with Fidelity Kernel (3D PCA), VQC with RealAmplitudes Ansatz (2D PCA).
- **Simulation Layer**: Qiskit Aer allows us to run these complex quantum gates on standard binary CPUs.
