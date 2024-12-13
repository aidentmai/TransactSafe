// UploadFile.jsx
import { useState } from 'react';
import axios from 'axios';
import PredictionResults from './PredictionResults';
import { preprocess } from '../endpoints/api';

const UploadFile = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [predictions, setPredictions] = useState(null); // To store the prediction results

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
  };

  const handleUpload = async () => {
    if (selectedFile) {
      const res = await preprocess(selectedFile);
        // Assuming the backend returns a list of predictions
        setPredictions(res.data.predictions);  // Set predictions in state

        alert(res.data.message || 'File uploaded and analyzed successfully!')
    } else {
      alert('No file selected');
    }
  };

  return (
    <div className="m-24 ml-[700px] mr-[700px]">
      <label className="block mb-1 text-xs font-medium text-gray-900" htmlFor="file_input">
        Upload file
      </label>
      <div className="flex items-center space-x-2">
        <input
          className="block w-full text-xs text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 p-1"
          id="file_input"
          type="file"
          onChange={handleFileChange}
        />
        <button
          className="text-white bg-blue-700 hover:bg-blue-800 font-medium rounded-lg text-sm px-4 py-2"
          onClick={handleUpload}
        >
          Analyze
        </button>
      </div>

      {/* Render PredictionResults if predictions exist */}
      {predictions && <PredictionResults predictions={predictions} />}
    </div>
  );
};

export default UploadFile;
