function DateDetails({ date, handleClickToEdit, handleClickToDelete }) {
  function handleClickE() {
    handleClickToEdit(date);
  }
  function handleClickD() {
    handleClickToDelete(date);
  }
  // return <h2>Hi, this is a date details component!!!!</h2>;
  return (
    <ul>
      {/* <img
        src={date.image_uri}
        alt={date.name + " the date"}
        width="290"
        height="290"
      ></img> */}
      {<li>{"The date of the date: " + date.date_of_date}</li>}
      <li>{"Gender: " + date.gender}</li>
      <li>
        {"See again? "}
        {date.see_again ? "True" : "False"}
      </li>
      <button onClick={handleClickE}>Edit</button>
      <button onClick={handleClickD}>Delete</button>
    </ul>
  );
}

export default DateDetails;
