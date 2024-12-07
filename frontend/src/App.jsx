import React from "react";
import { Canvas } from "@react-three/fiber";
import { OrbitControls, Sphere, Stars } from "@react-three/drei";
import EarthPath from "./components/Equator";
import EarthPath2 from "./components/Meridian";
import RouteTracker from "./components/RouteTracker";
import EarthMarker from "./components/EarthMarker";
import Earth from "./components/Earth";
import "./App.css";
import SidePanel from "./components/control_panel/SidePanel";

function App() {
  return (
    <div className="page" style={{ height: "100vh" }}>
      <SidePanel />
      <Canvas>
        <Stars />
        <Earth />
        <EarthPath />
        <EarthPath2 />
        <RouteTracker />
        <EarthMarker latitude={25.9875} longitude={-97.1864} />
        <OrbitControls />
        <ambientLight intensity={1.5} />
        <directionalLight position={[5, 5, 5]} intensity={1} />
        <pointLight position={[10, 10, 10]} intensity={1} />
      </Canvas>
    </div>
  );
}

export default App;
