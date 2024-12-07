import { Sphere } from "@react-three/drei";
import * as THREE from "three";

export default function Earth() {
  return (
    <Sphere args={[2, 256, 256]} position={[0, 0, 0]}>
      <meshStandardMaterial
        attach="material"
        map={new THREE.TextureLoader().load("earth.jpg")}
      />
    </Sphere>
  );
}
