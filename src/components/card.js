import React from 'react';
import { useParams,useNavigate } from "react-router-dom";

const Card = (props) => {
  const navigate = useNavigate();
  const { image, title, desc } = props;

  return (
    <>
      <div className="col">
        <div className="card">
          <img src={image} className="card-img-top" alt="" />
          <div className="card-body">
            <h5 className="card-title">{title}</h5>
            <p className="card-text">
              {desc}
            </p>
            <button className="button" onClick={() => {navigate("/main")}}>View Recipe</button>
          </div>
        </div>
      </div>
    </>
  )
}

export default Card
