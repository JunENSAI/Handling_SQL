# Handling_SQL

The repository `Handling SQL` contains :

- Python file (`.py`) related on : 

    - `Database connection` with **psycopg2** and **sqlalchemy**, 

    - SQL commands that have an equivalent in `pandas`

- Markdown file (`.md`) related on :

    - Concepts explanation,

    - Syntax example

- SQL file (`.sql`) related on :

    - Code that will be run on `Dbeaver`,

    - Practice samples on SQL commands like `SELECT`, `CREATE`, `INSERT`, `UPDATE`, etc

## Python

To run efficiently the code provided in `.py` you must :

- Create a virtual environnement to make sure that the packages does not collapse with other dependencies

```bash
python3 -m venv name_env
```

- To activate the virtual environnement that you name :

```bash
source path/name_env/bin/activate
```
- Install the packages required for this repo :

```bash
pip install -r requirements.txt
```
---

## SQL

To run the code in `.sql` file you must have :

- Postgres installed on your computer. If not follow the steps :

    - install Postgres with apt

    ```bash
    sudo apt install postgresql postgresql-contrib -y
    ```
    - test your interface
    ```bash
    sudo -u postgres psql
    ```
    - create user with password, then create database that owns by your new user. Grant all privileges for this users
    ```bash
    CREATE USER user_name WITH PASSWORD 'user_pwd';
    CREATE DATABASE db_user OWNER user_name;
    GRANT ALL PRIVILEGES ON DATABASE db_user TO user_name;
    ```
    - **remember your user_name et the password associed on that user**

- Dbeaver (community edition) is used because it's simple to manipulate and configure. Here is the step to follow :

    - install Dbeaver :
    ```bash
    curl -fsSL https://dbeaver.io/debs/dbeaver.gpg.key | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/dbeaver.gpg
    echo "deb https://dbeaver.io/debs/dbeaver-ce /" | sudo tee /etc/apt/sources.list.d/dbeaver.list
    sudo apt update && sudo apt install dbeaver-ce -y
    ```
    - Download the pagila database on : https://www.postgresql.org/ftp/projects/pgFoundry/dbsamples/pagila/pagila/.

    - unzip the file `pagila-0.10.1.zip`.

    - Go to your Dbeaver interface : `Database` --> `New Database connection` --> `select Postgresql` --> `Replace the information (database, Username and password)` from the user creation on postgres step  and finally `Test Connection`.

    - Normally you saw your database connected click : `Database` --> `your_database`` (right click on it) --> `SQL editor` --> Open SQL script` --> Right click on the new windows --> `File` --> `Import SQL scipt`

    - You need to import the three `.sql` file from pagila folder one by one

---