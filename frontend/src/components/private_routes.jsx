import { useEffect } from 'react';
import { useAuth } from "../context/useAuth";
import { useNavigate } from "react-router-dom";

const PrivateRoute = ({ children }) => {
  const { isAuthenticated, loading } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    if (!loading && !isAuthenticated) {
      //navigate('/login');
    }
  }, [loading, isAuthenticated, navigate]);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (isAuthenticated) {
    return children;
  }

  return null; // Return null if not authenticated and not loading
};

export default PrivateRoute;