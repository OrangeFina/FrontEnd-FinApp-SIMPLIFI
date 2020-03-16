import React from "react";
import axios from "axios";

// for axios and django integration added querystring import

import querystring from 'querystring';

class Qinputs extends React.Component {
  state = {
    inputs: []
  };

  Qimdone = () => {
    this.handleSubmit();
  };

  handleChange = event => {
    //appends new value into array
    this.state.inputs.push(event.target.value);
  };
  

  handleSubmit = () => {
    const question = {
      'question': this.state.inputs
    };

    // formats the inputs for django
    const submission = querystring.stringify(question); 
    axios
      .get("http://127.0.0.1:8000/risk-list?" + submission,{question})
      .then(res => {
        console.log(res);
        console.log(res.data);
        window.location = "/counter";
      });
  };

  render() {
    return (
      <div>
        <h2 class="header">Questionnaire</h2>
        <form id="myForm" method='get'>
          <label>
            <div class="question">Question 1</div>
            <b>
              {" "}
              Which of the following do you think best describes your investment
              objectives?{" "}
            </b>
            <br />
            <br />
            A. Your primary focus is on capital growth. You are prepared to
            accept a high level of short term volatility and possible capital
            losses in order to generate potentially higher levels of capital
            growth over the long term. You are well placed to recover from
            unforeseen market downturns either because you have time on your
            side or access to capital reserves.
            <br />
            <br />
            B. You require your investments to be a balance between capital
            growth and income generating assets. Calculated risks will be
            acceptable as you are prepared to accept short term levels of
            volatility in order to outperform inflation.
            <br />
            <br />
            C. Generating a regular income stream is a priority over capital
            growth. You are prepared to sacrifice higher returns in favour of
            preservation of capital
          </label>
          <br />
          <input
            onChange={this.handleChange}
            type="text"
            name="question1"
            placeholder="A , B , C"
          />
          <br />
          <div class="question">Question 2</div>
          <b>
            {" "}
            What percentage of your risk capital are you comfortable will you be
            investing?{" "}
          </b>
          <br />
          <br />
          <b>
            ** Risk capital means funds and assets which if lost would not
            materially change your lifestyle or your family's lifestyle.{" "}
          </b>
          <br />
          <br />
          A. Greater than 70%
          <br />
          <br />
          B. 35% to 70%
          <br />
          <br />
          C. Less than 35%
          <br />
          <input
            onChange={this.handleChange}
            type="text"
            name="question2"
            placeholder="A , B , C"
          />
          <br />
          <label>
            <div class="question">Question 3</div>
            <b>
              {" "}
              Once investments have been placed, how long would it be before you
              would need to access your capital?
            </b>
            <br />
            <br />
            A. > 2 Years
            <br />
            <br />
            B. Between 6 Months and 2 Years
            <br />
            <br />
            C. Less than 6 Months
          </label>
          <br />
          <input
            onChange={this.handleChange}
            type="text"
            name="question3"
            placeholder="A , B , C"
          />
          <br />
          <label>
            <div class="question">Question 4</div>
            <b>
              {" "}
              Inflation can reduce your spending power. How much risk are you
              prepared to take to counteract the effects of inflation?{" "}
            </b>
            <br />
            <br />
            A. I am comfortable with short to medium term losses in order to
            beat inflation over the long term.
            <br />
            <br />
            B. I am conscious of the effects of inflation, and am prepared to
            take moderate risks in order to stay ahead of inflation.
            <br />
            <br />
            C. Inflation may erode my savings over the long-term, but I am only
            willing to take limited risks to attempt to counter the effects of
            inflation.
          </label>
          <br />
          <input
            onChange={this.handleChange}
            type="text"
            name="question4"
            placeholder="A , B , C"
          />
          <br />
          <label>
            <div class="question">Question 5</div>
            <b>
              {" "}
              How much money have you set aside (outside of your pension /
              Central Provident Fund savings) to handle emergencies?{" "}
            </b>
            <br />
            <br />
            A. More than six(6) months of living expenses.
            <br />
            <br />
            B. Between one(1) and six(6) months of living expenses.
            <br />
            <br />
            C. Less than one(1) month of living expenses.
          </label>
          <br />
          <input
            onChange={this.handleChange}
            type="text"
            name="question5"
            placeholder="A , B , C"
          />
          <br />
          <label>
            <div class="question">Question 6</div>
            <b>
              {" "}
              You possess $100,000 and wish to invest the funds for the future.
              Which of the asset mixes would you choose to invest in?{" "}
            </b>
            <br />
            <br />
            Investment A has a potential return of 30% but the possibility of
            losing up to 40% in any year.
            <br />
            <br />
            Investment B has a potential return of 3% with the possibility of
            losing up to 5% in any year.
            <br />
            <br />
            A. 80% in Investment A and 20% in Investment B
            <br />
            <br />
            B. 50% in Investment A and 50% in Investment B
            <br />
            <br />
            C. 20% in Investment A and 80% in Investment B
          </label>
          <br />
          <input
            onChange={this.handleChange}
            type="text"
            name="question6"
            placeholder="A , B , C"
          />
          <br />
          <label>
            <div class="question">Question 7</div>
            <b>
              {" "}
              Over the long term, what returns do you reasonably expect to
              achieve from your portfolio.?{" "}
            </b>
            <br />
            <br />
            A. More than 9% per annum above the fixed deposit rate.
            <br />
            <br />
            B. 3% - 9% per annum above the fixed deposit rate.
            <br />
            <br />
            C. Less than 3% per annum above the fixed deposit rate.
          </label>
          <br />
          <input
            onChange={this.handleChange}
            type="text"
            name="question7"
            placeholder="A , B , C"
          />
          <br />
          <label>
            <div class="question">Question 8</div>
            <b>
              {" "}
              Most investments can fluctuate both up and down (i.e volatility).
              How much could your investment fall in value over a 12 months
              period before you begin to feel concerned and anxious?{" "}
            </b>
            <br />
            <br />
            A. More than 25%.
            <br />
            <br />
            B. Up to 25%.
            <br />
            <br />
            C. Up to 5%.
          </label>
          <br />
          <input
            onChange={this.handleChange}
            type="text"
            name="question8"
            placeholder="A , B , C"
          />
          <br />
          <label>
            <div class="question">Question 9</div>
            <b>
              {" "}
              What would your reaction be if six months after placing your
              investment you discover that your portfolio had decreased in value
              by 20%?{" "}
            </b>
            <br />
            <br />
            A. I would invest more funds to lower my average investment price,
            expecting future growth.
            <br />
            <br />
            B. This was a calculated risk and I would leave the investment in
            place, expecting future growth.
            <br />
            <br />
            C. I would cut my losses.
          </label>
          <br />
          <input
            onChange={this.handleChange}
            type="text"
            name="question9"
            placeholder="A , B , C"
          />
          <br />
          <label>
            <div class="question">Question 10</div>
            <b>
              {" "}
              To what extent are you concerned about preservation of your
              capital?{" "}
            </b>
            <br />
            <br />
            A. A high degree of risk would be acceptable given long term capital
            growth objectives.
            <br />
            <br />
            B. A moderate degree of risk would be acceptable given the potential
            for increased returns.
            <br />
            <br />
            C. A minimal degree of risk would be acceptable for a slight
            increase in potential returns.
          </label>
          <br />
          <input
            onChange={this.handleChange}
            type="text"
            name="question10"
            placeholder="A , B , C"
          />
          <br />
          <label>
            <div class="question">Question 11</div>
            <b>
              {" "}
              What are your current income requirements from your investments?{" "}
            </b>
            <br />
            <br />
            A. I require a small amount of investment income as I am mainly
            focused on capital growth.
            <br />
            <br />
            B. I require an equal combination of investment income and capital
            growth.
            <br />
            <br />
            C. I require substantial investment income with only some capital
            growth.
          </label>
          <br />
          <input
            onChange={this.handleChange}
            type="text"
            name="question11"
            placeholder="A , B , C"
          />
          <br />
          <label>
            <div class="question">Personal Details</div>
          </label>
          <br />
          <b> Your Education </b>
          <br />
          <input
            onChange={this.handleChange}
            type="text"
            name="question12"
            placeholder="Business, Chemistry, Engineering"
          />
          <br />
          <b> Your Profession </b>
          <br />
          <input
            onChange={this.handleChange}
            type="text"
            name="question13"
            placeholder="Chemist, Driver, Manager"
          />
          <br />
          <b> Your Interest </b>
          <br />
          <input
            onChange={this.handleChange}
            type="text"
            name="question14"
            placeholder="Basketball, Tennis, Gardening"
          />
          <br />
          <button type="submit" onClick={this.Qimdone}>
            Update
          </button>
        </form>
      </div>
    );
  }
}

export default Qinputs;
