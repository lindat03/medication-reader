import React, { useState } from 'react';
import './App.css'; // Import your CSS file

function App() {
    const [ocrText, setOcrText] = useState('');
    const [medicationList, setMedicationList] = useState('');
    const [selectedFile, setSelectedFile] = useState(null);
    const handleFileChange = (e) => {
        setSelectedFile(e.target.files[0]);
    };

    const handleSave = () => {
        if (ocrText) {
            setMedicationList([...medicationList, ocrText+'\n\n']);
        }
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
                console.log("HEREEEE");
                console.log(data.text);
            } else {
                console.error('Failed to upload image.');
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <div className="app-container">
          <div className="header-container">
            <img src="https://cdn.discordapp.com/attachments/1147324798725279895/1152957413297758359/image.png" alt="Logo" />
            <h1>Shifa</h1>
          </div>
          <div className="body-container">
            <div className="left-side">
                <h1 className='titles-scan'>New Scan</h1>
                <input type="file" accept="image/*" onChange={handleFileChange} />
                <center><button onClick={handleUpload}>Upload</button></center>
                    <div className="ocr-result">
                        <p>{ocrText}</p>
                        <center><button onClick={handleSave}>Save to my list</button></center>
                </div>
            </div>
            <div className="right-side">
                    <h1 className='titles'>My Medications</h1>
                    <p>{medicationList}</p>
            </div>
          </div>
        </div>
    );
}

export default App;