import * as THREE from "three";

export default function EarthMarker({ latitude, longitude }) {
    const radius = 2;
  
    const position = latLonToXYZ(latitude, longitude, radius);
  
    return (
      <mesh position={position}>
        <sphereGeometry args={[0.005, 16, 16]} />
        <meshBasicMaterial color="blue" />
      </mesh>
    );
  }
  
  function latLonToXYZ(latitude, longitude, radius) {
    const latRad = THREE.MathUtils.degToRad(latitude); 
    const lonRad = - THREE.MathUtils.degToRad(longitude); // - Because of way how it`s mapped on sphere
  
    
    const x = radius * Math.cos(latRad) * Math.cos(lonRad); 
    const y = radius * Math.sin(latRad);                    
    const z = radius * Math.cos(latRad) * Math.sin(lonRad); 
  
    return new THREE.Vector3(x, y, z);
  }