const PredictionResults = ({ predictions }) => {
  if (!predictions) return null;  // Don't render if there are no predictions

  return (
    <div className="prediction-results">
      <h2>Prediction Results</h2>
      <table className="w-full table-auto border-collapse">
        <thead>
          <tr>
            <th className="px-4 py-2 border">Transaction ID</th>
            <th className="px-4 py-2 border">Prediction (Fraud Score)</th>
          </tr>
        </thead>
        <tbody>
          {predictions.map((prediction, index) => (
            <tr key={index}>
              <td className="px-4 py-2 border">{prediction.trans_num}</td>
              <td className="px-4 py-2 border">{prediction.fraud_score}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default PredictionResults;
