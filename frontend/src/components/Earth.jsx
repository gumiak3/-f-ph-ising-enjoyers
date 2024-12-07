import { Sphere } from "@react-three/drei";
import * as THREE from "three";

export default function Earth() {
  return (
    <Sphere args={[2, 64, 64]}>
      <meshStandardMaterial
        attach="material"
        map={new THREE.TextureLoader().load("earth.jpg")}
      />
    </Sphere>
  );
}
