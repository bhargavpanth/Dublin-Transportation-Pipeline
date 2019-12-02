## Dublin Bus Data Pipeline - Producer

## UPDATE
This repo is under active maintenance. Updates will be documented here.

## Requirements
- `docker`
- `RabbitMQ` (will be moving to supporting RabbitMQ on Docker shortly)

### What does this project do?
 * Using the modules created in [here]('https://gitlab.scss.tcd.ie/panthb/Dublin-Transport_RPP'), a data pipeline is established

#### RabbitMQ specifics

For Mac users
- `docker-compose up`

For Ubuntu Users
 * ```sudo rabbitmq-server start```
 * [RabbitMQ dashboard access]('https://developers.coveo.com/display/public/SitecoreV3/Accessing+the+RabbitMQ+Management+Console;jsessionid=548855A4C0EC0A72DA10CA8E400B124F')
 * Pre-req [here]('https://www.rabbitmq.com/management.html')

#### RabbitMQ Docker
 * Image available [here]('https://docs.docker.com/samples/library/rabbitmq/')

#### Run the project
 * ```python main.py --flag=bus --host=localhost --start_index=0 --end_index=2```

#### Remote instance
 * ```---host=mongodb://IP_ADD:27017/```

## Repo update (To-do)
- RabbitMQ is probably not the best solution for streaming high volume data (potentially data from Dublin Bus and Dublin Bikes in the interval of few seconds). Considering moving to using Kafka and PySpark.
- This repo will undergo active maintenance for the next few months. Will be replacing RabbitMQ with Apache Kafka and Spark for stream processing (MLlib)
