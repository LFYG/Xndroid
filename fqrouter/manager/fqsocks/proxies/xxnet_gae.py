from http_connect import HttpConnectProxy

class XXnetGAE(HttpConnectProxy):
    def __init__(self, priority=255):
        HttpConnectProxy.__init__(self, '127.0.0.1', 8087, priority=priority)

    def __repr__(self):
        return 'XXnetGAE[%s:%s %0.2f]' % (self.proxy_host, self.proxy_port, self.latency)
