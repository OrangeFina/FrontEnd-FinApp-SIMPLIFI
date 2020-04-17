/* daily_stock_chart.js */
import CanvasJSReact from './canvasjs.react';
import React, {Component} from 'react';
// import './App.css';
import chartticker from "./ticker_chart";

    var CanvasJS = CanvasJSReact.CanvasJS;
    var CanvasJSChart= CanvasJSReact.CanvasJSChart;
	var dataPoints = [] ;
	


//var React = require('react');
//var Component = React.Component;
//var CanvasJSReact = require('./canvasjs.react');
//var CanvasJS = CanvasJSReact.CanvasJS;
//var CanvasJSChart = CanvasJSReact.CanvasJSChart;
//var dataPoints =[];
	
    class DailyStockChart extends Component {

    	componentDidMount(){
			var chart = this.chart;

			/* To host "stock_ticker_chart.json" file created previously on server and API from there*/
			
			fetch('http://127.0.0.1:8000/chartdb')
    		.then(function(response) {
    			return response.json();
    		})
    		.then(function(data) {
    			for (var i = 0; i < data.length; i++) {
    				dataPoints.push({
    					x: data[i].x,
    					y: data[i].y
    				});
    			}
    			chart.render();
    		});
		}
		render() {
    		const options1 = {
    			exportEnabled: true,
    			title: {
    				text: "Stock Price"
    			},
    			axisX: {
    				valueFormatString: "DD MMM"
    			},
    			axisY: {
    				title: "Price",
    				includeZero: false,
    				prefix: "$"
    			},
    			data: [{
    				type: "candlestick",
    				name: "Stock Price",
    				showInLegend: true,
					yValueFormatString: "$##0.00",
					xValueFormatString: "DD MMM",
    				xValueType: "dateTime",
    				dataPoints: dataPoints
    			}]
    		}
    		return (
    			<div>
    			<CanvasJSChart options = {options1}
    				 onRef={ref => this.chart = ref}
    			/>
    			{/*You can get reference to the chart instance as shown above using onRef. This allows you to access all chart properties and methods*/}
    			</div>
    		);
    	}
    }
    export default DailyStockChart;    