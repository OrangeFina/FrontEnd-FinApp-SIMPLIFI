import React, { Component } from "react";
import axios from "axios";
import details from "./details";
import stockdetails from "./1";

class FullStock1 extends Component {
  
  handleSubmit = () => {
    // const question = {
    //   'question': this.state.inputs
    // };

    // // formats the inputs for django
    // const submission = querystring.stringify(question); 
    axios
      .get("http://127.0.0.1:8000/stockexplorer?"+ "load")
      .then(res => {
        console.log(res);
        console.log(res.data);
        window.location = "/counter";
        
      });
  };
// just copy paste this 3 times and route to each button easier then each page just 1 = 1,2,3

  render() {

    return (
      <div className="full">
        <body onload = {this.handleSubmit}>
        <div className="sticker">
          {/* <h1 className="header">Ticker: {details.Ticker[0]}</h1> */}
          <h2 className="header">Company Name: {stockdetails.company_name_ticker[0]}</h2>
          <ul className="fullstock">
            <h6>Market Capitalisation: {stockdetails.market_cap[0]}</h6>
            <h6>Net Income (TTM): {stockdetails.net_income[0]}</h6>
            <h6>Revenue (TTM): {stockdetails.revenue[0]}</h6>
            <h6>Book Value per Share: {stockdetails.book_value_share[0]}</h6>
            <h6>Cash per Share: {stockdetails.cash_share[0]}</h6>
            <h6>Dividend: {stockdetails.div[0]}</h6>
            {/* <h6>Mean Recommendation: {stockdetails.MeanRecommendation[0]}</h6> */}
            <h6>P/E: {stockdetails.pe[0]}</h6>
            <h6>Forward P/E: {stockdetails.pe_fwd[0]}</h6>
            <h6>PEG: {stockdetails.peg[0]}</h6>
            <h6>P/S: {stockdetails.ps[0]}</h6>
            <h6>P/B: {stockdetails.pb[0]}</h6>
            <h6>P/C: {stockdetails.pc[0]}</h6>
            <h6>P/FCF: {stockdetails.pfcf[0]}</h6>
            <h6>Quick Ratio: {stockdetails.quick_ratio[0]}</h6>
            <h6>Current Ratio: {stockdetails.current_ratio[0]}</h6>
            <h6>Debt/Equity: {stockdetails.debt_equity[0]}</h6>
            {/* <h6>LT Debt/Equity: {stockdetails.LTDebtEquity[0]}</h6> */}
            <h6>EPS (TTM): {stockdetails.eps_ttm[0]}</h6>
            {/* <h6>EPS (Next Y): {stockdetails.EPSNextY[0]}</h6>
            <h6>EPS (Next Q): {stockdetails.EPSNextQ[0]}</h6>
            <h6>EPS % (Past 5Y): {stockdetails.EPSPast5Y[0]}</h6> */}
            {/* <h6>Sales Growth (Past 5Y): {stockdetails.SalesGrowthPast5Y[0]}</h6> */}
            <h6>Sales Q/Q: {stockdetails.sales_qonq[0]}</h6>
            <h6>EPS Q/Q: {stockdetails.eps_qonq[0]}</h6>
            <h6>ROA (TTM): {stockdetails.roa[0]}</h6>
            <h6>ROE (TTM): {stockdetails.roe[0]}</h6>
            <h6>ROI (TTM): {stockdetails.roi[0]}</h6>
            <h6>Gross Margin: {stockdetails.gross_margin[0]}</h6>
            <h6>Operating Margin: {stockdetails.op_margin[0]}</h6>
            <h6>Profit Margin: {stockdetails.profit_margin[0]}</h6>
            <h6>Shares Outstanding: {stockdetails.shares_outstanding[0]}</h6>
            <h6>Shares Float: {stockdetails.shares_float[0]}</h6>
            <h6>52W Range: {stockdetails.fifty_two_weeks[0]}</h6>
            {/* <h6>Avg 3M Volume: {stockdetails.Avg3MVolume[0]}</h6>
            <h6>Volume: {stockdetails.Volume[0]}</h6> */}
            <h6>Beta: {stockdetails.beta[0]}</h6>
            <h6>Prev Close: {stockdetails.prev_close[0]}</h6>
          </ul>
        </div>
        </body>
      </div>
    );
  }
}

export default FullStock1;
