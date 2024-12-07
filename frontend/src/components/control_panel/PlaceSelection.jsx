import { useRef, useState, useEffect } from "react";

export default function PlaceSelection({ isExpanded }) {
  const places = ["Poland", "United States", "Japan"];
  const latitudeRef = useRef(null);
  const longitutdeRef = useRef(null);
  const [coordinates, setCoordinates] = useState([]);

  const handleClick = () => {
    if (!latitudeRef && !longitutdeRef) return;

    setCoordinates((prev) => {
      return [
        ...prev,
        {
          latitude: latitudeRef.current.value,
          longitude: longitutdeRef.current.value,
        },
      ];
    });
  };

  return (
    <div className={`place-selection ${isExpanded ? "expanded" : "collapsed"}`}>
      <label for="latitude-input">Latitude</label>
      <input
        ref={latitudeRef}
        name="latitude-input"
        id="latitude-input"
        type="text"
      />
      <label for="longitude-input">Longitude</label>
      <input
        ref={longitutdeRef}
        name="longitude-input"
        id="longitude-input"
        type="text"
      />
      <button className="" onClick={handleClick}>
        Add
      </button>
    </div>
  );
}
