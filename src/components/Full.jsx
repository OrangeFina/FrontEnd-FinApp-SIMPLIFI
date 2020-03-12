import React, { Component } from "react";
import axios from "axios";
import data from "./stockdata";
import FullStock from "./Fullstock";

var i = 49;
var ii = 68;
var iii = 382;

class Full extends Component {
  state = {
    inputs: []
  };

  Fimdone = () => {
    window.location.href = "/Fullstock";
  };

  render() {
    return (
      <div className="full">
        <div className="sticker">
          <h1>Ticker: {data.Ticker[i]}</h1>{" "}
          <h2>Company Name: {data.CompanyName[i]}</h2>
          <h6>Brief Description: {data.Profile[i]}</h6>
          <button onClick={this.Fimdone}>
            {" "}
            Click to learn more about {data.Ticker[i]}
          </button>
        </div>
        <div className="sticker">
          <h1>Ticker: {data.Ticker[ii]}</h1>
          <h2>Company Name: {data.CompanyName[ii]}</h2>
          <h6>Brief Description: {data.Profile[ii]}</h6>
          <button onClick={this.Fimdone}>
            {" "}
            Click to learn more about {data.Ticker[iii]}
          </button>
        </div>
        <div className="sticker">
          <h1>Ticker: {data.Ticker[iii]}</h1>
          <h2>Company Name: {data.CompanyName[iii]}</h2>
          <h6>Brief Description: {data.Profile[iii]}</h6>
          <button onClick={this.Fimdone}>
            {" "}
            Click to learn more about {data.Ticker[iii]}
          </button>
        </div>
      </div>
    );
  }
}

export default Full;
