import React from "react";
import { Canvas } from "@react-three/fiber";
import { OrbitControls, Sphere, Stars } from "@react-three/drei";
import * as THREE from "three";
import "./App.css";

function Earth() {
  return (
    <Sphere args={[1, 64, 64]}>
      <meshStandardMaterial
        attach="material"
        map={new THREE.TextureLoader().load("earth.jpg")}
        emissive={new THREE.Color(0xffffff)}        /* Glow effect */
        emissiveIntensity={0.1}                    /* Control glow intensity */
        roughness={0.1}                            /* Shiny surface */
        metalness={0.1}                            /* Slight metallic effect */
      />
    </Sphere>
  );
}

function App() {
  return (
    <div style={{ height: "100vh" }}>
      <Canvas>
        {/* Background with stars */}
        <Stars />
        {/* Earth sphere */}
        <Earth />
        {/* Orbit controls for rotation */}
        <EarthPath /> 
        <OrbitControls />
        {/* Lighting */}
        <ambientLight intensity={1.5} />  {/* More ambient light */}
        <directionalLight position={[5, 5, 5]} intensity={1} />  {/* Sun-like directional light */}
        <pointLight position={[10, 10, 10]} intensity={1} />  {/* Additional point light */}
      </Canvas>
    </div>
  );
}

function EarthPath() {
  const points = [];  // Array to store the points for the line

  const radius = 1.2; // Slightly larger radius than the Earth's sphere radius
  const numPoints = 100; // Number of points to create a smooth line
  const angleStep = (Math.PI * 2) / numPoints; // Angle step for each point

  
  // Generate points in a circle around the Earth (on the x-z plane)
  for (let i = 0; i < numPoints; i++) {
    const angle = i * angleStep;
    const x = radius * Math.cos(angle);  // X coordinate
    const z = radius * Math.sin(angle);  // Z coordinate
    const y = 0;  // Keep y as 0 for a horizontal path (or adjust for vertical if needed)
    points.push(new THREE.Vector3(x, y, z));  // Add the point to the array
    console.log("x=" + x + "y=" + y + "z=" + z + " ");
  }
  points.push(new THREE.Vector3(1.2, 0, 0));

  const geometry = new THREE.BufferGeometry().setFromPoints(points); // Create geometry from points
  const material = new THREE.LineBasicMaterial({ color: 0xff0000, linewidth: 2 }); // Line material

  return <line geometry={geometry} material={material} />;
}

export default App;
