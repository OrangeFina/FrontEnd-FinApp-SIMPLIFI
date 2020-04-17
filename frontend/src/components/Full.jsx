import React, { Component } from "react";
import axios from "axios";
import data from "./stockdata";
import stockresult from "./stockresult.json"



// dependent on the selection (need react from django)


class Full extends Component {
  state = {
    inputs: []
  };


  Fimdone1 = () => {
    window.location.href = "/Fullstock";
  };
  Fimdone2 = () => {
    window.location.href = "/Fullstock1";
  };
  Fimdone3 = () => {
    window.location.href = "/Fullstock2";
  };

  render() {
    console.log(stockresult)
    return (
      <div className="full">
        <div className="sticker">
          <h1>Ticker: {stockresult.company_name_ticker[0]}</h1>{" "}
          <h2>Company Name: {stockresult.company_name_ticker[0]}</h2>
          <h6>Brief Description: {stockresult.profile[0]}</h6>
          <button onClick={this.Fimdone1}>
            {" "}
            Click to learn more about {stockresult.company_name_ticker[0]}
          </button>
        </div>
        <div className="sticker">
          <h1>Ticker: {stockresult.company_name_ticker[1]}</h1>
          <h2>Company Name: {stockresult.company_name_ticker[1]}</h2>
          <h6>Brief Description: {stockresult.profile[1]}</h6>
          <button onClick={this.Fimdone2}>
            {" "}
            Click to learn more about {stockresult.company_name_ticker[1]}
          </button>
        </div>
        <div className="sticker">
          <h1>Ticker: {stockresult.company_name_ticker[2]}</h1>
          <h2>Company Name: {stockresult.company_name_ticker[2]}</h2>
          <h6>Brief Description: {stockresult.profile[2]}</h6>
          <button onClick={this.Fimdone3}>
            {" "}
            Click to learn more about {stockresult.company_name_ticker[2]}
          </button>
        </div>
      </div>
    );
  }
}

export default Full;
