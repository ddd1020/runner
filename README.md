## Runner
A Celery wrapped app that loads dicom-contour data and readies it for processing.

### Installing dependencies:
- local RabbitMQ:
`http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html#broker-rabbitmq`

- `pip install requirements.txt`

- HACK: unpack zip file into 'final_data' (normally we would pull data from AWS bucket, but for this demo we're just doing filesystem)

- HACK: install this app into 'dist-packages'

in this demo I will omit turning this repo into a PIP installable app. Since celery tasks must be shared between both `runner` and `data-pipeline` projects, its best to install this app into `dist-packages`

ex: after cloning this repo run `sudo ln -s runner /usr/local/lib/python2.7/dist-packages/runner` (Note: adjust for your Virtualenv if needed)


### Running task-runner:
`celery worker --app=runner -l debug`
