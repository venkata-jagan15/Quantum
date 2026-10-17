import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Activity, Shield, TrendingUp } from 'lucide-react';

const LandingPage = () => {
    const navigate = useNavigate();

    return (
        <div className="landing-page">
            <header className="hero-section">
                <div className="hero-content">
                    <h1>Quantum vs Classical Heart Disease Prediction Platform</h1>
                    <p className="subtitle">Exploring the frontier of machine learning accuracy and computational power for critical medical diagnoses.</p>
                    <button className="btn-predict glow-effect huge-btn" onClick={() => navigate('/form')}>
                        START PREDICTION
                    </button>
                </div>
            </header>

            <section className="info-section">
                <h2>Why Comparison is Important</h2>
                <div className="cards-grid">
                    <div className="card info-card">
                        <Activity className="icon" size={32} color="#00f2ff" />
                        <h3>Medical Reliability</h3>
                        <p>In healthcare, a false negative can be fatal. Comparing models ensures we identify the one with the highest recall for risk detection.</p>
                    </div>
                    <div className="card info-card">
                        <Shield className="icon" size={32} color="#7000ff" />
                        <h3>Quantum Advantage</h3>
                        <p>Quantum algorithms can uncover complex non-linear correlations in patient health data that classical approaches might miss.</p>
                    </div>
                    <div className="card info-card">
                        <TrendingUp className="icon" size={32} color="#ffcc00" />
                        <h3>Performance Trade-offs</h3>
                        <p>Evaluate exact training times versus predictive probability metrics across Logistic Regression, Random Forest, SVM, QSVM, and VQC models.</p>
                    </div>
                </div>
            </section>
        </div>
    );
};

export default LandingPage;
