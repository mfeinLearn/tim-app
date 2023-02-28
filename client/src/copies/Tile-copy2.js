import React, { useState } from "react";

import { Link } from "react-router-dom";
// DateDetails

function Tile({ dates }) {
  const [toggler, setToggler] = useState(false);

  //   let toggler = true;
  const details = (date) => (
    <ul>
      {<li>{"The date of the date: " + date.date_of_date}</li>}
      <li>{"Gender: " + date.gender}</li>
      <li>
        {"See again? "}
        {date.see_again ? "True" : "False"}
      </li>
    </ul>
  );

  function handleClick() {
    // toggler = false;
    setToggler(() => !toggler);
  }

  const dateArray = dates.map((date) => {
    return (
      <div
        class="ui centered card"
        key={date.name}
        onClick={(date) => handleClick(date)}
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
              <Link to={`/dates/${date.id}`}>More information</Link>
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
