import React from "react";

class Skate extends React.Component {
  constructor() {
    super();
    this.state = {data: {}};
  }

  componentDidMount(){
      this.setState({
        data: {}
      });
    };

  render(){
    return(
      <div>
        <header>
          <h1>SKATE</h1>
          <p>posers ONLY</p>
        </header>
      </div>
    );
  }
}

export default Skate;
