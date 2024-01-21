# Pokemon_api and MongoDB
## Project objective
Create an ETL process that extracts Pokemons information from an API in a Json format, load it into a MongoDB database. Then extract it again, transform it with Pandas, and load it to PostgreSQL with a simple model design.

## Execution
The project can be executed by anyone. It only needs Docker, being independant from local environment. With the command "docker-compose -up" you can build:
- postgre container
- mongodb container
- airflow containers
All of them are configured in the docker-compose file and already configured within the scripts to be connected successfully.

## Validation
The two last tasks of the DAG, validate the correct load into both Databases by querying some sample data from them.

