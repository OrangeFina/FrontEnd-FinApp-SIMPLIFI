import React, { Component } from "react";
import "./mycss.css";
import axios from "axios";
import querystring from 'querystring';

class Counter extends Component {
  state = {
    count: 0
  };

  imdone = () => {
    this.handleSubmit();
    // window.location.href = "/allocation";
  };

  handleSubmit = () => {
    // event.preventDefault();
    const game = {
      'count': this.state.count
    };

    const submission = querystring.stringify(game); 

    axios
      .get("http://127.0.0.1:8000/questionnaire?"+ submission,{game})
      .then(res => {
        console.log(res);
        console.log(res.data);
        window.location = "/allocation";
      });
      window.location.href = '/allocation';
  };

  handleIncrement = () => {
    this.setState({ count: this.state.count + 1 });
    console.log(this.state.count + 1);
    if (this.state.count + 1 === 500) {
      alert("YOU ARE TOO RISKY BRO");
      window.location.href = "/dashboard";
    }
  };
  // ALSO PREP FOR CONSOLE.SAVE to make sure we can get the input for TrueRisk

  render() {
    return (
      <div className="buttons">
        <h1 class="footer"> Rules of the Game </h1>
        <h5 class="footer">
          You will click and earn as many point as possible. However, there is a
          secret limit that will return you to zero points. Once you think you
          have enough points, hit button{" "}
          <b>"That is enough for me." at the bottom</b> to save your points! You
          have one try, all the best!
        </h5>
        <span className={this.getBadgeClasses()}>{this.formatCount()}</span>
        <br />
        <button
          type="buttons"
          onClick={this.handleIncrement}
          className="btn btn-secondary btn-lg"
        >
          Click ME to earn points!
        </button>
        
        <button
            onSubmit={this.handleSubmit}
            type="buttons"
            onClick={this.imdone}
            className="btn btn-dark btn-lg"
            action="/allocation"
          >
            That is enough for me.
          </button>

      </div>
    );
  }

  getBadgeClasses() {
    let classes = "badge m-3 badge-";
    classes += this.state.count === 0 ? "warning" : "primary";
    return classes;
  }

  formatCount() {
    const { count } = this.state;
    return count === 0 ? <span>Zero</span> : count;
  }
}
export default Counter;
