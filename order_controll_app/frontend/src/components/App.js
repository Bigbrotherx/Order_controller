import React, { Component } from "react";
import { createRoot } from "react-dom/client";
import HomePage from "./HomePage";
import { Box } from "@mui/material";


export default class App extends Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <Box className="center">
        <HomePage />
      </Box>
    );
  }
}

const appDiv = document.getElementById("app");
const root = createRoot(appDiv);
root.render(<App />);
