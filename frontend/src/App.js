import React,{useState} from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import 'primereact/resources/themes/md-dark-indigo/theme.css';
import 'primereact/resources/primereact.min.css';
import 'primeicons/primeicons.css';
import 'primeflex/primeflex.css';
import './App.css';

import ProjectPage from './views/ProjectsPage';
import TemplatesPage from './views/TemplatesPage'
import HomePage from './views/HomePage';  // New import

const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(true);
  return (
    <div className="App">
      <Router>

        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/projects" element={<ProjectPage />} />
          <Route path="/templates" element={<TemplatesPage />} />
        </Routes>
      </Router>
    </div>
  );
};

export default App;
