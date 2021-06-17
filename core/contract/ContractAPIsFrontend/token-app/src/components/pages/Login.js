import React, { useState } from "react";
import axios from "axios";

const Login = () => {
  // define hook
  const [username, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [token, setToken] = useState("");
  const [error, setError] = useState("");
  const submitHandler = (e) => {
    e.preventDefault();
    setToken("");
    if (username && password) {
      axios
        .get("http://138.232.18.138:5002/api/token/", {
          headers: {
            username: username,
            password: password,
          },
        })
        .then((response) => {
          console.log(response);
          if (response.data.token) {
            setToken(response.data.token);
          } else {
            setError(response.data);
          }
        });
      return true;
    } else {
      alert("Username or password is missing");
      return false;
    }
  };

  return (
    <div>
      <form onSubmit={submitHandler}>
        <div className="form-group row m-1">
          <div className="col-sm-2">
            <label style={{ fontStyle: "italic", fontWeight: "bold" }}>
              User Name :
            </label>
          </div>
          <div className="col-sm-8">
            <input
              type="text"
              name="username"
              value={username}
              className="form-control form-control-sm"
              onChange={(e) => setUserName(e.target.value)}
            />
          </div>
        </div>
        <div className="form-group row m-1">
          <div className="col-sm-2">
            <label style={{ fontStyle: "italic", fontWeight: "bold" }}>
              Password :
            </label>
          </div>
          <div className="col-sm-8">
            <input
              type="password"
              name="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="form-control form-control-sm"
            />
          </div>
        </div>
        <div className="form-group row m-1">
          <div className="col-sm-2">
            <label></label>
          </div>
          <div className="col-sm-8">
            <button className="btn btn-success btn-sm" type="submit">
              generate token
            </button>
          </div>
        </div>
        {token ? (
          <div className="form-group row">
            <div className="col-sm-2">
              <label>Token</label>
            </div>
            <div className="col-sm-10">
              <textarea
                className="form-control form-control-sm"
                value={token}
                onChange={(e) => setToken(e.target.value)}
                disabled
              ></textarea>
            </div>
          </div>
        ) : error ? (
          <div className="form-group row">
            <div className="col-sm-2">
              <label>Error</label>
            </div>
            <div className="col-sm-10">
              <textarea
                className="form-control form-control-sm"
                value={error}
                onChange={(e) => setError(e.target.value)}
                disabled
              ></textarea>
            </div>
          </div>
        ) : (
          ""
        )}
      </form>
    </div>
  );
};

export default Login;
