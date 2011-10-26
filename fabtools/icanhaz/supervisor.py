"""
Idempotent API for managing supervisor processes
"""
from fabtools.icanhaz import deb
from fabtools.supervisor import *


def process(name, options=None):
    """
    I can haz supervisor process
    """
    deb.package('supervisor')
    add_process(name, options)
    reload_config()
    if process_status(name) == 'STOPPED':
        start_process(name)
