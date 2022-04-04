## .env
```bash
cp .env-example .env
```
### Edit .env
```bash
MYSQL_USER = your_username
MYSQL_PASSWORD = your_password
MYSQL_HOST = localhost
#MYSQL_PORT = 3306
MYSQL_DATABASE = your_database
```
change the values with your username, password and create database with the name 'salepoint'.

### Install virtual enviroment
Install virtual enviroment with the next command.
```bash
python -m venv venv

#or

python3 -m venv venv
```

### Activate the virtual enviroment
To activate the virtual enviroment with the next command.
```bash
#on linux
. venv/bin/activate

#on windows
. venv/Scripts/activate
```
Once activate the virtual enviroment in the promp you see the (venv).
After you activate the virtual enviroment, you proceed to install the requirements while you see (venv). 

### Install requirements
On python install your requirements with the comand.
```bash
python -r install requirements.txt 

#or

python3 -r install requirements.txt 
```

