const { error } = require("console");
const express = require("express");
const app = express();
const fs = require("fs");
const { PythonShell } = require("python-shell");

app.get("/api", (req, res) => {
  var flag = 0;
  var target = req.query.target;
  if (target) flag += 1;
  var link = req.query.link;
  if (link) flag += 1;

  let options = {
    mode: "text",
    pythonOptions: ["-u"],
    scriptPath: "./interface",
    args: [flag, target, link],
  };
  console.log(link);

  PythonShell.run("main.py", options).then((messages) => {
    console.log("results: %j", messages);
    const data1 = {
      neutral: messages[0],
      joy: messages[1],
      surprise: messages[2],
      anger: messages[3],
      sadness: messages[4],
      fear: messages[5],
      disgust: messages[6],
    };
    const jsonData = JSON.stringify(data1, null, 2);

    fs.writeFileSync("./output.json", jsonData, (error) => {
      if (error) {
        console.log(error);
      } else {
        console.log("File is saved");
      }
    });
    res.status(200).json(data1);
  });
});

const port = 8000;
app.listen(port, () => console.log(`Server connected to ${port}`));
