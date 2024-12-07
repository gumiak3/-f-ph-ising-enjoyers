import React, { useState } from "react";
import { Canvas } from "@react-three/fiber";
import { OrbitControls, Sphere, Stars } from "@react-three/drei";
import Earth from "./components/Earth";
import "./App.css";
import EarthMarkerWrapper from "./components/EarthMarkerWrapper";
import ControlPanel from "./components/control_panel/ControlPanel";

function App() {
  const [cooridantes, setCoordinates] = useState([
    { latitude: 25.9875, longitude: -97.1864 },
  ]);

  const areDuplicated = (prev, coords) => {
    return prev.some(
      (item) =>
        item.longitude === coords.longitude && item.latitude === coords.latitude
    );
  };

  const handleCoordinates = (coordinates) => {
    setCoordinates((prev) => {
      if (areDuplicated(prev, coordinates)) {
        return prev;
      }
      return [...prev, coordinates];
    });
  };

  return (
    <div className="page" style={{ height: "100vh" }}>
      <ControlPanel
        sendCoordinates={handleCoordinates}
        coordinates={cooridantes}
      />
      <Canvas>
        <Stars />
        <Earth />
        <EarthMarkerWrapper cooridantes={cooridantes} />
        {/* <EarthMarker latitude={25.9875} longitude={-97.1864} /> */}
        <OrbitControls />
        <ambientLight intensity={1.5} />
        <directionalLight position={[5, 5, 5]} intensity={1} />
        <pointLight position={[10, 10, 10]} intensity={1} />
      </Canvas>
    </div>
  );
}

export default App;
