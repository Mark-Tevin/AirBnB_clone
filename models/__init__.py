#!/usr/bin/python3
""" data handling
This module initializes an object
of class FileStorage
"""

from models.engine.file_storage import FileStorage
""" successful import """

storage = FileStorage()
storage.reload()
