import React from "react";
import axios from "axios";
import collatednews from "./collatednews";

class Newsoutput extends React.Component {
  //   state = {
  //     inputs: []
  //   };
  constructor(props) {
    super(props);
    this.state = {
        title: [
          Object.values(collatednews["Title"])
        ],
        date: [
          Object.values(collatednews["Date"])
        ]
        }

    this.items = this.state.title.map((item,key) =>
      <div>
        <il key={key.index}> {item[0]} </il>
        <br />
        <il key={key.index}> {item[1]} </il>
        <br />
        <il key={key.index}> {item[2]} </il>
        <br />
        <il key={key.index}> {item[3]} </il>
        <br />
        <il key={key.index}> {item[4]} </il>
        <br />
        <il key={key.index}> {item[5]} </il>
        <br />
        <il key={key.index}> {item[6]} </il>
        <br />
        <il key={key.index}> {item[7]} </il>
        <br />
        <il key={key.index}> {item[8]} </il>
        <br />
        <il key={key.index}> {item[9]} </il>
        <br />
        <il key={key.index}> {item[10]} </il>
        <br />
        <il key={key.index}> {item[11]} </il>
        <br />
        <il key={key.index}> {item[12]} </il>
        <br />
        <il key={key.index}> {item[13]} </il>
        <br />
        <il key={key.index}> {item[14]} </il>
        <br />
        <il key={key.index}> {item[15]} </il>
        <br />
        <il key={key.index}> {item[16]} </il>
        <br />
        <il key={key.index}> {item[17]} </il>
        <br />
        <il key={key.index}> {item[18]} </il>
        <br />
        <il key={key.index}> {item[19]} </il>
        <br />   
        <il key={key.index}> {item[20]} </il>
        <br />
        <il key={key.index}> {item[21]} </il>
        <br />   
        <il key={key.index}> {item[22]} </il>
        <br />
        <il key={key.index}> {item[23]} </il>
        <br />   
        <il key={key.index}> {item[24]} </il>
        <br />
        <il key={key.index}> {item[25]} </il>
        <br />   
      </div>

    );
    }
  render() {
    var title = Object.values(collatednews["Title"])
    var date = Object.values(collatednews["Date"])
    var formatted = []
    for (var i=0, len=date.length;i<len;i++){
      var placeholder = new Date(date[i])
      placeholder = placeholder.toLocaleDateString()
      formatted.push(placeholder)
    }
    console.log(date.toLocaleString())
    return (
      <form className="full">
        <div className="sticker">
          <label>
            <b> Relevant News</b>
          </label>
          <ul>
          <il> {formatted[0]}: {title[0]} </il>
          <br />
          <il> {formatted[1]}: {title[1]} </il>
          <br />
          <il> {formatted[2]}: {title[2]} </il>
          <br />
          <il> {formatted[3]}: {title[3]} </il>
          <br />
          <il> {formatted[4]}: {title[4]} </il>
          <br />
          <il> {formatted[5]}: {title[5]} </il>
          <br />
          <il> {formatted[6]}: {title[6]} </il>
          <br />
          <il> {formatted[7]}: {title[7]} </il>
          <br />
          <il> {formatted[8]}: {title[8]} </il>
          <br />
          <il> {formatted[9]}: {title[9]} </il>
          <br />
          <il> {formatted[10]}: {title[10]} </il>
          <br />
          <il> {formatted[11]}: {title[11]} </il>
          <br />
          <il> {formatted[12]}: {title[12]} </il>
          <br />
          <il> {formatted[13]}: {title[13]} </il>
          <br />
          <il> {formatted[14]}: {title[14]} </il>
          <br />
          <il> {formatted[15]}: {title[15]} </il>
          <br />
          <il> {formatted[16]}: {title[16]} </il>
          <br />
          <il> {formatted[17]}: {title[17]} </il>
          <br />
          <il> {formatted[18]}: {title[18]} </il>
          <br />
          <il> {formatted[19]}: {title[19]} </il>
          <br />   
          <il> {formatted[20]}: {title[20]} </il>
          <br />
          <il> {formatted[21]}: {title[21]} </il>
          <br />   
          <il> {formatted[22]}: {title[22]} </il>
          <br />
          <il> {formatted[23]}: {title[23]} </il>
          <br />   
          <il> {formatted[24]}: {title[24]} </il>
          <br />
          <il> {formatted[25]}: {title[25]} </il>
          <br />   
          </ul> 
        </div>
      </form>
    );
  }
}

export default Newsoutput;
