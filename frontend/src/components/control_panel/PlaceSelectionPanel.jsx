import { useState } from "react";
import PlaceSelection from "./PlaceSelection";

export default function PlaceSelectionPanel({ sendCoordinates }) {
  const [isExpanded, setIsExpanded] = useState(false);

  const handleClick = () => {
    setIsExpanded((prev) => !prev);
  };

  return (
    <section className="side-panel">
      <button onClick={handleClick}>Select places to see</button>

      <PlaceSelection
        isExpanded={isExpanded}
        sendCoordinates={sendCoordinates}
      />
    </section>
  );
}
