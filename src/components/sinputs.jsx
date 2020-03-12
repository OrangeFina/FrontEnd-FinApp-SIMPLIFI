import React from "react";
import axios from "axios";

class Sinputs extends React.Component {
  state = {
    inputs: []
  };

  Simdone = () => {
    window.location.href = "/newsoutput2";
  };

  handleChange = event => {
    this.setState({ inputs: event.target.value });
  };

  handleSubmit = event => {
    event.preventDefault();

    const question = {
      inputs: this.state.inputs
    };

    axios
      .post("https://my-json-server.typicode.com/typicode/demo/db", {
        question
      })
      .then(res => {
        console.log(res);
        console.log(res.data);
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
            id="ticker"
            type="text"
            placeholder="e.g. AAPL"
            name="ticker"
            required
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
            id="sDate"
            type="text"
            placeholder="DD/MM/YY"
            name="sDate"
            required
          />
          <br />
          <label>
            <b>End Date</b>
          </label>
          <br />
          <input
            id="eDate"
            type="text"
            placeholder="DD/MM/YY"
            name="eDate"
            required
          />
          <button type="submit" onClick={this.Simdone}>
            Analyse
          </button>
        </div>
        <div>
          <label>
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
          <br />
          <label>
            <b>Factor change</b>
          </label>
          <br />
          <input
            id="change"
            type="text"
            placeholder="in % or millions (e.g. +3, -3)"
            name="change"
            required
          />
        </div>
      </form>
    );
  }
}
export default Sinputs;
