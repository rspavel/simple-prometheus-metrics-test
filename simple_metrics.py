from prometheus_client import start_http_server, Counter
import random
import time

# Heavily based on https://prometheus.github.io/client_python/getting-started/three-step-demo/

if __name__ == '__main__':
    start_http_server(8000)
    cnt = Counter('simple_count', 'A Mostly Pointless Metric')
    while True:
        time.sleep(random.random())
        print('Writing Metric')
        cnt.inc(1.0)


