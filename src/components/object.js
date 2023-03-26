import React from 'react';
import { useState } from 'react';
import camera from "../images/camera.png";

const Object = () => {

  const [imageUrl, setImageUrl] = useState(null);

  const handleImageClick = () => {
    navigator.mediaDevices.getUserMedia({ video: true })
      .then((stream) => {
        const video = document.createElement('video');
        video.srcObject = stream;
        video.play();
        const canvas = document.createElement('canvas');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
        setImageUrl(canvas.toDataURL('image/png'));
        stream.getTracks().forEach((track) => track.stop());
      })
      .catch((error) => console.error('Error accessing webcam:', error));
  };

  return (
    <>
      <div className="object">
        <h2>Ingredient Identification</h2>
            <img src = {camera} alt="" width="400px" onClick={handleImageClick} />
            {imageUrl && <img src={imageUrl} alt="Captured Image" />}
      </div>
    </>
  )
}

export default Object




