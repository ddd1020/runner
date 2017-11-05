from __future__ import absolute_import, unicode_literals
from celery import shared_task

import logging
log = logging.getLogger(__name__)

import runner.parsing as p

def validate_task_input(patient_files):
    """Validates task patient files before actually starting the task
    :param input_data: contains data to be used in model training
    return bool
    """
    #
    # ... perform some data validation before starting running models here ...
    #

    return True

@shared_task(bind=True)
def process_data_task(self, patient_files):
    """Sample processing task to demonstrate parallelism when processing batches of data.
    All tasks can run in parallel

    :param input_data: data to train on
    """
    # extract task id from celery
    task_id = 0  # defaults to zero if ran outside of celery
    if self and self.request and self.request.id:
        task_id = self.request.id

    # validate task input and return error if invalid
    if validate_task_input(patient_files):
        log.info('Starting task %s' % task_id)

        #
        # NOTE: at this point we would download 'patient_files' from some source (ex: AWS bucket)
        # for this demo we will assume that patient_files were successfully downloaded
        #

        # parse and load all patient data
        patient_data = []
        for dicom_file, contour_file in patient_files: # each patient has a list of paired dicom-contour files
            logging.debug('Processing file pair: [%s] and [%s]' % (dicom_file, contour_file))
            cdata = p.parse_contour_file(contour_file)
            ddata, width, height = p.parse_dicom_file(dicom_file)
            if not ddata or not width or not height:
              logging.error('Failed to load dicom file %s' % dicom_file)
            mask = p.poly_to_mask(cdata, width, height)
            patient_data.append({
                'contour': cdata,
                'pixel_array': ddata,
                'mask': mask
            })

        #
        # NOTE: at this point patient data has been successfully loaded,
        # ... now proceed with training ...
        log.debug(patient_data)
        log.info('Processed file pairs %s' % len(patient_data))
        log.info('Finished task %s' % task_id)
