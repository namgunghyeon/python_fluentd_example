import time
import threading
import logging
from fluent import handler

customFormat = {
  'host': '%(hostname)s',
  'where': '%(module)s.%(funcName)s',
  'type': '%(levelname)s',
  'stack_trace': '%(exc_text)s'
}

class fluentdLogging(object):
    def __init__(self, tag, ip, port, loggerName="fluent.test"):
        logging.basicConfig(level=logging.INFO)
        self._logger = logging.getLogger(loggerName)
        self._loggerHandler = handler.FluentHandler(tag, host=ip, port=port)
        self._formatter = handler.FluentRecordFormatter(customFormat)
        self._loggerHandler.setFormatter(self._formatter)

        self._logger.addHandler(self._loggerHandler)

    def __getattr__(cls, key):
        if key == 'logger':
            return cls._logger

if __name__ == '__main__':
    logger = fluentdLogging('app', '192.168.56.116', 24224).logger

    logger.info({
        'from': 'userA',
        'to': 'userB'
    })
