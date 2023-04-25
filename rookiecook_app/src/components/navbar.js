import React from "react";
import { Link } from "react-router-dom";
import { useNavigate } from 'react-router-dom';


const Navbar = () => {

  const navigate = useNavigate();

  const handleGoBack = () => {
    navigate(-1);

  };


  return (
    <>
      <nav className="navbar navbar-expand-lg">
        <div className="container-fluid">
          <Link className="navbar-brand" to="/">
            RookieCook
          </Link>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <Link className="nav-link active" aria-current="page" to="#">
                  About Us
                </Link>
              </li>
            </ul>
            <button id = "nav-btn" className="button" onClick={handleGoBack}
             style={{position: "relative", left: "90%", borderRadius: "20px", boxShadow: "0 0 10px rgba(59, 58, 0, 0.795)", border: "none"}}><i className="fa fa-arrow-left" aria-hidden="true"></i></button>

          </div>
        </div>
      </nav>
    </>
  );
};

export default Navbar;
