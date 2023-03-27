import React from 'react';
import { useState,useRef } from 'react';
import camera from "../images/camera.png";

const Object = () => {

  const videoRef = useRef(null);
  const [webcamOn, setWebcamOn] = useState(false);  
  
  const handleImageClick = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ video: true });
      setWebcamOn(true);
      if (videoRef.current) {
        videoRef.current.srcObject = stream;
        videoRef.current.play();
      }
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <>
      <div className="object">
        <h2>Ingredient Identification</h2>
        {!webcamOn && (
            <img src = {camera} alt="" width="400px" onClick={handleImageClick} 
            style={{ display: `${webcamOn ? 'none' : 'block'}` }}/>
            )}
            <video ref={videoRef} className = "webcam" />
      </div>
    </>
  )
}

export default Object




