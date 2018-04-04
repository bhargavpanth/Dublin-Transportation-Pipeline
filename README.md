## Dublin Bus Data Pipeline - Producer

### What does this project do?

 * Using the modules created in [here]('https://gitlab.scss.tcd.ie/panthb/Dublin-Transport_RPP'), the project establishes a pipeline to push messages into a queue (RabbitMQ)

#### RabbitMQ specifics
 * ```sudo rabbitmq-server start```
 * [RabbitMQ dashboard access]('https://developers.coveo.com/display/public/SitecoreV3/Accessing+the+RabbitMQ+Management+Console;jsessionid=548855A4C0EC0A72DA10CA8E400B124F')
 * Pre-req [here]('https://www.rabbitmq.com/management.html')

#### RabbitMQ Docker
 * Image available [here]('https://docs.docker.com/samples/library/rabbitmq/')

#### Run the project
 * ```python main.py --flag=bus --host=localhost --start_index=0 --end_index=2```

#### Remote instance
 * ```---host=mongodb://IP_ADD:27017/```