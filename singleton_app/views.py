from django.shortcuts import render
import threading

# Create your views here.
class FileBasedConfigurationManager:
    pass

class FileBasedConfigurationManagerImpl(FileBasedConfigurationManager):
    _instance = None
    _lock = threading.Lock()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance

    @classmethod
    def reset_instance(cls):
        cls._instance = None

    def __init__(self):
        super().__init__()

    

