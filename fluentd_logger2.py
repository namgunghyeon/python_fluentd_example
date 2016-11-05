import logging.config
import yaml

with open('logging.yaml') as fd:
    conf = yaml.load(fd)

logging.config.dictConfig(conf['logging'])

if __name__ == '__main__':
    logger = logging.getLogger('fluent.test')
    logger.info({
        'from': 'userA',
        'to': 'userB'
    })
