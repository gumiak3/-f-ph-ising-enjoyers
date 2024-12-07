import React from "react";
import { Canvas } from "@react-three/fiber";
import { OrbitControls, Sphere, Stars } from "@react-three/drei";
import EarthPath from "./components/EarthPath";
import Earth from "./components/Earth";
import "./App.css";

function App() {
  return (
    <div className="page" style={{ height: "100vh" }}>
      <Canvas>
        <Stars />
        <Earth />
        <EarthPath />
        <OrbitControls />
        <ambientLight intensity={1.5} />
        <directionalLight position={[5, 5, 5]} intensity={1} />
        <pointLight position={[10, 10, 10]} intensity={1} />
      </Canvas>
    </div>
  );
}

export default App;
