# Generative-AI
Generative AI-Driven Intelligent Apps Development

# Development Environment Setup
* My System Info:  
  MacBook Air M1 2020  
  Mac OS 13.4    
  Memory 8GB

## Step1: Install Ubuntu
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
   
