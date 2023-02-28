import { useState } from "react";
import Tile from "./Tile";
import EditDate from "./EditDate";

function DateList({ user }) {
  const [dateOfDate, setDateOfDate] = useState(null);
  const [gender, setGender] = useState(null);
  const [id, setId] = useState(null);
  const [imageUri, setImageUri] = useState(null);
  const [locations, setLocations] = useState(null);
  const [name, setName] = useState(null);
  const [notes, setNotes] = useState(null);
  const [seeAgain, setSeeAgain] = useState(null);
  const [userId, setUserId] = useState(null);

  function handleClickToEdit(d) {
    console.log("clicked by handleClickToEdit", d);
    const {
      date_of_date,
      gender,
      id,
      image_uri,
      locations,
      name,
      notes,
      see_again,
      user_id,
    } = d;
    setDateOfDate(date_of_date);
    setGender(gender);
    setId(id);
    setImageUri(image_uri);
    setLocations(locations);
    setName(name);
    setNotes(notes);
    setSeeAgain(see_again);
    setUserId(user_id);
  }

  console.log(dateOfDate);
  console.log(gender);
  console.log(id);
  console.log(imageUri);
  console.log(locations);
  console.log(name);
  console.log(notes);
  console.log(seeAgain);
  console.log(userId);

  function handleClickToDelete(d) {
    console.log("clicked by handleClickToDelete", d);
    fetch(`/dates/${d.id}`, {
      method: "DELETE", // or 'PUT'
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(d),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }
  //console.log("this is the user: ", user.dates);
  return (
    <>
      {user &&
      !dateOfDate &&
      !gender &&
      !id &&
      !imageUri &&
      !locations &&
      !name &&
      !notes &&
      !seeAgain &&
      !userId ? (
        <Tile
          key={user.id}
          dates={user.dates}
          handleClickToEdit={handleClickToEdit}
          handleClickToDelete={handleClickToDelete}
        />
      ) : (
        <EditDate
          dateOfDate={dateOfDate}
          gender={gender}
          id={id}
          imageUri={imageUri}
          locations={locations}
          name={name}
          notes={notes}
          seeAgain={seeAgain}
          userId={userId}
        />
      )}
    </>
  );
}

export default DateList;
