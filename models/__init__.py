#!/usr/bin/python3

"""Instantiation of our models directory including creating a unique
FileStorage instance for the application"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
