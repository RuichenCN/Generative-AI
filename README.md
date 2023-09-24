# Generative-AI
Generative AI-Driven Intelligent Apps Development

# Development Environment Setup(With Ubuntu)
* My System Info:  
  MacBook Air M1 2020  
  Mac OS 13.4    
  Memory 8GB

## Step1: Install Ubuntu
💡This step is optional for a Mac user.
1. Download Ubuntu Server for ARM

   [Link](https://ubuntu.com/download/server/arm)

   <img width="434" alt="Screenshot 2023-09-07 at 11 13 28 AM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/87cb7a22-a50f-4741-80c2-b4a060d4a7f3">

2. Download UTM for Mac
   We use UTM as a virtual machine to install Ubuntu

   [Link](https://mac.getutm.app/)

   <img width="480" alt="Screenshot 2023-09-07 at 11 14 41 AM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/7d03a138-20cf-440e-9f20-1ee2fe714d47">

3. Install UTM for Mac

   <img width="477" alt="Screenshot 2023-09-07 at 11 15 10 AM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/53361002-aa68-4d07-878c-4cfc877a1c4d">

4. Create a virtual machine for Mac

   <img width="242" alt="Screenshot 2023-09-07 at 11 15 32 AM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/e2e370ca-d239-4bf3-8aad-2ffedaba17f1">

    For detailed steps, please refer this [video beginning at 2:52](https://www.youtube.com/watch?v=O19mv1pe76M)

5. Intall Ubuntu
   
    <img width="530" alt="Screenshot 2023-09-07 at 11 21 17 AM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/4b78cd8a-369d-4802-bedc-1077017a24cd">

    For detailed steps, please refer this [video beginning at 4:40](https://www.youtube.com/watch?v=O19mv1pe76M)

6. Set up GUI

    Use the username and password set before to login in.

   For detailed steps, please refer this [video beginning at 8:35](https://www.youtube.com/watch?v=O19mv1pe76M)
   
   Code Reference:  
   
   ```
    sudo apt update && sudo apt upgrade -y
   ```
   ```
    sudo apt install ubuntu-desktop
   ```
   ```
    reboot
   ```
   When you get into the Ubuntu, you can see this desktop.
   
    <img width="1282" alt="Screenshot 2023-09-07 at 11 30 19 AM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/f5776462-daac-4106-9885-44730fa61a8f">

    Then, use the following code:

   ```
    sudo apt install spice-vdagent spice-webdavd -y
   ```

## Step2: Prepare the Development Environment
1. Install Python, pip, Virtual Environment

   * Check the python version:  
     ```
      python3 --version
     ```
   * Install pip:  
     ```
      sudo apt update
     ```
     ```
      sudo apt install python3-pip
     ```
   * Install virtualenvwrapper:
     ```
      sudo apt install virtualenv virtualenvwrapper
     ```
   * Update .bashrc file by adding these lines:
   
      <img width="542" alt="Screenshot 2023-09-07 at 4 03 24 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/3ae90c3e-11bd-4f86-94a3-8bc77a3bf3ec">

    * Save the file and configure the update:

     ```
      source ~/.bashrc
     ```
   * Create a virtual environment：
     ```
      mkvirtualenv CS589
     ```
   * Deactivate and activate the virtual environment

     ```
      deactivate
     ```
     ```
      workon CS589
     ```

2. Get OpenAI API keys

   [Sign up an account](https://openai.com/product) and create a new secret key under API Keys menu item.
   
    <img width="1436" alt="Screenshot 2023-09-07 at 4 17 47 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/e8edac1e-8a20-4c75-86cd-569c3364c934">

3. Installing the Official Python Bindings:
     ```
      workon CS589
     ```
     ```
      pip install openai
     ```
4. Testing our API Keys:

   * Create a .env file to store our API Key and organization id

     ```
      nano .env
     ```
     Type your api key and org id into the file.
     You can find org id [here](https://platform.openai.com/account/org-settings)

  * Test authorization
     ```
      source .env
     ```
     ```
      curl https://api.openai.com/v1/models -H 'Authorization: Bearer '$API_KEY'' -H 'OpenAIOrganization: '$ORG_ID''
     ```
     <img width="486" alt="Screenshot 2023-09-07 at 4 44 13 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/c8eaa1dc-4e97-47b4-866e-c7b84f0cacb8">
  * Test API using Python code
     ```
      nano test-env.py
     ```
     ```
      import os
      import openai
      
      def init_api():
          with open(".env") as env:
              for line in env:
                 key, value = line.strip().split("=")
                 os.environ[key] = value
      
           openai.api_key = os.environ.get("API_KEY")
           openai.organization = os.environ.get("ORG_ID")
      
      init_api()
      
      models = openai.Model.list()
      print(models)
     ```

     Run python file to test
     ```
      python3 test-env.py
     ```
     <img width="459" alt="Screenshot 2023-09-07 at 5 47 20 PM" src="https://github.com/RuichenCN/Generative-AI/assets/113652310/a25954ea-9012-4588-90d1-e0858e3ff99d">

# Development Environment Setup(Without Ubuntu)
## Step1: Installing Python, pip, and a Virtual Environment for Development
1. Install Python from [python.org](https://www.python.org/downloads/)

   My python version: 3.10.7

2. Install pip, the Python package installer

   ```
   python get-pip.py
   ```

3. Using virtualenvwrapper

   ```
   pip install virtualenvwrapper
   ```

4. configure virtualenvwrapper

   ```
   nano ~/.zshrc
   ```
   ```
   export WORKON_HOME=$HOME/.virtualenvs
   export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
   source /usr/local/bin/virtualenvwrapper.sh
   ```
   Change the paths according to your own paths. Then save and exist.
   ```
   source ~/.zshrc
   ```
5. Creating a Virtual Environment
   ```
   mkvirtualenv myenv
   ```
6. Activating the Virtual Environment
   ```
   workon myenv
   ```
7. Existing the Virtual Environment
   ```
   deactivate
   ```
