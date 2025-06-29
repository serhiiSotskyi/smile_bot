import os

# How many messages to buffer before summarizing
MESSAGE_BUFFER_SIZE = int(os.getenv("MESSAGE_BUFFER_SIZE", "10"))
