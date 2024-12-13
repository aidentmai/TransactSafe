import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./routes/login";
import Home from "./routes/home";
import Register from "./routes/register";
import Dashboard from "./routes/dashboard";
import { AuthProvider } from "./context/useAuth";
import PrivateRoute from "./components/private_routes";

function App() {
  return (
    <Router future={{ v7_startTransition: true, v7_relativeSplatPath: true }}>
      <AuthProvider>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/dashboard" element={<PrivateRoute><Dashboard /></PrivateRoute>} />
        </Routes>
      </AuthProvider>
    </Router>
  );
}

export default App;
