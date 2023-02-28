import { Link } from "react-router-dom";

function Navbar({ user, onLogout }) {
  function handleLogout() {
    fetch("/logout", {
      method: "DELETE",
    }).then(() => onLogout());
  }

  return (
    <header>
      <h1>
        <Link to="/">Home</Link>
      </h1>
      {user ? (
        <div>
          <p>Welcome, {user.username}!</p>
          <br />
          <Link to="/dates">Dates</Link>
          <br />
          <Link to="/dates/new">Add Date</Link>
          <br />
          <br />
          <button onClick={handleLogout}>Logout</button>
        </div>
      ) : (
        <>
          <Link to="/login">Login</Link>
          <br />
          <Link to="/signup">Signup!</Link>
        </>
      )}
    </header>
  );
}

export default Navbar;
