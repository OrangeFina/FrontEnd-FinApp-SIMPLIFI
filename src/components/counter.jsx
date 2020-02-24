import React, { Component } from "react";
import "./mycss.css";

class Counter extends Component {
  state = {
    count: 0
  };

  imdone = () => {
    window.location.href = "/dashboard";
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
      <div class="buttons">
        <span className={this.getBadgeClasses()}>{this.formatCount()}</span>
        <br />
        <button
          type="buttons"
          onClick={this.handleIncrement}
          className="btn btn-secondary btn-lg btn-block"
        >
          Click me before I disappear!
        </button>
        <button
          type="buttons"
          onClick={this.imdone}
          className="btn btn-dark btn-sm"
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
