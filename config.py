# celery
BROKER_URL='amqp://myuser:mypassword@localhost:5672/myvhost'
BROKER_POOL_LIMIT = 10
BROKER_HEARTBEAT = None  # We're using TCP keep-alive instead
BROKER_CONNECTION_TIMEOUT = 30  # May require a long timeout due to Linux DNS timeouts etc
CELERY_RESULT_BACKEND = None
#CELERY_SEND_EVENTS = False  # Will not create celeryev.* queues
#CELERY_EVENT_QUEUE_EXPIRES = 60  # Will delete all celeryev. queues without consumers after 1 minute.
CELERY_IMPORTS = ('runner.tasks',)
