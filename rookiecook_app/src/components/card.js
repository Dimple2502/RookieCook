import React from 'react';
import { useParams,useNavigate } from "react-router-dom";

const Card = (props) => {
  const navigate = useNavigate();
  const {id, image, title, ingredients, desc } = props;

  return (
    <>
      <div className="col">
        <div className="card">
          <img src={image} className="card-img-top" alt="" />
          <div className="card-body">
            <h5 className="card-title">{[title.slice(0,20),(title.length>=10)?"....":""]}</h5>
            <p className="card-text">
              {[desc.slice(0,80),(desc.length>=80)?"......":""]}
            </p>
            <button className="button" onClick={() => navigate(`/main/${id}`)}>View Recipe</button>

          </div>
        </div>
      </div>
    </>
  )
}

export default Card
