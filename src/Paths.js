import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Main from './pages/Main.js'; 
import { Output } from './pages/Output.js';
import { Input } from './pages/Input.js';


export const Paths = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" exact element={<Main />} />
                <Route path="/input" element={<Input />} />
                <Route path="/output" element={<Output />} />
            </Routes>
        </Router>
    );
}