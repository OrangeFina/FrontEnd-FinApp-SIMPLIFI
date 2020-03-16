import React from "react";
import axios from "axios";

class Newsoutput extends React.Component {
  //   state = {
  //     inputs: []
  //   };

  render() {
    return (
      <form className="full">
        <div className="sticker">
          <label>
            <b> Relevant Idiosyncratic News</b>
          </label>
          <li className="alignleft">
            31/10/19: Apple's wearables drive revenue as iPhone sags
          </li>
          <li className="alignleft">
            30/10/19: Apple goes full bore into 5G phones
          </li>
          <li className="alignleft">
            30/10/19: Apples are the most generous of trees
          </li>
        </div>
        <div className="sticker">
          <label>
            <b> Relevant Systemic News</b>
          </label>
          <li className="alignleft">
            30/10/19: AT&T's video streaming service to cost more than rivals'
          </li>
          <li className="alignleft">
            30/10/19: Sony pulls plug on PlayStation Vue video streaming service
          </li>
          <li className="alignleft">
            30/10/19: Inside the WhatsApp hack: how an Israeli technology was
            used to spy
          </li>
        </div>
      </form>
    );
  }
}

export default Newsoutput;
