import { Route, Switch, useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
import DateList from "./DateList";
import CreateDate from "./CreateDate";
import Login from "./Login";
import Navbar from "./Navbar";
import Home from "./Home";
import Signup from "./Signup";

function App() {
  const [dates, setDate] = useState([]);
  const [user, setUser] = useState(null);
  const location = useLocation();
  const data = location.state;
  console.log(data);

  // const [selectedDate, setSelectedDate] = useState(null);

  useEffect(() => {
    fetch("/check_session").then((response) => {
      if (response.ok) {
        response.json().then((user) => setUser(user));
      }
    });
  }, []);

  useEffect(() => {
    fetch("/dates")
      .then((r) => r.json())
      .then((dates) => setDate(dates));
  }, []);

  function handleLogin(user) {
    setUser(user);
  }

  function handleLogout() {
    setUser(null);
  }

  // function handleSelectedDate(date) {
  //   setSelectedDate(date);
  // }

  const handleAddDate = (date) => {
    setDate([date, ...dates]);
  };
  return (
    <>
      <Navbar user={user} onLogout={handleLogout} />
      <Switch>
        <Route exact path="/">
          <Home />
        </Route>
        <Route exact path="/signup">
          <Signup />
        </Route>
        {/* <Route exact path="/dates/:id">
          {/* <DateDetails date={date} /> </Route>*/}

        <Route exact path="/dates">
          <DateList
            user={user}
            dates={dates}
            // onDateClick={handleSelectedDate}
          />
        </Route>
        <Route exact path="/dates/new">
          <CreateDate handleAddDate={handleAddDate} />
        </Route>
        <Route exact path="/login">
          <Login user={user} onLogin={handleLogin} />
        </Route>
      </Switch>
    </>
  );
}

export default App;

// import { useEffect, useState } from "react";
// import Tile from "./Tile";
// import CreateDate from "./CreateDate";

// function App() {
//   const [dates, setDate] = useState([]);

//   useEffect(() => {
//     fetch("/dates")
//       .then((r) => r.json())
//       .then((dates) => setDate(dates));
//   }, []);

//   const handleAddDate = (date) => {
//     setDate([date, ...dates]);
//   };

//   return (
//     <>
//       <CreateDate handleAddDate={handleAddDate} />
//       <Tile dates={dates} />
//     </>
//   );
//   // return <h1>Check the console for a list of dates!</h1>;
// }

// export default App;
