import ctypes
dll = ctypes.cdll.LoadLibrary('./libthosttraderapi_se.so')
info = (ctypes.c_char * 344)()
length = ctypes.c_int()
print(dll._Z21CTP_GetRealSystemInfoPcRi(info, ctypes.byref(length)))
print(info.value)
