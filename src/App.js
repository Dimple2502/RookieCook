import './App.css';
import { Routes, Route } from "react-router-dom";
import "./css/style.css";
import Home from './components/home';
import Logo from './components/logo';
import Navbar from './components/navbar';
import Object from './components/object';
import Weather from './components/weather';
import Recipe from './components/recipe';

function App() {
  return (
    <>
    <Navbar/>
      <Routes>      
          <Route path="/l" element={<Logo/>} />          
          <Route path="/" element={<Home/>} />          
          <Route path="/recipe" element={<Recipe/>} />          
          <Route path="/weather" element={<Weather/>} />          
          <Route path="/object" element={<Object/>} />          
        </Routes>
    </>
  );
}

export default App;
