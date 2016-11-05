import time
import threading
import logging
from fluent import sender

class Sender(threading.Thread):
    def __init__(self, tag, ip, port):
        threading.Thread.__init__(self)
        self._ip = ip
        self._port = port
        self._tag = tag
        self.daemon = True

    def run(self):
        fluentdLogger = sender.FluentSender(self._tag, host=self._ip, port=self._port)

        while True:
            message = {'from': 'userA', 'to': 'userB'}
            fluentdLogger.emit('follow', message)
            print "Send Message %s message Error %s" %(message, fluentdLogger.last_error)
            time.sleep(1)

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )

    threads = [
        Sender('app', '192.168.56.116', 24224)
    ]
    for t in threads:
        t.start()

    time.sleep(10)
