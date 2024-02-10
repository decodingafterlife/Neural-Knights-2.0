const express = require("express");
const app = express();
const { PythonShell } = require("python-shell");

app.get("/api", (req, res) => {
  var flag = 0;
  var target = req.query.target;
  if (target) flag += 1;
  var video = req.query.video;
  if (video) flag += 1;

  let options = {
    mode: "text",
    pythonOptions: ["-u"],
    scriptPath: "./interface",
    args: [flag, target, video],
  };

  try {
    PythonShell.run("main.py", options, function (err, result) {
      if (err) throw err;
      // result is an array consisting of messages collected
      //during execution of script.
      console.log("result: ", result.toString());
      res.status(200).json("./output.json");
    });
  } catch {
    console.log("Error");
  }
});

const port = 8000;
app.listen(port, () => console.log(`Server connected to ${port}`));
