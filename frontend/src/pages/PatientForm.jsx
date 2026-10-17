import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Activity, Info } from 'lucide-react';

const PatientForm = () => {
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        age: 52, sex: 1, cp: 0, trestbps: 125, chol: 212, fbs: 0,
        restecg: 1, thalach: 168, exang: 0, oldpeak: 1.0, slope: 2,
        ca: 2, thal: 3
    });

    const [errors, setErrors] = useState({});

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({ ...prev, [name]: parseFloat(value) }));
        if (errors[name]) {
            setErrors(prev => ({ ...prev, [name]: null }));
        }
    };

    const validateForm = () => {
        const newErrors = {};
        if (formData.age < 1 || formData.age > 120) newErrors.age = "Age must be between 1 and 120";
        if (formData.trestbps < 50 || formData.trestbps > 300) newErrors.trestbps = "BP must be between 50 and 300 mm Hg";
        if (formData.chol < 50 || formData.chol > 600) newErrors.chol = "Cholesterol must be realistic (50-600 mg/dl)";
        if (formData.thalach < 50 || formData.thalach > 250) newErrors.thalach = "Max HR must be realistic (50-250 bpm)";
        if (formData.oldpeak < 0 || formData.oldpeak > 10) newErrors.oldpeak = "ST depression must be between 0 and 10";

        setErrors(newErrors);
        return Object.keys(newErrors).length === 0;
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (validateForm()) {
            navigate('/dashboard', { state: { formData } });
        }
    };

    const inputFields = [
        { name: 'age', label: 'Age', type: 'number', tooltip: 'Patient age in years' },
        { name: 'sex', label: 'Sex', type: 'select', options: [{ value: 1, label: 'Male' }, { value: 0, label: 'Female' }], tooltip: 'Biological sex parameter' },
        { name: 'cp', label: 'Chest Pain Type', type: 'select', options: [{ value: 0, label: 'Typical Angina' }, { value: 1, label: 'Atypical Angina' }, { value: 2, label: 'Non-anginal Pain' }, { value: 3, label: 'Asymptomatic' }], tooltip: 'Type of chest pain medically experienced' },
        { name: 'trestbps', label: 'Resting Blood Pressure', type: 'number', tooltip: 'Resting blood pressure in mm Hg' },
        { name: 'chol', label: 'Serum Cholestoral', type: 'number', tooltip: 'Serum cholestoral measured in mg/dl' },
        { name: 'fbs', label: 'Fasting Blood Sugar > 120 mg/dl', type: 'select', options: [{ value: 0, label: 'False' }, { value: 1, label: 'True' }], tooltip: 'Indicates if fasting blood sugar is elevated' },
        { name: 'restecg', label: 'Resting ECG Results', type: 'select', options: [{ value: 0, label: 'Normal' }, { value: 1, label: 'ST-T Wave Abnormality' }, { value: 2, label: 'Left Ventricular Hypertrophy' }], tooltip: 'Electrocardiographic profile at rest' },
        { name: 'thalach', label: 'Max Heart Rate Achieved', type: 'number', tooltip: 'Maximum heart rate recorded during exercise test' },
        { name: 'exang', label: 'Exercise Induced Angina', type: 'select', options: [{ value: 0, label: 'No' }, { value: 1, label: 'Yes' }], tooltip: 'Did exercise induce chest pain?' },
        { name: 'oldpeak', label: 'ST Depression (Oldpeak)', type: 'number', step: 0.1, tooltip: 'ST depression induced by exercise relative to rest' },
        { name: 'slope', label: 'ST Segment Slope', type: 'select', options: [{ value: 0, label: 'Upsloping' }, { value: 1, label: 'Flat' }, { value: 2, label: 'Downsloping' }], tooltip: 'The slope of the peak exercise ST segment' },
        { name: 'ca', label: 'Number of Major Vessels', type: 'select', options: [{ value: 0, label: '0' }, { value: 1, label: '1' }, { value: 2, label: '2' }, { value: 3, label: '3' }, { value: 4, label: '4' }], tooltip: 'Vessels colored by flourosopy' },
        { name: 'thal', label: 'Thalassemia', type: 'select', options: [{ value: 0, label: '1' }, { value: 1, label: '2' }, { value: 2, label: '3' }, { value: 3, label: '0' }], tooltip: 'Presence of Thalassemia blood disorders' },
    ];

    return (
        <div className="form-page">
            <div className="card form-card">
                <div className="form-header header">
                    <h2><Activity size={24} color="#00f2ff" style={{ marginRight: '10px' }} /> Patient Diagnostic Data</h2>
                    <p style={{ marginTop: '10px', color: '#aaa' }}>Enter the clinical parameters to perform the advanced quantum vs classical comparison.</p>
                </div>

                <form onSubmit={handleSubmit} className="patient-form">
                    <div className="form-grid">
                        {inputFields.map((field) => (
                            <div key={field.name} className="field form-field-container">
                                <label className="field-label">
                                    {field.label}
                                    <div className="tooltip-container">
                                        <Info size={14} color="#888" className="info-icon" />
                                        <div className="tooltip-text">{field.tooltip}</div>
                                    </div>
                                </label>

                                {field.type === 'select' ? (
                                    <select
                                        name={field.name}
                                        value={formData[field.name]}
                                        onChange={handleInputChange}
                                        className={`glass-input ${errors[field.name] ? 'input-error' : ''}`}
                                    >
                                        {field.options.map(opt => (
                                            <option key={opt.value} value={opt.value} style={{ color: '#000' }}>{opt.label}</option>
                                        ))}
                                    </select>
                                ) : (
                                    <input
                                        type="number"
                                        name={field.name}
                                        value={formData[field.name]}
                                        onChange={handleInputChange}
                                        step={field.step || 1}
                                        className={`glass-input ${errors[field.name] ? 'input-error' : ''}`}
                                    />
                                )}
                                {errors[field.name] && <span className="error-message">{errors[field.name]}</span>}
                            </div>
                        ))}
                    </div>

                    <div className="form-actions" style={{ marginTop: '40px', textAlign: 'center' }}>
                        <button type="submit" className="btn-predict glow-effect huge-btn">
                            👉 COMPARE MODELS
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
};

export default PatientForm;
