# Astronomer Cosmos Install using `jaffle_shop duckdb` dbtproject

## Steps:

1. Start Astro CLI with `astro dev init`
2. Open Dockerfile and put this code to _install dbt into a virtual environment_
    > RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
        pip install --no-cache-dir dbt-duckdb && deactivate
3. Install cosmos pasting `astronomer-cosmos==1.10.2` on requirements.txt (check for latests version on [cosmos github][cosmos])
4. Put Jaffle_shop dbt worflow into project: 
    * Created new folder `dbt` inside project
    * `cd dbt` to get into dbt folder
    * git Clonned [Jaffle_shop][Jaffle_shop] project on duck db
5. Open `profiles.yml` and change path to duck_db local db. In this case is the folder path inside docker container that is running airflow instance
6. (Optional) Set up a Python virtual environment with Airflow for IDE autocompletion:
    * Airflow will run inside the Docker container, not on your local machine.This step is only to enable code autocompletion in your IDE
    * Navigate to the project root folder
    * Create a virtual env `uv venv` or `python -m venv .venv`
    * Run `pip install -r requirements.txt` to install Cosmos (Airflow will be installed automatically as a dependency)
    * Edit gitignore with .venv 
7. Remove exampledag.py from dags folder and created my_dag.py file
8. Define on my_dag.py file the dbt profile, project and execution config
9. Configure .env with AIRFLOW_CONN_DUCKDB_DEFAULT
10. Run astro dev start



<!-- Links -->
[cosmos]:(https://github.com/astronomer/astronomer-cosmos?tab=readme-ov-file)
[Jaffle_shop]: (https://github.com/dbt-labs/jaffle_shop_duckdb.git)