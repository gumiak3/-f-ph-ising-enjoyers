import SelectedPlaces from "./SelectedPlaces";
import PlaceSelectionPanel from "./PlaceSelectionPanel";

export default function ControlPanel({ sendCoordinates, coordinates }) {
  return (
    <section>
      <PlaceSelectionPanel sendCoordinates={sendCoordinates} />
      <SelectedPlaces coordinates={coordinates} />
    </section>
  );
}
