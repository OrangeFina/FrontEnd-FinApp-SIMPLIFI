import React from "react";
import axios from "axios";
import Newsoutput from "./newsoutput";
import Sinputs from "./sinputs";
import AaplChart from "./aaplchart";
import DailyStockChart from "./daily_stock_chart.js";

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
          <DailyStockChart />
        </div>
        <div className="inline">
          <Newsoutput />
        </div>
      </div>
    ];
  }
}

export default Newsoutput2;

// range of date
// if column[date] is within range of date
// append into new array
// new array sort by top
// take out top 3
