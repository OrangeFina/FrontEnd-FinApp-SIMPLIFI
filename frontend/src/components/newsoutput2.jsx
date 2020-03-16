import React from "react";
import axios from "axios";
import Newsoutput from "./newsoutput";
import Sinputs from "./sinputs";
import AaplChart from "./aaplchart";

class Newsoutput2 extends React.Component {
  state = {
    inputs: []
  };

  render() {
    return [
      <div>
        <div>
          <Sinputs />
        </div>
        <div>
          <AaplChart />
        </div>
        <div className="inline">
          <Newsoutput />
        </div>
      </div>
    ];
  }
}

export default Newsoutput2;
