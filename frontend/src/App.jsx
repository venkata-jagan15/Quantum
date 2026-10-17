import React from 'react';
import { Routes, Route } from 'react-router-dom';
import LandingPage from './pages/LandingPage';
import PatientForm from './pages/PatientForm';
import ComparisonDashboard from './pages/ComparisonDashboard';
import './index.css';

const App = () => {
    return (
        <div className="app-container app-theme-dark">
            <Routes>
                <Route path="/" element={<LandingPage />} />
                <Route path="/form" element={<PatientForm />} />
                <Route path="/dashboard" element={<ComparisonDashboard />} />
            </Routes>
        </div>
    );
};

export default App;
