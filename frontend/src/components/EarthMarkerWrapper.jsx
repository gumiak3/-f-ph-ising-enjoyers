import EarthMarker from "./EarthMarker";

export default function EarthMarkerWrapper({ cooridantes }) {
  if (cooridantes.length === 0) {
    return;
  }
  return (
    <>
      {cooridantes.map((coords, index) => (
        <EarthMarker
          key={index}
          longitude={coords.longitude}
          latitude={coords.latitude}
        />
      ))}
    </>
  );
}
