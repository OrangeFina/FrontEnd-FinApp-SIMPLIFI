import React from "react";
import axios from "axios";

import querystring from 'querystring';

class Sinputs extends React.Component {
  state = {
    inputs: []
  };

  Simdone = () => {
    this.handleSubmit();
  };

  handleChange = event => {
    //appends new value into array
    const value = event.target.value;
    this.state.inputs.push(value);
  };
  

  handleSubmit = () => {
    const question = {
      'question': this.state.inputs
    };

    // formats the inputs for django
    const submission = querystring.stringify(question); 
    axios
      .get("http://127.0.0.1:8000/stock-query?" + submission,{question})
      .then(res => {
        console.log(res);
        console.log(res.data);
        // window.location = "/newsoutputs2";
        
      });
  };

  render() {
    return (
      <form className="screener" action="/newsoutput2">
        <div>
          <label>
            <b>Stock Ticker</b>
          </label>
          <br />
          <input
            name="ticker"
            type="text"
            placeholder="e.g. AAPL"
            onBlur={this.handleChange}
          />
        </div>
        <br />
        <br />
        <br />
        <div>
          <label>
            <b>Start Date</b>
          </label>
          <br />
          <input
            type="text"
            placeholder="DD/MM/YY"
            name="sDate"
            onBlur={this.handleChange}
          />
          <br />
          <label>
            <b>End Date</b>
          </label>
          <br />
          <input
            type="text"
            placeholder="DD/MM/YY"
            name="sDate"
            onBlur={this.handleChange}
          />
          <button type="submit" onClick={this.Simdone}>
            Analyse
          </button>
        </div>
        <div>
          {/* <label>
            <b>Price/Volume</b>
          </label>
          <br />
          <input
            id="PV"
            type="text"
            placeholder="Price or Volume"
            name="PV"
            required
          />
          <br /> */}
          <label>
            <b>Factor change</b>
          </label>
          <br />
          <input
            type="text"
            placeholder="Pos or Neg"
            name="change"
            onBlur={this.handleChange}
          />
          <label>
            <b>Factor Value</b>
          </label>
          <br />
          <input
            type="text"
            placeholder="1,2,3"
            name="change"
            // onBlur={this.handleChange}
          />
        </div>
      </form>
    );
  }
}
export default Sinputs;
