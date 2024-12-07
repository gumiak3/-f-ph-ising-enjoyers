import { useRef, useState, useEffect } from "react";

export default function PlaceSelection({ isExpanded, sendCoordinates }) {
  const latitudeRef = useRef(null);
  const longitutdeRef = useRef(null);

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!latitudeRef && !longitutdeRef) return;

    if (
      latitudeRef.current.value.trim() === "" ||
      longitutdeRef.current.value.trim() === ""
    )
      return;

    const parsedLatitutde = parseFloat(latitudeRef.current.value);
    const parsedLongitutde = parseFloat(longitutdeRef.current.value);

    sendCoordinates({
      latitude: parsedLatitutde,
      longitude: parsedLongitutde,
    });
  };

  return (
    <div className={`place-selection ${isExpanded ? "expanded" : "collapsed"}`}>
      <form onSubmit={handleSubmit}>
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
        <button className="">Add</button>
      </form>
    </div>
  );
}
