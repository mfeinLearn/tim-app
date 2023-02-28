import React, { useState } from "react";

import { Link } from "react-router-dom";
import DateDetails from "./DateDetails";
// DateDetails

function Tile({ dates, onDateClick, handleClickToEdit, handleClickToDelete }) {
  const [toggler, setToggler] = useState(false);
  // const [clicked, setClicked] = useState(null);

  //   let toggler = true;

  function handleClick(e) {
    e.preventDefault();
    setToggler(() => !toggler);
    // onDateClick(date);
  }

  const dateArray = dates.map((date) => {
    return (
      <div
        class="ui centered card"
        key={date.name}
        onClick={(e) => handleClick(e)}
      >
        <img
          src={date.image_uri}
          alt={date.name + " the date"}
          width="290"
          height="290"
        ></img>
        <div class="content">
          <div class="header">
            {date.name + " Day of date: " + date.date_of_date}
          </div>
        </div>

        <br />
        {/* <div>{toggler ? details(date) : null}</div> */}
        <div>
          {toggler ? (
            <>
              <DateDetails
                key={date.id}
                date={date}
                handleClickToEdit={handleClickToEdit}
                handleClickToDelete={handleClickToDelete}
              />
              {/* <Link to={`/dates/${date.id}`}>More information</Link> */}
              <br />
            </>
          ) : null}
        </div>
      </div>
    );
  });

  return dateArray;
}

export default Tile;
