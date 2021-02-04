import time
import uuid

def format(item):
    item.date = int(time.time())
    item.uuid = str(uuid.uuid4())
    