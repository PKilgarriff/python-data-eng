from ui.interface import Interface, ConsoleIO
from storage.csv_storage import MusicCSVStorage
import subprocess

interface = Interface(ConsoleIO(), MusicCSVStorage, subprocess)
interface.run()
