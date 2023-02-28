import React, { useState, selectedDate } from "react";

function EditDate(props) {
  const [name, setName] = useState(props.name);
  const [age, setAge] = useState(props.age);

  console.log(selectedDate);

  function handleSubmit(event) {
    event.preventDefault();
    const formData = { name, age };
    props.onSubmit(formData);
  }

  return (
    // <>
    //   <div>hiiiiiiii</div>
    // </>
    <form onSubmit={handleSubmit}>
      <h2>Edit Form</h2>
      <label>
        Name:
        <input
          type="text"
          value={"bob"}
          //   value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </label>
      <label>
        Age:
        <input
          type="number"
          value={age}
          onChange={(e) => setAge(e.target.value)}
        />
      </label>
      <button type="submit">Save</button>
    </form>
  );
}

export default EditDate;
