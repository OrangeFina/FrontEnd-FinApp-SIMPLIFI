import React from "react";
import axios from "axios";

class Allocation extends React.Component {
  constructor() {
    super();

    this.onClickForward = this.onClickForward.bind(this);
    this.onClickBack = this.onClickBack.bind(this);

    const imgAgg_info = require("./Aggressive_info.jpg");
    const imgAgg = require("./Aggressive.jpg");
    const imgCon_info = require("./Conservative_info.jpg");
    const imgCon = require("./Conservative.jpg");
    const imgGrow_info = require("./Growth Balance_info.jpg");
    const imgGrow = require("./Growth Balance.jpg");
    const imgMod_info = require("./Moderate Balance_info.jpg");
    const imgMod = require("./Moderate Balance.jpg");

    this.state = {
      index: 0,
      imgList: [
        imgAgg_info,
        imgAgg,
        imgCon_info,
        imgCon,
        imgGrow_info,
        imgGrow,
        imgMod_info,
        imgMod
      ]
    };
  }
  onClickForward() {
    if (this.state.index + 1 === this.state.imgList.length) {
      this.setState({
        index: 0
      });
    } else {
      this.setState({
        index: this.state.index + 1
      });
    }
  }

  onClickBack() {
    if (this.state.index - 1 === this.state.imgList.length) {
      this.setState({
        index: 0
      });
    } else {
      this.setState({
        index: this.state.index - 1
      });
    }
  }

  Aimdone = () => {
    window.location.href = "/full";
  };

  render() {
    return (
      <div>
        <br />
        <button onClick={this.onClickBack}>Back to Previous</button>
        <button onClick={this.onClickForward}>
          To Optimal Portfolio Allocation
        </button>
        <button onClick={this.Aimdone}>To Stock Explorer</button>
        <br />
        <img src={this.state.imgList[this.state.index]} alt="" />
      </div>
    );
  }
}

export default Allocation;
