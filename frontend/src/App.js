import React, { useState } from 'react';
import "./App.css";

function App() {
    const [ocrText, setOcrText] = useState('');
    const [selectedFile, setSelectedFile] = useState(null);

    const handleFileChange = (e) => {
        setSelectedFile(e.target.files[0]);
    };

    const handleUpload = async () => {
        const formData = new FormData();
        formData.append('image', selectedFile);

        try {
            const response = await fetch('http://localhost:5000/upload', {
                method: 'POST',
                body: formData,
            });

            if (response.ok) {
                const data = await response.json();
                setOcrText(data.text);
                console.log(data.text);
            } else {
                console.error('Failed to upload image.');
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <div className="App">
            <h1 className="header-title">Shifa</h1>
            <div className="upload-container">
                <h1>Upload Medication Label</h1>
                <input type="file" accept="image/*" onChange={handleFileChange} />
                <button onClick={handleUpload}>Upload Image</button>
                <div>
                    <h2>Medication Information:</h2>
                    <p>{ocrText}</p>
                </div>
            </div>

        </div>
    );
}

export default App;