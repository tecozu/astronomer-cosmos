#Import necessary libraries
from datetime import datetime
from cosmos import ProjectConfig, ProfileConfig, ExecutionConfig, DbtDag
from cosmos.profiles import DuckDBUserPasswordProfileMapping
import os

DUCKDB_CONN_ID = os.getenv("DUCKDB_CONN_ID", "duckdb_default")
DB_PATH = "/usr/local/airflow/include/jaffle_shop.duckdb"
SCHEMA_NAME = os.getenv("DUCKDB_SCHEMA", "main")

DBT_PROJECT_PATH  = "/usr/local/airflow/dbt/jaffle_shop_duckdb"
DBT_EXECUTABLE_PATH = f"{os.getenv('AIRFLOW_HOME')}/dbt_venv/bin/dbt"

# Indicates the path to DBT project 
_project_config = ProjectConfig (
    dbt_project_path = DBT_PROJECT_PATH
)

# Indicates the profile configuration for DuckDB connection using airflow connection
_profile_config = ProfileConfig (
    profile_name = "default",
    target_name = "dev",
    profile_mapping= DuckDBUserPasswordProfileMapping ( 
        conn_id= DUCKDB_CONN_ID,
        profile_args={
            "path": DB_PATH,
            "schema": SCHEMA_NAME
        }
    ))

# Indicates the execution configuration for DBT to run trough local dbt executable
_execution_config = ExecutionConfig (
    dbt_executable_path = DBT_EXECUTABLE_PATH
)

# Instantiate the DbtDag to translate the DBT project into an Airflow DAG
my_dag = DbtDag (
    dag_id = "my_dag",
    project_config = _project_config,
    profile_config = _profile_config,
    execution_config = _execution_config,
    schedule = "@daily",
    start_date = datetime(2025,1,1),
    max_active_tasks = 1
)