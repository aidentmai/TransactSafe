import { createContext, useContext, useEffect, useState } from "react";
import { is_authenticated } from "../endpoints/api";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [loading, setLoading] = useState(true);
  const get_authenticated = async () => {
    try {
      const success = await is_authenticated();
      setIsAuthenticated(success);
    } catch {
      setIsAuthenticated(false);
    } finally {
      setLoading(false);
    }
  };

  const setLoginState = () => {
    setIsAuthenticated(true);
  };

  const setLogoutState = () => {
    setIsAuthenticated(false);
  };

  useEffect(() => {
    get_authenticated();
  }, []);
  return (
    <AuthContext.Provider value={{ isAuthenticated, loading, setLoginState, setLogoutState }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
