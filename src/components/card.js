import React from 'react';
import logo from "../images/logo.png";

const Card = (props) => {
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
          </div>
        </div>
      </div>
    </>
  )
}

export default Card
