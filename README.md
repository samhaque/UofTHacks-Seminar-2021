## Pre-Work
1. [Sign up for Heroku](https://www.heroku.com/home) (billing information NOT required for Free plan)
2. [Have a Github account](https://github.com/join)
3. [Git installed](https://git-scm.com/)
4. [SSH keys configured for your account](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)
5. [Docker installed](https://docs.docker.com/get-docker/)
6. [Install the heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

## Installation
1. Download and install latest version of Python for your operating system: [Here](https://www.python.org/downloads/)
2. Clone this project:
   ```
   git@github.com:samhaque/UofTHacks-Seminar-2021.git
   ```
3. Create a python virtual environment and install all the dependencies
   
   ### Windows
   ```
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ```
   ### Mac/Linux
   ```
   python3 -m venv venv
   source ./venv/bin/activate
   pip install -r requirements.txt
   ```
4. Run the app:
   ```
   uvicorn app.main:app --reload
   ```
5. Test the app:
   ```
   pytest test/test.py
   ```
   
## Build
1. Build the docker image:
   ```
   docker build -t uofthacks-2021-api .
   ```
2. Run and test the docker image:
   ```
   docker run --rm -it -p 8000:8000 uofthacks-2021-api
   ```

## Deploy to Heroku
[Docs](https://devcenter.heroku.com/articles/container-registry-and-runtime)

Live demo
   
