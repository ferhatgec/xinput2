import xinput2
import ctypes

xlib = ctypes.CDLL('libX11.so.6')

XSync = xlib.XSync
XSync.restype = ctypes.c_int
XSync.argtypes = [ctypes.POINTER(xinput2.Display),
                  ctypes.c_bool]

XNextEvent = xlib.XNextEvent
XNextEvent.restype = ctypes.c_int
XNextEvent.argtypes = [ctypes.POINTER(xinput2.Display),
                        ]

XOpenDisplay = xlib.XOpenDisplay
XOpenDisplay.restype = ctypes.POINTER(xinput2.Display)
XOpenDisplay.argtypes = [ctypes.POINTER(ctypes.c_char)]

XDefaultRootWindow = xlib.XDefaultRootWindow
XDefaultRootWindow.restype = ctypes.c_ulong
XDefaultRootWindow.argtypes = [ctypes.POINTER(xinput2.Display)]

mask = xinput2.XIEventMask()
dp = XOpenDisplay(None)
wnd = XDefaultRootWindow(dp)
mask.deviceid = xinput2.XIAllMasterDevices
mask.mask_len = xinput2.XIMaskLen(xinput2.XI_LASTEVENT)

_mask = (ctypes.c_byte * mask.mask_len)()

xinput2.XISetMask(_mask, xinput2.XI_RawKeyPress)
xinput2.XISetMask(_mask, xinput2.XI_RawKeyRelease)

mask.mask = ctypes.cast(ctypes.pointer(mask), ctypes.POINTER(ctypes.c_char))

xinput2.XISelectEvents(dp, wnd, mask, 1)