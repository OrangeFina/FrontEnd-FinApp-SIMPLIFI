import React from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import Counter from "./counter";
// import { Component } from "react";
import "./mycss.css";
import Qinputs from "./qinputs";
import Sinputs from "./sinputs";
import Allocation from "./allocation";
import Full from "./Full";
import FullStock from "./Fullstock";
import FullStock1 from "./Fullstock1";
import FullStock2 from "./Fullstock2";
import Newsoutput2 from "./newsoutput2";
import AaplChart from "./aaplchart";
import Grid from "@material-ui/core/Grid";


export default function BasicExample() {
  return (
    <Router>
      <div>
        <ul id="nav">
          <Grid container spacing={1}>
            <Grid item xs={6}>
              <li>
                <Link to="/">About</Link>
              </li>
              {/* <li>
              <Link to="/LOGIN">Login</Link>
            </li> */}
              <li>
                <Link to="/qinputs">Risk Profile</Link>
              </li>
              {/* <li>
            <Link to="/counter">Counter Game</Link>
          </li> */}
              <li>
                <Link to="/allocation">Asset Allocation</Link>
              </li>
              <li>
                <Link to="/full">Stock Explorer</Link>
              </li>
              <li>
                <Link to="/advanced">Relevant News Engine</Link>
              </li>
            </Grid>
            <Grid item xs={5}></Grid>
            <Grid item xs={1}>
              <li>
                <Link to="/LOGIN">Login</Link>
              </li>
            </Grid>
          </Grid>
        </ul>

        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/LOGIN">
            <Login />
          </Route>
          <Route path="/qinputs">
            <Qinputs />
          </Route>
          <Route path="/counter">
            <Counter />
          </Route>
          <Route path="/allocation">
            <Allocation />
          </Route>
          <Route path="/full">
            <Full />
          </Route>
          <Route path="/fullstock">
            <FullStock />
          </Route>
          <Route path="/fullstock1">
            <FullStock1 />
          </Route>
          <Route path="/fullstock2">
            <FullStock2 />
          </Route>
          <Route path="/advanced">
            <Sinputs />
          </Route>
          <Route path="/newsoutput2">
            <Newsoutput2 />
          </Route>
          <Route path="/aaplchart">
            <AaplChart />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

// Each component is one page

function Home() {
  return (
    <div>
      <h2 class="header">TeamCashCow</h2>
      <body>
        <div id="index"></div>

        <form id="memlogin" action="/LOGIN">
          <div>
            <button type="submit">Member Login</button>
          </div>
          <img className="imgteaser" src={require("./SIMPLIFI.jpeg")} />
        </form>
      </body>
    </div>
  );
}

function Login() {
  return (
    <div>
      <h2 class="header">Login</h2>
      <form id="login" action="/qinputs">
        <label>
          <b>Username</b>
        </label>
        <br />
        <input
          id="loginInput"
          type="text"
          placeholder="Enter your Username"
          name="uname"
          required
        />
        <br />
        <label>
          <b>Password</b>
        </label>
        <br />
        <input
          type="password"
          placeholder="Enter your Password"
          name="psw"
          required
        />
        <br />
        <button type="submit" onClick="request">
          Login
        </button>
        <br />
        <input type="checkbox" name="remember" unchecked="unchecked" />
        Remember Me
      </form>
    </div>
  );
}

// Below for validation logic flow, please ignore
// <script>
// document.getData
// let usnm = document.getData('usnm')
// let pwd = document.getData('pws')

// axios.get('/user', {
//     params: {
//       username: usnm,
//       lalala: pwd
//     }
//   })
//   .then(function (response) {
//     console.log(response);
//   })
//   .catch(function (error) {
//     console.log(error);
//   })
//   .then(function () {
//     // always executed
//   });
// </script>
