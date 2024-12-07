import { useState } from "react";
import PlaceSelection from "./PlaceSelection";

export default function SidePanel() {
  const [isExpanded, setIsExpanded] = useState(false);

  const handleClick = () => {
    setIsExpanded((prev) => !prev);
  };

  const handleCoordinates = (cooridantes) => {};

  return (
    <section className="side-panel">
      <button onClick={handleClick}>Select places to see</button>

      <PlaceSelection
        isExpanded={isExpanded}
        sendCooridantes={handleCoordinates}
      />
    </section>
  );
}
