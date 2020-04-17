import React from "react";
import axios from "axios";
import maindb from "./maindb"


class Allocation extends React.Component {
  constructor() {
    super();

    this.onClickForward = this.onClickForward.bind(this);
    this.onClickBack = this.onClickBack.bind(this);
    this.onLoadA = this.onLoadA.bind(this);

    // const imgAgg_info = require("./Aggressive_info.jpg");
    // const imgAgg = require("./Aggressive.jpg");
    // const imgCon_info = require("./Conservative_info.jpg");
    // const imgCon = require("./Conservative.jpg");
    // const imgGrow_info = require("./Growth Balance_info.jpg");
    // const imgGrow = require("./Growth Balance.jpg");
    // const imgMod_info = require("./Moderate Balance_info.jpg");
    // const imgMod = require("./Moderate Balance.jpg");

    const imgAgg = require("./Aggressive.jpg");
    const imgCon = require("./Conservative.jpg");
    const imgGrow = require("./Growth Balance.jpg");
    const imgMod = require("./Moderate Balance.jpg");


    this.state = {
      // value here is the one that determines the portfolio
      index: 0,
      imgList: [
        imgAgg,
        imgCon,
        imgGrow,
        imgMod
      ]
    };
  }

  // just need to set the routing for the rest of the if statements
  // can try put the img below? cuz now like i stuck on
  onLoadA(){

    var dict = maindb[0]
    var keydict = Object.keys(maindb[0])
    var userid = keydict[keydict.length - 1]
    var profile = dict[userid].user_profile
    console.log(profile)
    switch(profile){
      case 'Aggressive':
        this.setState({
          index: 0
        })
        return;
      case 'Growth Balance':
        this.setState({
          index: 2
        })
        return;
      case 'Conservative':
        this.setState({
          index: 1
        })
        return;
      case 'Moderate Balance':
        this.setState({
          index:3
        });
        return;
    }
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
  };

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
  };

  Aimdone = () => {
    window.location.href = "/full";
  };

  render() {
    var keys = Object.keys(maindb[0])
    var lastUser = keys[keys.length -1]
    // console.log(lastUser)
    // console.log(Object.keys(maindb[0])[])
    return (
      <div>
        <body onLoad={this.onLoadA}>
          {/* <button onClick={this.onClickBack}>Back to Previous</button>
          <button onClick={this.Aimdone}>To Stock Explorer</button> */}
          <br />

          <br />
          {/* <globalThis.onLoad></globalThis.onLoad> */}

          <img src={this.state.imgList[this.state.index]} alt="" />
          </body>

      </div>
    );
  }
}

export default Allocation;
