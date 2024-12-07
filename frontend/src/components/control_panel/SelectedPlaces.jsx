export default function SelectedPlaces({ coordinates }) {
  const handleDelete = () => {};

  return (
    <section className="selected-places-panel">
      <h2>Selected Places:</h2>
      <ul>
        {coordinates.map((coords, index) => (
          <li key={index}>
            <button onClick={handleDelete}>X</button>
            {coords.latitude},{coords.longitude}
          </li>
        ))}
      </ul>
    </section>
  );
}
