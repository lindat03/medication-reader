import React, { useState } from 'react';
import './App.css'; // Import your CSS file

function App() {
    const [ocrText, setOcrText] = useState('');
    const [medicationList, setMedicationList] = useState('');
    const [selectedFile, setSelectedFile] = useState(null);
    const [uploadedImage, setUploadedImage] = useState(null);
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
          <div className="left-side">
            <h1>New Scan</h1>
            <input type="file" accept="image/*" onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload</button>
                <div className="ocr-result">
                    {uploadedImage && <img src={uploadedImage} alt="Uploaded" />}
                    <p>{ocrText}</p>
                    <center><button onClick={handleSave}>Save to my list</button></center>
            </div>
          </div>
          <div className="right-side">
                <h1>My Medications</h1>
                <p>{medicationList}</p>
          </div>
      </div>
    );
}

export default App;