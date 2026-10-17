# Mini-Quantum: Prediction Lifecycle Flow

This document tracks the journey of a single patient diagnosis request, highlighting the parallel execution of classical and quantum tasks.

## Full Prediction Flow Chart

```mermaid
flowchart TD
    %% Styling
    classDef start fill:#00f2ff,stroke:#00f2ff,color:#000,stroke-width:2px;
    classDef process fill:#111,stroke:#00f2ff,color:#fff,stroke-width:1px;
    classDef quantum fill:#ffcc00,stroke:#ffcc00,color:#000,stroke-width:2px;
    classDef decision fill:#7000ff,stroke:#7000ff,color:#fff,stroke-width:1px;
    classDef error fill:#ff4d4d,stroke:#ff4d4d,color:#fff,stroke-width:1px;

    Start((User Submits Form)):::start --> Capture[React Captures Patient Features]:::process
    Capture --> API[Axios: Parallel POST /api/predict]:::process
    
    API --> FastAPI{FastAPI Entrypoint}:::decision
    
    FastAPI -- "model_type: Classical" --> ScaleC[StandardScaler]:::process
    ScaleC --> SKLearn[Scikit-Learn: Fit & Predict]:::process
    SKLearn --> ResultC[Prepare JSON Response]:::process
    
    FastAPI -- "model_type: Quantum" --> ScaleQ[StandardScaler]:::process
    ScaleQ --> PCA[PCA Dimensionality Reduction]:::quantum
    PCA --> Qiskit[Build Quantum Circuit]:::quantum
    Qiskit --> Aer[Aer Simulator: Run Circuit]:::quantum
    
    Aer -- "Success" --> ResultQ[Extract Counts & Probability]:::process
    Aer -- "Simulation Error" --> Error[FastAPI: Return 500 Error]:::error
    
    ResultC & ResultQ --> Return[HTTP 200: JSON Payload]:::process
    Return --> Update[React: Update Model Row & Recharts]:::process
    Error --> DashErr[React: Show 'Failed to Compute']:::error
    
    Update & DashErr --> End((Dashboard Updated)):::start

    %% Subgraphs for visual grouping
    subgraph "Presentation Layer"
        Capture
        Update
        DashErr
    end

    subgraph "Hybrid Intelligence Engine"
        ScaleC
        SKLearn
        ScaleQ
        PCA
        Qiskit
        Aer
    end
```

## Key Technical Details

### 1. The Parallelization Strategy
- **Frontend**: The `ComparisonDashboard.jsx` uses a `forEach` loop with `async/await` to fire requests for all 5 models simultaneously. This means the total wait time is governed by the *slowest* model (VQC), rather than the *sum* of all models.

### 2. The Dimensionality Gap (PCA)
- **Problem**: Quantum simulators take exponential time for every added feature.
- **Solution**: The architecture includes a **PCA (Principal Component Analysis)** step that compresses the 13 patient features into **2 or 3 essential dimensions** (qubits) for quantum processing.

### 3. Graceful Error Resilience
- If a quantum simulation fails (e.g., due to a memory limit on the local machine), the FastAPI backend catches the exception and returns a **500 error**.
- The React dashboard is programmed to catch these errors *per-model*, allowing the rest of the dashboard to stay functional.
