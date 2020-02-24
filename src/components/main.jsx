import React from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import Counter from "./counter";
// import { Component } from "react";
import "./mycss.css";
// import "./formtabs.js";

// This site has 3 pages, all of which are rendered
// dynamically in the browser (not server rendered).
//
// Although the page does not ever refresh, notice how
// React Router keeps the URL up to date as you navigate
// through the site. This preserves the browser history,
// making sure things like the back button and bookmarks
// work properly.

export default function BasicExample() {
  return (
    <Router>
      <div>
        <ul id="nav">
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/LOGIN">LOGIN</Link>
          </li>
          <li>
            <Link to="/dashboard">Questionnaire</Link>
          </li>
          <li>
            <Link to="/counter">Counter Game</Link>
          </li>
        </ul>

        {/* <hr /> */}

        {/*
          A <Switch> looks through all its children <Route>
          elements and renders the first one whose path
          matches the current URL. Use a <Switch> any time
          you have multiple routes, but you want only one
          of them to render at a time
        */}
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/LOGIN">
            <Login />
          </Route>
          <Route path="/dashboard">
            <Dashboard />
          </Route>
          <Route path="/counter">
            <Counter />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

// You can think of these components as "pages"
// in your app.

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
        </form>

        <noscript>You need to enable JavaScript to run this app.</noscript>
      </body>
    </div>
  );
}

// HOW TO VALIDATEEEEEEEEEEE, make a function and call it in inputs
// function validateInput(input) {
//   var x = document.getElementById(loginInput);
//   let letters = /[0-9]/;
//   if (input.value.match(letters)) {
//     return true;
//   } else {
//     alert("Please input alphabets");
// search the assgiend string, then
// if input exist , then assign input as the input as ''
// prompt
// document.getElementById("loginInput");
// document.getElementById("loginInput") = inputLogin
//   .contain(input)
//   .replace(input, "");
//     return false;
//   }
// }

function Login() {
  return (
    <div>
      <h2 class="header">Login</h2>
      <form id="login" action="/dashboard">
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

function Dashboard() {
  return (
    <div>
      <h2 class="header">Questionnaire</h2>
      <form id="myForm" action="/counter">
        <label>
          <div class="question">Question 1</div>
          <b>
            {" "}
            Which of the following do you think best describes your investment
            objectives?
            <br />
            <br />
            A. Your primary focus is on capital growth. You are prepared to
            accept a high level of short term volatility and possible capital
            losses in order to generate potentially higher levels of capital
            growth over the long term. You are well placed to recover from
            unforeseen market downturns either because you have time on your
            side or access to capital reserves.
            <br />
            <br />
            B. You require your investments to be a balance between capital
            growth and income generating assets. Calculated risks will be
            acceptable as you are prepared to accept short term levels of
            volatility in order to outperform inflation.
            <br />
            <br />
            C. Generating a regular income stream is a priority over capital
            growth. You are prepared to sacrifice higher returns in favour of
            preservation of capital
          </b>
        </label>
        <br />
        <input type="text" name="questions" placeholder="A , B , C" />
        <br />
        <div class="question">Question 2</div>
        <b>
          {" "}
          What percentage of your risk capital are you comfortable will you be
          investing?
          <br />
          <br />
          ** Risk capital means funds and assets which if lost would not
          materially change your lifestyle or your family's lifestyle.
          <br />
          <br />
          A. Greater than 70%
          <br />
          <br />
          B. 35% to 70%
          <br />
          <br />
          C. Less than 35%
        </b>
        <br />
        <input type="text" name="questions" placeholder="A , B , C" />
        <br />
        <label>
          <div class="question">Question 3</div>
          <b>
            {" "}
            Once investments have been placed, how long would it be before you
            would need to access your capital?
            <br />
            <br />
            A. > 2 Years
            <br />
            <br />
            B. Between 6 Months and 2 Years
            <br />
            <br />
            C. Less than 6 Months
          </b>
        </label>
        <br />
        <input type="text" name="questions" placeholder="A , B , C" />
        <br />
        <b>Feedback?</b>
        <br />
        <textarea
          placeholder="Let us know what you think about your finance health!"
          name="about"
          rows="10"
          cols="70"
        ></textarea>
        <br />
        <button type="submit">Update</button>
      </form>
    </div>
  );
}
// FOR NOW I ONLY DID 3 questions to sample, will put the rest in

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
