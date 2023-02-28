////
// import React, { useState, selectedDate } from "react";

import { useEffect } from "react";

function EditDate({
  dateOfDate,
  gender,
  id,
  imageUri,
  locations,
  name,
  notes,
  seeAgain,
  userId,
}) {
  // const [formData, setFormData] = useState(data);

  // const handleInputChange = (event) => {
  //   const { name, value } = event.target;
  //   setFormData((prevFormData) => ({
  //     ...prevFormData,
  //     [name]: value,
  //   }));
  // };

  function handleSubmit(event) {
    event.preventDefault();
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Edit Form</h2>

      {/*  */}
      <label>Name:</label>
      {/* <input type="text" value={value} onChange={(e) => handleChange(e)} /> */}
      <input
        type="text"
        name="name"
        value={name}
        // onChange={handleChange}
      />
      <br />
      <br />
      <label>Gender:</label>
      <input
        type="text"
        name="gender"
        value={gender}
        // onChange={handleChange}
      />

      <br />
      <br />
      <label>Date of Date:</label>
      <input
        type="text"
        name="date_of_date"
        value={dateOfDate}
        // onChange={handleChange}
      />
      <br />
      <br />
      <label>Image:</label>
      <input
        type="text"
        name="image_uri"
        value={imageUri}
        // onChange={handleChange}
      />
      <br />
      <br />
      <label>See again:</label>
      <input
        name="see_again"
        type="radio"
        value={seeAgain}
        // onChange={handleChange}
      />
      <br />
      <br />
      {/*  */}
      <button type="submit">Save</button>
    </form>
  );
}

export default EditDate;
