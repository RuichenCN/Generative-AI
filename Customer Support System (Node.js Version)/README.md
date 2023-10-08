# Customer Support System (Node.js Version)
## Step1: Create a web-based interface to ChatGPT using Javascript/Node.js
1. Install Node.js in your system
2. Download the ChatGPT sample code by cloning this repository

   a. Creating the working directory
   ```
   mkdir quickstart_node
   cd quickstart_node
   ```

   b. Download the code to the working directory
   ```
   git clone https://github.com/openai/openai-quickstart-node.git
   ```
3. Add your API key
   ```
   cd openai-quickstart-node
   cp .env.example .env
   vi .env
   ```
4. Run the app(server)
   
   Run the following commands in the project directory (.../quickstart_node/openai-quickstart-node) to install the dependencies and run the app

   a. install npm
   ```
   npm install
   ```
   <img width="496" alt="Screenshot 2023-10-03 at 3 12 45 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/23c8ec10-519d-4183-998b-1d8e684a2aa9">
   
   b. npm run dev
   ```
   npm run dev
   ```
   <img width="566" alt="Screenshot 2023-10-03 at 3 13 38 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/d3e52be0-8f4b-4547-abd4-b303ed90dbb0">
   
5. Open a browser to access

   Address: http://localhost:3000
   <img width="1440" alt="Screenshot 2023-10-03 at 3 02 12 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/58d7572f-b115-4f58-b58b-78ef10bd4c04">

## Step2: Integrate the Javascript (Node.js) code
🎯 Target: Create a web-based interface to let the users ask ChatGPT questions about the website using a browser.

Put this file into the same directory with web-flask.py
app.js:
```
const { exec } = require("child_process");

// Replace 'python_script.py' with the path to your Python script.
const pythonScriptPath = "web-flask.py";

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
```
Then run the code use this command:
```
node app.js
```
<img width="1440" alt="Screenshot 2023-10-07 at 12 21 14 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/a6b94f03-9fd6-412a-a638-8ddb679e5f57">

