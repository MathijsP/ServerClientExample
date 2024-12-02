# Simple Server Client example.
This public repo contains a simple python server - client example. It uses poetry (https://python-poetry.org/docs/) to handle dependencies (it pins dependecy versions in a poetry.lock file and installs them in a virtual environment - the exact setup can then be reproduced by running poetry install). 

# Components.
A simple server is set up in main.py using FastAPI. A fixed json scheme is established using pydantic (see models.py - for an example json file that adheres to the defined schema see simple.json). In client.py an example of a client application is available, that sends an http POST request with a json payload (i.e. inputs) that is then processed by the server, returning a response (outputs).

# Usage.
- Set up using "poetry install". (Will require poetry to be installed first)
- Run the server using "poetry run python3 main.py".
- Run the client (in a different terminal) using "poetry run python3 client.py"

# Obvious expansions.
- Using a database to hold users and tokens.
- Adding other functions to do CRUD operations to add and remove users.