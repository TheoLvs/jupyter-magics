from IPython.core import magic_arguments
from IPython.core.magic import line_magic, cell_magic, line_cell_magic, Magics, magics_class

import winsound
import os


@magics_class
class CustomMagics(Magics):
    
    @line_magic
    def alarm(self,line=""):
        file = os.path.join(os.path.dirname(__file__),"static/alarm.wav")
        print(f"... Launching alarm at {file}")
        winsound.PlaySound(file, winsound.SND_FILENAME)


ip = get_ipython()
ip.register_magics(CustomMagics)


# def load_ipython_extension(ipython):
#     ipython.register_magics(CustomMagics)