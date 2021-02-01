import time
import uuid

def format(item):
    item.date = time.time()
    item.uuid = str(uuid.uuid4())
    
#reject duplicates