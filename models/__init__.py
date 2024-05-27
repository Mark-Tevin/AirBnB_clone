#!/usr/bin/python3
"""
Script to create and reload a FileStorage instance
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
