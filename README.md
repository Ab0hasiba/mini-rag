# mini-rag

this is a minimal rag project implementation

# Requirments

- python 3.8 or later

# installation 

- download anaconda
- create an environment for this project
  ```bash 
  $ conda create -n mini-rag python=3.8 
  ```
- activate the environment
  ```bash 
  $ conda activate mini-rag 
  ```
# install requirements 


```bash 
$ pip install -r requirements.txt
```
# Setup the env variables
```bash
$ cp .env.example .env
```
set your env variables in the `.env` file

# run the fastapi server
```bash
$ uvicorn main:app --reload
```