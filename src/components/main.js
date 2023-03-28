import React from "react";
import logo from "../images/logo.png";

const Main = () => {
  return (
    <>
      <div className="container">
        <img
          src={logo}
          alt=""
          width="200px"
          height="auto"
          style={{ position: "relative", left: "40%" }}
        />
        <h2>Recipe Name</h2>
        <br/>
        <p>
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Nemo nam
          nulla excepturi sequi cum non veritatis, atque nobis, earum blanditiis
          quod odio voluptate dicta incidunt qui magnam tempore ex temporibus.
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolore
          aliquam minus officiis harum labore quod cumque sed, laborum, esse,
          animi repudiandae tempora cupiditate provident culpa alias quisquam
          asperiores magni aspernatur.<br/><br/>
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Nemo nam
          nulla excepturi sequi cum non veritatis, atque nobis, earum blanditiis
          quod odio voluptate dicta incidunt qui magnam tempore ex temporibus.
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolore
          aliquam minus officiis harum labore quod cumque sed, laborum, esse,
          animi repudiandae tempora cupiditate provident culpa alias quisquam
          asperiores magni aspernatur.
        </p>
      </div>
    </>
  );
};

export default Main;
