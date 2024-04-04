import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Main from './pages/Main.js'; 
import { Output } from './pages/Output.js';
import { Login } from './pages/Login.js';


export const Paths = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" exact element={<Main />} />
                <Route path="/login" element={<Login />} />
                <Route path="/output" element={<Output />} />
            </Routes>
        </Router>
    );
}