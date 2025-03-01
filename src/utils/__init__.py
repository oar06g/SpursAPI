from modules.pydllmanager import LoaderLibrary
import ctypes

utiles_loader = LoaderLibrary("bin/utiles.dll")
utiles_loader.load()

@utiles_loader.include()
def GetSerialNumber() -> ctypes.c_char_p: ...
def GetSerialNumberUse():
  get_s = GetSerialNumber()
  decoded_serial = ctypes.cast(get_s, ctypes.c_char_p).value
  return decoded_serial.decode("utf-8") if decoded_serial else "Decoding Failed"