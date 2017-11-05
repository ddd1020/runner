from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

# initiate celery app
app = Celery('runner',
            broker='amqp://myuser:mypassword@localhost:5672/myvhost', # default
            include=['runner.tasks'] # default
            )

# configure celery app (so it finds task-runner tasks)
os.environ.setdefault('CELERY_CONFIG_MODULE', 'runner.config')
app.config_from_envvar('CELERY_CONFIG_MODULE')

# print debug info. TODO: remove in prod
print 'Worker config:'
print app.conf.humanize(with_defaults=False, censored=False)

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
