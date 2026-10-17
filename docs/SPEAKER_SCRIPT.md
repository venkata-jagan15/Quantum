# Mini-Quantum: Detailed Speaker Script

This document contains the exact speaking script for the mini-project review. It is divided by team member so each person knows exactly when and what to speak. 

---

## 🎤 Member 1: Introduction, Frontend & UI, Literature (Papers 1-3)

**[Slide: Title Slide]**
**Member 1:** "Good morning/afternoon respected panel members. We are here to present our mini-project titled **'Comparative Analysis of Classical and Quantum-Assisted Machine Learning Models for Early Heart Disease Prediction'**. We are a team of 4, guided by Dr. V. Vasudha Rani. I will begin by introducing the project, our abstract, and my specific contributions, followed by my portion of the literature review."

**[Slide: Abstract]**
**Member 1:** "Heart disease is a leading cause of mortality worldwide. While traditional machine learning techniques are widely used for prediction, they often struggle with highly complex medical data. In this project, we conducted a comparative study to evaluate classical classifiers—specifically Logistic Regression, Random Forest, and Support Vector Machine—against cutting-edge Quantum-Assisted models, namely the Quantum Support Vector Machine (QSVM) and Variational Quantum Classifier (VQC). We pre-processed clinical data and evaluated these models using standard metrics like accuracy, precision, and F1-score to see if quantum approaches offer a complementary advantage."

**[Slide: Technical Contribution - Frontend]**
**Member 1:** "For my technical contribution, I was responsible for the **Frontend Architecture and UI/UX design**. I developed the client-side interface using React and Vite, implementing a modern 'Glassmorphism' dark-mode aesthetic. I also integrated Recharts for real-time data visualization and utilized Axios to securely transmit patient data payloads to our backend for prediction."

**[Slide: Literature Review 1]**
**Member 1:** "Moving to the literature survey, I reviewed three key papers:
1. The first paper from 2025 focuses on a hybrid framework for heart disease prediction. The main research gap identified here is that existing models struggle with large numbers of features, which reduces interpretability and accuracy.
2. The second paper discusses a comparative analysis of logistic regression, SVM, and random forest. It highlights that robust cross-validation strategies in this domain are still underexplored.
3. The third paper, 'QuCardio', applies Quantum Machine Learning for cardiovascular diseases using ECG images. It points out the limited prior work on multi-class QML classification."

**Member 1:** "I will now hand it over to Member 2 to discuss the Backend Architecture and their literature review."

---

## 🎤 Member 2: Backend Architecture, Preprocessing, Literature (Papers 4-6)

**[Slide: Technical Contribution - Backend]**
**Member 2:** "Thank you. My name is [Your Name], and my technical contribution focused on the **Backend Architecture and Data Processing**. I built a robust Python server using FastAPI and Uvicorn. Our architecture acts as a 'Modular Router'—when patient data is received, the `MLEngine` core routes the prediction task to either the Classical or the Quantum domains. Additionally, I handled the crucial data preprocessing phase, which involved data validation using Pydantic and applying Z-Score Normalization using `StandardScaler` to ensure all numerical inputs are properly scaled for our distance-based models."

**[Slide: Architecture Flow]**
**Member 2:** "To briefly explain the flow: The frontend sends a JSON payload to our FastAPI `/predict` endpoint. The backend validates this data, processes the features from our `heart.csv` dataset, and triggers the respective machine learning pipelines. Finally, the consensus of the predictions is returned to the frontend."

**[Slide: Literature Review 2]**
**Member 2:** "For my portion of the literature survey, I focused on the application of Quantum Enhanced Machine Learning:
4. The fourth paper proposes a Quantum K-means clustering method. It addresses the gap that classical ML faces computational bottlenecks on larger data.
5. The fifth paper discusses revolutionizing prediction with quantum-enhanced ML. It reinforces that traditional algorithms suffer heavily when processing highly complex medical datasets.
6. The sixth paper evaluates multiple classifiers like GridSearchCV and Random Forest, pointing out that existing models lack optimal hyperparameter tuning for high-dimensional clinical data."

**Member 2:** "I will now pass the presentation to Member 3, who will explain the Classical Machine Learning methodology."

---

## 🎤 Member 3: Classical ML Methodology, Literature (Papers 7-9)

**[Slide: Technical Contribution - Classical ML]**
**Member 3:** "Thank you. I am [Your Name], and my technical role was the **Integration of the Classical Machine Learning Models**. I developed the classical branch of our `MLEngine` using the Scikit-Learn library. I successfully implemented Logistic Regression, Random Forest, and Support Vector Machines (SVM). I also designed the evaluation logic, which benchmarks the performance of these classical algorithms against the quantum models using metrics like Accuracy, Precision, Recall, and F1-Score. In our findings, Random Forest acted as a strong ensemble method, performing exceptionally well on the full feature set."

**[Slide: Literature Review 3]**
**Member 3:** "For my literature review, I looked into the historical and practical challenges of ML in healthcare:
7. Paper seven focuses on early prediction using historical medical data. The research gap here is the scalability issue in healthcare and the difficulty in making decisions based on discrete medical data.
8. Paper eight assesses seven different ML classifiers. It highlights the urgent real-world need for efficient predictive models to detect heart disease early due to limited healthcare facilities globally.
9. Paper nine directly compares Quantum Neural Networks (QNN) and QSVMs. It identifies that classical ML often struggles with imbalanced healthcare data, resulting in biased models. Quantum models, however, can exploit higher-dimensional Hilbert spaces for better pattern detection."

**Member 3:** "I will now invite Member 4 to discuss the Quantum ML Methodology, our application execution, and the conclusion."

---

## 🎤 Member 4: Quantum ML Methodology, Application Demo, Literature (Papers 10-12), Conclusion

**[Slide: Technical Contribution - Quantum ML]**
**Member 4:** "Thank you. I am [Your Name], and my primary technical contribution was spearheading the **Quantum Machine Learning Integration**. Due to the current hardware constraints of quantum computers, we cannot process all 13 clinical features directly. Therefore, I implemented Principal Component Analysis (PCA) to compress the features into a smaller state space suitable for quantum registers. I then developed the Variational Quantum Classifier (VQC) and the Quantum Support Vector Machine (QSVM) utilizing Qiskit. These quantum circuits were simulated locally using the Qiskit Aer simulator."

**[Slide: Literature Review 4]**
**Member 4:** "My literature review focused strictly on the frontier of quantum applications:
10. Paper ten proposes a prediction system integrating quantum technology, highlighting the gap that there are very few practical implementations evaluated on real-world clinical datasets.
11. Paper eleven proposes an AI-driven preventive healthcare framework using quantum computing, noting that classical AI struggles to capture complex feature interactions.
12. Paper twelve evaluates QNN and QSVM for imbalanced datasets like heart failure and diabetes, proving that QSVM can capture complex non-linear patterns that classical models miss."

**[Slide: Application Explanation]**
**Member 4:** "Before we conclude, I would like to briefly explain how our application runs. Our architecture requires two parallel processes. First, we start our Python Backend by activating a virtual environment and running `python main.py` to spin up the FastAPI server on port 8000. Second, we start our React Frontend by running `npm run dev` to launch the dashboard on port 5173. When a doctor inputs data on the UI and clicks predict, the frontend communicates with the backend via REST API, the models process the data (with quantum models running via simulator), and the results are rendered dynamically on the screen."

**[Slide: Conclusion]**
**Member 4:** "To conclude, our comparative analysis shows that while classical models like Random Forest perform robustly, quantum-assisted models like VQC and QSVM show highly competitive performance, particularly in capturing non-linear relationships in reduced feature spaces. Despite current quantum hardware limitations, this project proves the massive potential of quantum-assisted learning as a complementary tool in intelligent healthcare. Thank you, the panel is now welcome to ask questions."
