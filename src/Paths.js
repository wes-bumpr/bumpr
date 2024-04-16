import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Main from './pages/Main.js'; 
import { Output } from './pages/Output.js';
import { Login } from './pages/Login.js';


export const Paths = () => {
    return (
        <Router>
            <Routes>
                <Route path="/login" element={<Login />} />
                <Route path="/home" exact element={<Main />} />
                <Route path="/output" element={<Output />} />
                <Route path="/" element={<Navigate to="/login" />} />
            </Routes>
        </Router>
    );
}