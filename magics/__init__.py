from .main import *

ip = get_ipython()
ip.register_magics(CustomMagics)