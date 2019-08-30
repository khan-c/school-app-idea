import React, { Component } from "react";
import ReactDom from "react-dom";

export class App extends Component {
  render() {
    return <div>Test</div>;
  }
}

ReactDom.render(<App />, document.getElementById("app"));
