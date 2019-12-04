## Dublin Bus Data Pipeline - Producer

## UPDATE
This repo is under active maintenance. Updates will be documented here.

## Requirements
- `docker`
- `RabbitMQ` (will be moving to supporting RabbitMQ on Docker shortly)

### What does this project do?
 * Using the modules created in [here]('https://gitlab.scss.tcd.ie/panthb/Dublin-Transport_RPP'), a data pipeline is established

#### RabbitMQ specifics
- `docker-compose up`
- `docker build -t pipeline .`

#### Run the project
 * ```python main.py --flag=bus --host=localhost --start_index=0 --end_index=2```

## Repo update
- This repo will undergo active maintenance for the next few months. Will be using RabbitMQ with Spark for stream processing on the consumer side (MLlib)
