import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Main from './pages/Main.js'; 
import { Login } from './pages/Login.js';


export const Paths = () => {
    return (
        <Router>
            <Routes>
                <Route path="/login" element={<Login />} />
                <Route path="/home" exact element={<Main />} />
                <Route path="/" element={<Navigate to="/login" />} />
            </Routes>
        </Router>
    );
}