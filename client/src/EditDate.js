////
// import React, { useState, selectedDate } from "react";

import { useState } from "react";

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
  const [formData, setFormData] = useState({
    name: name,
    gender: gender,
    date_of_date: dateOfDate,
    image_uri: imageUri,
    see_again: seeAgain,
    id: id,
    user_id: userId,
  });
  console.log(formData);
  const handleInputChange = (event) => {
    event.preventDefault();
    const { name, value } = event.target;
    console.log(name, value);
    setFormData((prevFormData) => ({
      ...prevFormData,
      [name]: value,
    }));
  };

  function handleSubmit(event) {
    event.preventDefault();
    console.log("This is the form data: ", formData);
    const requestOptions = {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData),
    };
    fetch(`/dates/${id}`, requestOptions)
      .then((response) => response.json())
      .then((data) => console.log(data))
      .catch((error) => console.error(error));
  }

  return (
    <form onSubmit={(e) => handleSubmit(e)}>
      <h2>Edit Form</h2>

      {/*  */}
      <label>Name:</label>
      {/* <input type="text" value={value} onChange={(e) => handleChange(e)} /> */}
      <input
        type="text"
        name="name"
        value={formData.name}
        onChange={(e) => handleInputChange(e)}
      />
      <br />
      <br />
      <label>Gender:</label>

      <input
        type="text"
        name="gender"
        value={formData.gender}
        onChange={(e) => handleInputChange(e)}
      />

      <br />
      <br />
      <label>Date of Date:</label>
      <input
        type="text"
        name="date_of_date"
        value={formData.date_of_date}
        onChange={(e) => handleInputChange(e)}
      />
      <br />
      <br />
      <label>Image:</label>
      <input
        type="text"
        name="image_uri"
        value={formData.image_uri}
        onChange={(e) => handleInputChange(e)}
      />
      <br />
      <br />
      <label>See again:</label>
      <input
        name="see_again"
        type="radio"
        value={formData.see_again}
        onChange={(e) => handleInputChange(e)}
      />
      <br />
      <br />
      {/*  */}
      <button type="submit">Submit</button>
    </form>
  );
}

export default EditDate;
