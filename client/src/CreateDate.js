import React, { useState } from "react";

function CreateDate({ handleAddDate }) {
  const [value, setValue] = useState({
    name: "",
    gender: "",
    see_again: false,
    date_of_date: "",
    image_uri: "",
  });

  function handleSubmit(event) {
    event.preventDefault();

    console.log("This is the value: ", value);

    fetch("/dates", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: value.name,
        gender: value.gender,
        see_again: value.see_again,
        date_of_date: value.date_of_date,
        image_uri: value.image_uri,
      }),
    });
    //   .then((r) => r.json())
    //   .then((newReview) => onAddReview(newReview));

    // console.log("date created: ", value);
    //handleAddDate(value);
  }

  function handleChange(event) {
    setValue({ ...value, [event.target.name]: event.target.value });
  }
  // name: "",
  // gender: "",
  // see_again: false,
  // date_of_date: "",
  // image_uri: "",
  return (
    <form class="ui form" onSubmit={handleSubmit}>
      <label>Name:</label>
      {/* <input type="text" value={value} onChange={(e) => handleChange(e)} /> */}
      <input name="name" value={value.name} onChange={handleChange} />
      <br />
      <br />
      <label>Gender:</label>
      <input name="gender" value={value.gender} onChange={handleChange} />

      <br />
      <br />
      <label>Date of Date:</label>
      <input
        name="date_of_date"
        value={value.date_of_date}
        onChange={handleChange}
      />
      <br />
      <br />
      <label>Image:</label>
      <input name="image_uri" value={value.image_uri} onChange={handleChange} />
      <br />
      <br />
      <label>See again:</label>
      <input
        name="see_again"
        type="radio"
        value={value.see_again}
        onChange={handleChange}
      />
      <br />
      <br />
      <input type="submit" value="Submit" />
    </form>
  );
}
export default CreateDate;
