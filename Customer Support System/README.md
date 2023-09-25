# Web-based Solution (Python Flask webserver)
## 1. Use Python to create a web-based interface to ChatGPT
#### Step1. Download the ChatGPT sample code by cloning this repository
1. Creating the working directory
```
mkdir quickstart_python
```
```
cd quickstart_python
```
2. Download the code to the working directory
```
git clone https://github.com/openai/openai-quickstart-python.git
```
#### Step2. Add your API key
```
cd openai-quickstart-python
cp .env.example .env
vi .env
```
#### Step3. Run the app
Current: You are in .../quickstart_python/openai-quickstart-python
1. Edit the file "run"
```
vi run
```
```
# python -m venv venv
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
flask run
```
2. Add execution permissions
```
chmod 755 run
```
3. run the file
```
./run
```
Open Chrome brower and enter the address: http://127.0.0.1:5000/

The result:

<img width="1438" alt="Screenshot 2023-09-24 at 4 08 29 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/c50490a3-9efc-4447-b2ec-7c66c3ea37e3">


## 2. Integrate the Python code to a create a web-based interface
Target: to let the users ask ChatGPT questions about the website using a browser.

1. Install Flask
```
pip install Flask
```
2. Create a python script

Download my code in web-flask.py.

3. Download the file "templates"

It contains two html files: index.html and result.html

4. Add your api key

Download "api_key.txt" and put your api key in this txt.

5. Implement the web-flask.py

The result:

<img width="1440" alt="Screenshot 2023-09-24 at 6 04 43 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/416a8c21-9b67-4c38-bd74-d75a10dd67ae">


