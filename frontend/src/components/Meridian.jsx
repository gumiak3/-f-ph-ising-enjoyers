import * as THREE from "three";

const LLRADIUS = 2.05;

export default function Meridian() {
    const points = [];
  
    const radius = LLRADIUS;
    const numPoints = 100;
    const angleStep = (Math.PI * 2) / numPoints;
  
    for (let i = 0; i < numPoints; i++) {
      const angle = i * angleStep;
      const x = radius * Math.cos(angle);
      const z = 0;
      const y = radius * Math.sin(angle);
      points.push(new THREE.Vector3(x, y, z));
    }
    points.push(new THREE.Vector3(LLRADIUS, 0, 0));
  
    const geometry = new THREE.BufferGeometry().setFromPoints(points);
    const material = new THREE.LineBasicMaterial({
      color: 0xff0000,
      linewidth: 2,
    });
  
    return <line geometry={geometry} material={material} />;
  }