from os import getcwdu

__version__ = '0.1.0'

# The directory where the application was called
working_dir = getcwdu()

from config import Config
config = Config()
