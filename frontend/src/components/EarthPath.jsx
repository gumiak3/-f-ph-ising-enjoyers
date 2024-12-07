import * as THREE from "three";

export default function EarthPath() {
  const points = [];

  const radius = 2.2;
  const numPoints = 100;
  const angleStep = (Math.PI * 2) / numPoints;

  for (let i = 0; i < numPoints; i++) {
    const angle = i * angleStep;
    const x = radius * Math.cos(angle);
    const z = radius * Math.sin(angle);
    const y = 0;
    points.push(new THREE.Vector3(x, y, z));
  }
  points.push(new THREE.Vector3(2.2, 0, 0));

  const geometry = new THREE.BufferGeometry().setFromPoints(points);
  const material = new THREE.LineBasicMaterial({
    color: 0xff0000,
    linewidth: 2,
  });

  return <line geometry={geometry} material={material} />;
}
