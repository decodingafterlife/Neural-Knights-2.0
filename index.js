const express = require("express");
const app = express();
const { PythonShell } = require("python-shell");

app.get("/", (req, res, next) => {
  let options = {
    mode: "text",
    pythonOptions: ["-u"],
    scriptPath: "path/to/my/scripts",
    args: [`${req.body}`],
  };
});
