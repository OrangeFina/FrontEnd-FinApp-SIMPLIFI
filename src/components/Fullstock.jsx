import React, { Component } from "react";
import axios from "axios";
import data from "./stockdata";

var i = 49;
var ii = 68;
var iii = 382;

class FullStock extends Component {
  render() {
    return (
      <div className="full">
        <div className="sticker">
          <h1 className="header">Ticker: {data.Ticker[i]}</h1>
          <h2 className="header">Company Name: {data.CompanyName[i]}</h2>
          <ul className="fullstock">
            <h6>Market Capitalisation: {data.MarketCap[i]}</h6>
            <h6>Net Income (TTM): {data.NetIncome[i]}</h6>
            <h6>Revenue (TTM): {data.Revenue[i]}</h6>
            <h6>Book Value per Share: {data.BookValueShare[i]}</h6>
            <h6>Cash per Share: {data.CashShare[i]}</h6>
            <h6>Dividend: {data.Dividend[i]}</h6>
            <h6>Mean Recommendation: {data.MeanRecommendation[i]}</h6>
            <h6>P/E: {data.PE[i]}</h6>
            <h6>Forward P/E: {data.FwdPE[i]}</h6>
            <h6>PEG: {data.PEG[i]}</h6>
            <h6>P/S: {data.PS[i]}</h6>
            <h6>P/B: {data.PB[i]}</h6>
            <h6>P/C: {data.PC[i]}</h6>
            <h6>P/FCF: {data.PFCF[i]}</h6>
            <h6>Quick Ratio: {data.QuickRatio[i]}</h6>
            <h6>Current Ratio: {data.CurrentRatio[i]}</h6>
            <h6>Debt/Equity: {data.DebtEquity[i]}</h6>
            <h6>LT Debt/Equity: {data.LTDebtEquity[i]}</h6>
            <h6>EPS (TTM): {data.EPS[i]}</h6>
            <h6>EPS (Next Y): {data.EPSNextY[i]}</h6>
            <h6>EPS (Next Q): {data.EPSNextQ[i]}</h6>
            <h6>EPS % (Past 5Y): {data.EPSPast5Y[i]}</h6>
            <h6>Sales Growth (Past 5Y): {data.SalesGrowthPast5Y[i]}</h6>
            <h6>Sales Q/Q: {data.SalesQQ[i]}</h6>
            <h6>EPS Q/Q: {data.EPSQQ[i]}</h6>
            <h6>ROA (TTM): {data.ROA[i]}</h6>
            <h6>ROE (TTM): {data.ROE[i]}</h6>
            <h6>ROI (TTM): {data.ROI[i]}</h6>
            <h6>Gross Margin: {data.GrossMargin[i]}</h6>
            <h6>Operating Margin: {data.OperatingMargin[i]}</h6>
            <h6>Profit Margin: {data.ProfitMargin[i]}</h6>
            <h6>Shares Outstanding: {data.SharesOutstanding[i]}</h6>
            <h6>Shares Float: {data.SharesFloat[i]}</h6>
            <h6>52W Range: {data.W52Range[i]}</h6>
            <h6>Avg 3M Volume: {data.Avg3MVolume[i]}</h6>
            <h6>Volume: {data.Volume[i]}</h6>
            <h6>Beta: {data.Beta[i]}</h6>
            <h6>Prev Close: {data.PrevClose[i]}</h6>
          </ul>
        </div>
      </div>
    );
  }
}

export default FullStock;
