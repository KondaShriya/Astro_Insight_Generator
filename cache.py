import time
from threading import Lock

class SimpleTTLCache:
    def __init__(self, ttl_seconds: int = 3600):
        self.ttl = ttl_seconds
        self.store = {}
        self.lock = Lock()

    def get(self, key):
        with self.lock:
            item = self.store.get(key)
            if not item:
                return None
            value, ts = item
            if time.time() - ts > self.ttl:
                del self.store[key]
                return None
            return value

    def set(self, key, value):
        with self.lock:
            self.store[key] = (value, time.time())
