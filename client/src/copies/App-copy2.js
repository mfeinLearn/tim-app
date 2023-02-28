import { Route, Switch } from "react-router-dom";
import { useEffect, useState } from "react";
import DateList from "./DateList";
import CreateDate from "./CreateDate";
import Login from "./Login";
import Navbar from "./Navbar";
import Home from "./Home";

function App() {
  const [dates, setDate] = useState([]);
  const [user, setUser] = useState(null);

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
        <Route exact path="/login">
          <Login onLogin={handleLogin} />
        </Route>
        <Route exact path="/dates">
          <DateList dates={dates} />
        </Route>
        <Route exact path="/dates/new">
          <CreateDate handleAddDate={handleAddDate} />
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
