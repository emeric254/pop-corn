# popcon-organisation

This project require __python 3.10 +__.


## Setup

Make sure you got the basic _python_ packages installed.

```shell
python3
python3-venv
python3-pip
python3-setuptools
python3-wheel
```

You can now set up a local environment for this project. 

```shell
python -m venv --upgrade --upgrade-deps ./venv

. venv/bin/activate

pip install -U -r requirements.txt
pip install -U -r requirements.test.txt
```

Requirements may need more system packages to be installed.


## Configuration

First you need to create a copy of the default settings file.
Then you can edit to reflect your local environment.

```shell
# create settings file
cp reference.env configuration.env

# edit the settings
$EDITOR configuration.env
```

### Keys

This server requires a pair of keys to be able to generate tokens.
It also needs a key to be able to encrypt and decrypt from and into the database.
You can create them with the basic `openssl` tool.

```shell
# generate a key for jwt
openssl genpkey -algorithm ED448 -out jwt.key
openssl pkey -in jwt.key -pubout -out jwt.key.pub
```

### Output folder

This server will read and write files from a folder.
Those files are also read by the `popcon-compagnon` project.
The folder is symlinked `popcon-compagnon/public/donnees/` reference the folder `donnees/` from here.


## Start the server

The server can be started using this command:
```shell
uvicorn main:app --port 8088 --reload
```

You can also use the utility script.
It will ensure the `venv` exists, check the dependencies and start the server:
```shell
bash lancer.sh
```

Once it started you can find the server running over [http://127.0.0.1:8088/](http://127.0.0.1:8088/)

The server also generate the associated OpenApi documentation at [http://127.0.0.1:8088/docs](http://127.0.0.1:8088/docs)
(a ReDoc format is also available at [http://127.0.0.1:8088/redoc](http://127.0.0.1:8088/redoc))

The OpenApi JSON definition file is accessible using [http://127.0.0.1:8088/openapi.json](http://127.0.0.1:8088/openapi.json)


## Build the container image

The server container image can be build using this command:
```shell
bash construire.sh
```