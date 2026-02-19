import { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return alert("Please select a PDF");

    // Standard JavaScript FormData - this is how we send files over HTTP
    const formData = new FormData();
    formData.append("file", file);
   

    setLoading(true);
    try {
      // Talking to our Python Backend (FastAPI)
      const response = await axios.post("http://127.0.0.1:8000/upload-resume", formData);
      setResult(response.data);
      setFile(null);
    } catch (error) {
      console.error("Upload failed", error);
      alert("Error uploading file. Check if Python server is running!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '40px', maxWidth: '600px', margin: 'auto' }}>
      <h1>Urban Logic AI</h1>
      <p>Upload a resume to see Python process the PDF bytes.</p>
      
      <input 
        type="file" 
        accept=".pdf" 
        // This line ensures that when setFile(null) is called, the text clears!
        value={file ? undefined : ""} 
        onChange={(e) => setFile(e.target.files[0])} 
      />
      
      <button onClick={handleUpload} disabled={loading} style={{ marginLeft: '10px' }}>
        {loading ? "Processing..." : "Upload to Python"}
      </button>

      {result && (
        <div style={{ marginTop: '20px', background: '#222', color: '#fff', padding: '20px', borderRadius: '8px' }}>
          <h3>Extracted from PDF:</h3>
          <pre style={{ whiteSpace: 'pre-wrap' }}>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;