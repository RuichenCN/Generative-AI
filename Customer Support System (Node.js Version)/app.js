const { exec } = require("child_process");

// Replace 'python_script.py' with the path to your Python script.
const pythonScriptPath = "./web-flask.py";

// Replace 'arg1' and 'arg2' with any arguments you want to pass to your Python script.
const arguments = ["arg1", "arg2"];

// Construct the command to run the Python script with arguments.
const command = `python3 ${pythonScriptPath} ${arguments.join(" ")}`;

// Execute the Python script from Node.js
exec(command, (error, stdout, stderr) => {
  if (error) {
    console.error(`Error executing Python script: ${error}`);
    return;
  }

  // Parse the Python script's output (assuming it's a JSON string in this example).
  let pythonResult;
  try {
    pythonResult = JSON.parse(stdout);
  } catch (e) {
    console.error("Error parsing Python result:", e);
    return;
  }

  // Use the result in your Node.js application
  console.log("Received Python result:");
  console.log(pythonResult);
});
