## Dublin Bus Data Pipeline - Producer

## UPDATE
This repo is under active maintenance. Updates will be documented here.

## Requirements
- `docker`
- `RabbitMQ` (will be moving to supporting RabbitMQ on Docker shortly)

### What does this project do?
 * Produces a stream of data from Dublin Bus, Dublin Bikes and some other dependent variables such as weather
 - This data is ingested into a RabbitMQ MQ
 - Consumers subscribe to these topics and build an online learning model

#### RabbitMQ specifics
- `docker-compose up`
- `docker build -t pipeline .`

#### Run the project
 * ```python main.py --flag=bus --host=localhost --start_index=0 --end_index=2```

## Repo update
- This repo will undergo active maintenance for the next few months. Will be using RabbitMQ with Spark for stream processing on the consumer side (MLlib)
