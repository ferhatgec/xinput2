# MIT License
#
# Copyright (c) 2023 Ferhat Geçdoğan All Rights Reserved.
# Distributed under the terms of the MIT License.
#
#

import ctypes

libXInput = ctypes.CDLL('libXi.so.6')

XIPropertyDeleted = 0
XIPropertyCreated = 1
XIPropertyModified = 2

XIPropModeReplace = 0
XIPropModePrepend = 1
XIPropModeAppend = 2

XIAnyPropertyType = 0

XINotifyNormal = 0
XINotifyGrab = 1
XINotifyUngrab = 2
XINotifyWhileGrabbed = 3
XINotifyPassiveGrab = 4
XINotifyPassiveUngrab = 5

XINotifyAncestor = 0
XINotifyVirtual = 1
XINotifyInferior = 2
XINotifyNonlinear = 3
XINotifyNonlinearVirtual = 4
XINotifyPointer = 5
XINotifyPointerRoot = 6
XINotifyDetailNone = 7

XIGrabModeSync = 0
XIGrabModeAsync = 1
XIGrabModeTouch = 2

XIGrabSuccess = 0
XIAlreadyGrabbed = 1
XIGrabInvalidTime = 2
XIGrabNotViewable = 3
XIGrabFrozen = 4

XIOwnerEvents = True
XINoOwnerEvents = False

XIGrabtypeButton = 0
XIGrabtypeKeycode = 1
XIGrabtypeEnter = 2
XIGrabtypeFocusIn = 3
XIGrabtypeTouchBegin = 4
XIGrabtypeGesturePinchBegin = 5
XIGrabtypeGestureSwipeBegin = 6

XIAnyModifier = (1 << 31)
XIAnyButton = 0
XIAnyKeycode = 0

XIAsyncDevice = 0
XISyncDevice = 1
XIReplayDevice = 2
XIAsyncPairedDevice = 3
XIAsyncPair = 4
XISyncPair = 5
XIAcceptTouch = 6
XIRejectTouch = 7

XISlaveSwitch = 1
XIDeviceChange = 2

XIMasterAdded = (1 << 0)
XIMasterRemoved = (1 << 1)
XISlaveAdded = (1 << 2)
XISlaveRemoved = (1 << 3)
XISlaveAttached = (1 << 4)
XISlaveDetached = (1 << 5)
XIDeviceEnabled = (1 << 6)
XIDeviceDisabled = (1 << 7)

XIAddMaster = 1
XIRemoveMaster = 2
XIAttachSlave = 3
XIDetachSlave = 4

XIAttachToMaster = 1
XIFloating = 2

XIModeRelative = 0
XIModeAbsolute = 1

XIMasterPointer = 1
XIMasterKeyboard = 2
XISlavePointer = 3
XISlaveKeyboard = 4
XIFloatingSlave = 5

XIKeyClass = 0
XIButtonClass = 1
XIValuatorClass = 2
XIScrollClass = 3
XITouchClass = 8
XIGestureClass = 9

XIScrollTypeVertical = 1
XIScrollTypeHorizontal = 2

XIScrollFlagNoEmulation = (1 << 0)
XIScrollFlagPreferred = (1 << 1)

XIKeyRepeat = (1 << 16)

XIPointerEmulated = (1 << 16)

XITouchPendingEnd = (1 << 16)
XITouchEmulatingPointer = (1 << 17)

XIBarrierPointerReleased = (1 << 0)
XIBarrierDeviceIsGrabbed = (1 << 1)

XIGesturePinchEventCancelled = (1 << 0)

XIGestureSwipeEventCancelled = (1 << 0)

XIDirectTouch = 1
XIDependentTouch = 2

XIAllDevices = 0
XIAllMasterDevices = 1

XI_DeviceChanged = 1
XI_KeyPress = 2
XI_KeyRelease = 3
XI_ButtonPress = 4
XI_ButtonRelease = 5
XI_Motion = 6
XI_Enter = 7
XI_Leave = 8
XI_FocusIn = 9
XI_FocusOut = 10
XI_HierarchyChanged = 11
XI_PropertyEvent = 12
XI_RawKeyPress = 13
XI_RawKeyRelease = 14
XI_RawButtonPress = 15
XI_RawButtonRelease = 16
XI_RawMotion = 17
XI_TouchBegin = 18
XI_TouchUpdate = 19
XI_TouchEnd = 20
XI_TouchOwnership = 21
XI_RawTouchBegin = 22
XI_RawTouchUpdate = 23
XI_RawTouchEnd = 24
XI_BarrierHit = 25
XI_BarrierLeave = 26
XI_GesturePinchBegin = 27
XI_GesturePinchUpdate = 28
XI_GesturePinchEnd = 29
XI_GestureSwipeBegin = 30
XI_GestureSwipeUpdate = 31
XI_GestureSwipeEnd = 32
XI_LASTEVENT = XI_GestureSwipeEnd

XI_DeviceChangedMask = (1 << XI_DeviceChanged)
XI_KeyPressMask = (1 << XI_KeyPress)
XI_KeyReleaseMask = (1 << XI_KeyRelease)
XI_ButtonPressMask = (1 << XI_ButtonPress)
XI_ButtonReleaseMask = (1 << XI_ButtonRelease)
XI_MotionMask = (1 << XI_Motion)
XI_EnterMask = (1 << XI_Enter)
XI_LeaveMask = (1 << XI_Leave)
XI_FocusInMask = (1 << XI_FocusIn)
XI_FocusOutMask = (1 << XI_FocusOut)
XI_HierarchyChangedMask = (1 << XI_HierarchyChanged)
XI_PropertyEventMask = (1 << XI_PropertyEvent)
XI_RawKeyPressMask = (1 << XI_RawKeyPress)
XI_RawKeyReleaseMask = (1 << XI_RawKeyRelease)
XI_RawButtonPressMask = (1 << XI_RawButtonPress)
XI_RawButtonReleaseMask = (1 << XI_RawButtonRelease)
XI_RawMotionMask = (1 << XI_RawMotion)
XI_TouchBeginMask = (1 << XI_TouchBegin)
XI_TouchEndMask = (1 << XI_TouchEnd)
XI_TouchOwnershipChangedMask = (1 << XI_TouchOwnership)
XI_TouchUpdateMask = (1 << XI_TouchUpdate)
XI_RawTouchBeginMask = (1 << XI_RawTouchBegin)
XI_RawTouchEndMask = (1 << XI_RawTouchEnd)
XI_RawTouchUpdateMask = (1 << XI_RawTouchUpdate)
XI_BarrierHitMask = (1 << XI_BarrierHit)
XI_BarrierLeaveMask = (1 << XI_BarrierLeave)

def XIMaskLen(event: int) -> int:
    return (event >> 3) + 1

def XISetMask(ptr, event):
    ptr[(event)>>3] |= (1 << ((event) & 7))

def XIClearMask(ptr, event):
    ptr[event >> 3] &= ~(1 << (event & 7))

def XIMaskIsSet(ptr, event):
    ptr[event >> 3] & (1 << ((event & 7)))

class XIAddMasterInfo(ctypes.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('name', ctypes.POINTER(ctypes.c_char)),
                ('send_core', ctypes.c_bool),
                ('enable', ctypes.c_bool)]

class XIRemoveMasterInfo(ctypes.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('deviceid', ctypes.c_int),
                ('return_mode', ctypes.c_int),
                ('return_pointer', ctypes.c_int),
                ('return_keyboard', ctypes.c_int)]

class XIAttachSlaveInfo(ctypes.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('deviceid', ctypes.c_int),
                ('new_master', ctypes.c_int)]

class XIDetachSlaveInfo(ctypes.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('deviceid', ctypes.c_int)]

class XIAnyHierarchyChangeInfo(ctypes.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('add', XIAddMasterInfo),
                ('remove', XIRemoveMasterInfo),
                ('attach', XIAttachSlaveInfo),
                ('detach', XIDetachSlaveInfo)]

class XIModifierState(ctypes.Structure):
    _fields_ = [('base', ctypes.c_int), 
                ('latched', ctypes.c_int),
                ('locked', ctypes.c_int),
                ('effective', ctypes.c_int)]

XIGroupState = XIModifierState

class XIButtonState(ctypes.Structure):
    _fields_ = [('mask_len', ctypes.c_int),
                ('mask', ctypes.POINTER(ctypes.c_char))]

class XIValuatorState(ctypes.Structure):
    _fields_ = [('mask_len', ctypes.c_int),
                ('mask', ctypes.POINTER(ctypes.c_char)),
                ('values', ctypes.POINTER(ctypes.c_double))]

class XIEventMask(ctypes.Structure):
    _fields_ = [('deviceid', ctypes.c_int),
                ('mask_len', ctypes.c_int),
                ('mask', ctypes.POINTER(ctypes.c_char))]

class XIAnyClassInfo(ctypes.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('sourceid', ctypes.c_int)]

class XIButtonClassInfo(ctypes.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('sourceid', ctypes.c_int),
                ('num_buttons', ctypes.c_int),
                ('labels', ctypes.POINTER(ctypes.c_ulong)),
                ('state', XIButtonState)]

class XIKeyClassInfo(ctypes.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('sourceid', ctypes.c_int),
                ('num_keycodes', ctypes.c_int),
                ('keycodes', ctypes.POINTER(ctypes.c_int))]

class XIValuatorClassInfo(ctypes.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('sourceid', ctypes.c_int),
                ('number', ctypes.c_int),
                ('label', ctypes.c_ulong),
                ('min', ctypes.c_double),
                ('max', ctypes.c_double),
                ('value', ctypes.c_double),
                ('resolution', ctypes.c_int),
                ('mode', ctypes.c_int)]

class XIScrollClassInfo(ctypes.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('sourceid', ctypes.c_int),
                ('number', ctypes.c_int),
                ('scroll_type', ctypes.c_int),
                ('increment', ctypes.c_double),
                ('flags', ctypes.c_int)]

class XITouchClassInfo(ctypes.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('sourceid', ctypes.c_int),
                ('mode', ctypes.c_int),
                ('num_touches', ctypes.c_int)]

class XIGestureClassInfo(ctypes.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('sourceid', ctypes.c_int),
                ('num_touches', ctypes.c_int)]

class XIDeviceInfo(ctypes.Structure):
    _fields_ = [('deviceid', ctypes.c_int),
                ('name', ctypes.POINTER(ctypes.c_char)),
                ('use', ctypes.c_int),
                ('attachment', ctypes.c_int),
                ('enabled', ctypes.c_bool),
                ('num_classes', ctypes.c_int),
                ('classes', ctypes.POINTER(ctypes.POINTER(XIAnyClassInfo)))]

class XIGrabModifiers(ctypes.Structure):
    _fields_ = [('modifiers', ctypes.c_int),
                ('status', ctypes.c_int)]

class XIBarrierReleasePointerInfo(ctypes.Structure):
    _fields_ = [('deviceid', ctypes.c_int),
                ('barrier', ctypes.c_ulong),
                ('eventid', ctypes.c_uint)]

class XPrivate(ctypes.Structure):
    pass

class XExtData(ctypes.Structure):
    pass

class XrmHashBucketRec(ctypes.Structure):
    pass

XExtData._fields_ = [('number', ctypes.c_int),
                     ('next', ctypes.POINTER(XExtData)),
                     ('free_private', ctypes.c_void_p),
                     ('private_data', ctypes.POINTER(ctypes.c_char))]

class ScreenFormat(ctypes.Structure):
    _fields_ = [('ext_data', ctypes.POINTER(XExtData)),
                ('depth', ctypes.c_int),
                ('bits_per_pixel', ctypes.c_int),
                ('scanline_pad', ctypes.c_int)]

class Display(ctypes.Structure):
    pass

class XGC(ctypes.Structure):
    _fields_ = [('ext_data', ctypes.POINTER(XExtData)),
                ('gid', ctypes.c_int)]

GC = ctypes.POINTER(XGC)

class Visual(ctypes.Structure):
    _fields_ = [('ext_data', ctypes.POINTER(XExtData)),
                ('visualid', ctypes.c_ulong),
                ('class', ctypes.c_int),
                ('red_mask', ctypes.c_ulong),
                ('green_mask', ctypes.c_ulong),
                ('blue_mask', ctypes.c_ulong),
                ('bits_per_rgb', ctypes.c_int),
                ('map_entries', ctypes.c_int)]


class Depth(ctypes.Structure):
    _fields_ = [('depth', ctypes.c_int),
                ('nvisuals', ctypes.c_int),
                ('visuals', ctypes.POINTER(Visual))]

class Screen(ctypes.Structure):
    _fields_ = [('ext_data', ctypes.POINTER(XExtData)),
                ('display', ctypes.POINTER(Display)),
                ('root', ctypes.c_ulong),
                ('width', ctypes.c_int),
                ('height', ctypes.c_int),
                ('mwidth', ctypes.c_int),
                ('mheight', ctypes.c_int),
                ('ndepths', ctypes.c_int),
                ('depths', ctypes.POINTER(Depth)),
                ('root_depth', ctypes.c_int),
                ('root_visual', ctypes.POINTER(Visual)),
                ('default_gc', GC),
                ('cmap', ctypes.c_ulong),
                ('white_pixel', ctypes.c_ulong),
                ('black_pixel', ctypes.c_ulong),
                ('max_maps', ctypes.c_int),
                ('min_maps', ctypes.c_int),
                ('backing_store', ctypes.c_int),
                ('save_unders', ctypes.c_bool),
                ('root_input_mask', ctypes.c_long)]


Display._fields_ = [('ext_data', ctypes.POINTER(XExtData)),
                ('private1', ctypes.POINTER(XPrivate)),
                ('fd', ctypes.c_int),
                ('private2', ctypes.c_int),
                ('proto_major_version', ctypes.c_int),
                ('proto_minor_version', ctypes.c_int),
                ('vendor', ctypes.POINTER(ctypes.c_char)),
                ('private3', ctypes.c_ulong),
                ('private4', ctypes.c_ulong),
                ('private5', ctypes.c_ulong),
                ('private6', ctypes.c_int),
                ('resource_alloc', ctypes.c_void_p),
                ('byte_order', ctypes.c_int),
                ('bitmap_unit', ctypes.c_int),
                ('bitmap_pad', ctypes.c_int),
                ('bitmap_bit_order', ctypes.c_int),
                ('nformats', ctypes.c_int),
                ('pixmap_format', ctypes.POINTER(ScreenFormat)),
                ('private8', ctypes.c_int),
                ('release', ctypes.c_int),
                ('private9', ctypes.POINTER(XPrivate)),
                ('private10', ctypes.POINTER(XPrivate)),
                ('qlen', ctypes.c_int),
                ('last_request_read', ctypes.c_ulong),
                ('request', ctypes.c_ulong),
                ('private11', ctypes.POINTER(ctypes.c_char)),
                ('private12', ctypes.POINTER(ctypes.c_char)),
                ('private13', ctypes.POINTER(ctypes.c_char)),
                ('private14', ctypes.POINTER(ctypes.c_char)),
                ('max_request_size', ctypes.c_uint),
                ('db', ctypes.POINTER(XrmHashBucketRec)),
                ('private15', ctypes.c_void_p),
                ('display_name', ctypes.POINTER(ctypes.c_char)),
                ('default_screen', ctypes.c_int),
                ('nscreens', ctypes.c_int),
                ('screens', ctypes.POINTER(Screen)),
                ('motion_buffer', ctypes.c_ulong),
                ('private16', ctypes.c_ulong),
                ('min_keycode', ctypes.c_int),
                ('max_keycode', ctypes.c_int),
                ('private17', ctypes.POINTER(ctypes.c_char)),
                ('private18', ctypes.POINTER(ctypes.c_char)),
                ('private19', ctypes.c_int),
                ('xdefaults', ctypes.POINTER(ctypes.c_char))]


class XIEvent(ctypes.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('serial', ctypes.c_ulong),
                ('send_event', ctypes.c_bool),
                ('display', ctypes.POINTER(Display)),
                ('extension', ctypes.c_int),
                ('evtype', ctypes.c_int),
                ('time', ctypes.c_ulong)]

class XIHierarchyInfo(ctypes.Structure):
    _fields_ = [('deviceid', ctypes.c_int),
                ('attachment', ctypes.c_int),
                ('use', ctypes.c_int),
                ('enabled', ctypes.c_bool),
                ('flags', ctypes.c_int)]

class XIHierarchyEvent(ctypes.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('serial', ctypes.c_ulong),
                ('send_event', ctypes.c_bool),
                ('display', ctypes.POINTER(Display)),
                ('extension', ctypes.c_int),
                ('evtype', ctypes.c_int),
                ('time', ctypes.c_ulong),
                ('flags', ctypes.c_int),
                ('num_info', ctypes.c_int),
                ('info', ctypes.POINTER(XIHierarchyInfo))]

class XIDeviceChangedEvent(ctypes.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('serial', ctypes.c_ulong),
                ('send_event', ctypes.c_bool),
                ('display', ctypes.POINTER(Display)),
                ('extension', ctypes.c_int),
                ('evtype', ctypes.c_int),
                ('time', ctypes.c_ulong),
                ('deviceid', ctypes.c_int),
                ('sourceid', ctypes.c_int),
                ('reason', ctypes.c_int),
                ('num_classes', ctypes.c_int),
                ('classes', ctypes.POINTER(ctypes.POINTER(XIAnyClassInfo)))]


class XIDeviceEvent(ctypes.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('serial', ctypes.c_ulong),
                ('send_event', ctypes.c_bool),
                ('display', ctypes.POINTER(Display)),
                ('extension', ctypes.c_int),
                ('evtype', ctypes.c_int),
                ('time', ctypes.c_ulong),
                ('deviceid', ctypes.c_int),
                ('sourceid', ctypes.c_int),
                ('detail', ctypes.c_int),
                ('root', ctypes.c_ulong),
                ('event', ctypes.c_ulong),
                ('child', ctypes.c_ulong),
                ('root_x', ctypes.c_double),
                ('root_y', ctypes.c_double),
                ('event_x', ctypes.c_double),
                ('event_y', ctypes.c_double),
                ('flags', ctypes.c_int),
                ('buttons', XIButtonState),
                ('valuators', XIValuatorState),
                ('mods', XIModifierState),
                ('group', XIGroupState)]

class XIRawEvent(ctypes.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('serial', ctypes.c_ulong),
                ('send_event', ctypes.c_bool),
                ('display', ctypes.POINTER(Display)),
                ('extension', ctypes.c_int),
                ('evtype', ctypes.c_int),
                ('time', ctypes.c_ulong),
                ('deviceid', ctypes.c_int),
                ('sourceid', ctypes.c_int),
                ('detail', ctypes.c_int),
                ('flags', ctypes.c_int),
                ('valuators', XIValuatorState),
                ('raw_values', ctypes.POINTER(ctypes.c_double))]

class XIEnterEvent(ctypes.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('serial', ctypes.c_ulong),
                ('send_event', ctypes.c_bool),
                ('display', ctypes.POINTER(Display)),
                ('extension', ctypes.c_int),
                ('evtype', ctypes.c_int),
                ('time', ctypes.c_ulong),
                ('deviceid', ctypes.c_int),
                ('sourceid', ctypes.c_int),
                ('detail', ctypes.c_int),
                ('root', ctypes.c_ulong),
                ('event', ctypes.c_ulong),
                ('child', ctypes.c_ulong),
                ('root_x', ctypes.c_double),
                ('root_y', ctypes.c_double),
                ('event_x', ctypes.c_double),
                ('event_y', ctypes.c_double),
                ('mode', ctypes.c_int),
                ('focus', ctypes.c_bool),
                ('same_screen', ctypes.c_bool),
                ('buttons', XIButtonState),
                ('mods', XIModifierState),
                ('group', XIGroupState)]

XILeaveEvent = XIEnterEvent
XIFocusInEvent = XIEnterEvent
XIFocusOutEvent = XIEnterEvent

class XIPropertyEvent(ctypes.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('serial', ctypes.c_ulong),
                ('send_event', ctypes.c_bool),
                ('display', ctypes.POINTER(Display)),
                ('extension', ctypes.c_int),
                ('evtype', ctypes.c_int),
                ('time', ctypes.c_ulong),
                ('deviceid', ctypes.c_int),
                ('property', ctypes.c_ulong),
                ('what', ctypes.c_int)]

class XITouchOwnershipEvent(ctypes.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('serial', ctypes.c_ulong),
                ('send_event', ctypes.c_bool),
                ('display', ctypes.POINTER(Display)),
                ('extension', ctypes.c_int),
                ('evtype', ctypes.c_int),
                ('time', ctypes.c_ulong),
                ('deviceid', ctypes.c_int),
                ('sourceid', ctypes.c_int),
                ('touchid', ctypes.c_uint),
                ('root', ctypes.c_ulong),
                ('event', ctypes.c_ulong),
                ('child', ctypes.c_ulong),
                ('flags', ctypes.c_int)]

class XIBarrierEvent(ctypes.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('serial', ctypes.c_ulong),
                ('send_event', ctypes.c_bool),
                ('display', ctypes.POINTER(Display)),
                ('extension', ctypes.c_int),
                ('evtype', ctypes.c_int),
                ('time', ctypes.c_ulong),
                ('deviceid', ctypes.c_int),
                ('sourceid', ctypes.c_int),
                ('event', ctypes.c_ulong),
                ('root', ctypes.c_ulong),
                ('root_x', ctypes.c_double),
                ('root_y', ctypes.c_double),
                ('dx', ctypes.c_double),
                ('dy', ctypes.c_double),
                ('dtime', ctypes.c_int),
                ('flags', ctypes.c_int),
                ('barrier', ctypes.c_ulong),
                ('eventid', ctypes.c_uint)]

class XIGesturePinchEvent(ctypes.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('serial', ctypes.c_ulong),
                ('send_event', ctypes.c_bool),
                ('display', ctypes.POINTER(Display)),
                ('extension', ctypes.c_int),
                ('evtype', ctypes.c_int),
                ('time', ctypes.c_ulong),
                ('deviceid', ctypes.c_int),
                ('sourceid', ctypes.c_int),
                ('detail', ctypes.c_int),
                ('root', ctypes.c_ulong),
                ('event', ctypes.c_ulong),
                ('child', ctypes.c_ulong),
                ('root_x', ctypes.c_double),
                ('root_y', ctypes.c_double),
                ('event_x', ctypes.c_double),
                ('event_y', ctypes.c_double),
                ('delta_x', ctypes.c_double),
                ('delta_y', ctypes.c_double),
                ('delta_unaccel_x', ctypes.c_double),
                ('delta_unaccel_y', ctypes.c_double),
                ('scale', ctypes.c_double),
                ('delta_angle', ctypes.c_double),
                ('flags', ctypes.c_int),
                ('mods', XIModifierState),
                ('group', XIGroupState)]


class XIGestureSwipeEvent(ctypes.Structure):
    _fields_ = [('type', ctypes.c_int),
                ('serial', ctypes.c_ulong),
                ('send_event', ctypes.c_bool),
                ('display', ctypes.POINTER(Display)),
                ('extension', ctypes.c_int),
                ('evtype', ctypes.c_int),
                ('time', ctypes.c_ulong),
                ('deviceid', ctypes.c_int),
                ('sourceid', ctypes.c_int),
                ('detail', ctypes.c_int),
                ('root', ctypes.c_ulong),
                ('event', ctypes.c_ulong),
                ('child', ctypes.c_ulong),
                ('root_x', ctypes.c_double),
                ('root_y', ctypes.c_double),
                ('event_x', ctypes.c_double),
                ('event_y', ctypes.c_double),
                ('delta_x', ctypes.c_double),
                ('delta_y', ctypes.c_double),
                ('delta_unaccel_x', ctypes.c_double),
                ('delta_unaccel_y', ctypes.c_double),
                ('flags', ctypes.c_int),
                ('mods', XIModifierState),
                ('group', XIGroupState)]



XIQueryPointer = libXInput.XIQueryPointer
XIQueryPointer.restype = ctypes.c_bool
XIQueryPointer.argtypes = [ctypes.POINTER(Display), # display
                           ctypes.c_int, # deviceid
                           ctypes.c_ulong, # win
                           ctypes.POINTER(ctypes.c_ulong), # root
                           ctypes.POINTER(ctypes.c_ulong), # child
                           ctypes.POINTER(ctypes.c_double), # root_x
                           ctypes.POINTER(ctypes.c_double), # root_y
                           ctypes.POINTER(ctypes.c_double), # win_x
                           ctypes.POINTER(ctypes.c_double), # win_y
                           ctypes.POINTER(XIButtonState), # buttons
                           ctypes.POINTER(XIModifierState), # mods
                           ctypes.POINTER(XIGroupState)  # group
                           ]

XIWarpPointer = libXInput.XIWarpPointer
XIWarpPointer.restype = ctypes.c_bool
XIWarpPointer.argtypes = [ctypes.POINTER(Display), # display
                          ctypes.c_int, # deviceid
                          ctypes.c_ulong, # src_win
                          ctypes.c_ulong, # dst_win
                          ctypes.c_double, # src_x
                          ctypes.c_double, # src_y
                          ctypes.c_uint, # src_width
                          ctypes.c_uint, # src_height
                          ctypes.c_double, # dst_x
                          ctypes.c_double # dst_y
                          ]

XIDefineCursor = libXInput.XIDefineCursor
XIDefineCursor.restype = ctypes.c_int
XIDefineCursor.argtypes = [ctypes.POINTER(Display), # display
                           ctypes.c_int, # deviceid
                           ctypes.c_ulong, # win
                           ctypes.c_ulong, # cursor
                           ]

XIUndefineCursor = libXInput.XIUndefineCursor
XIUndefineCursor.restype = ctypes.c_int
XIUndefineCursor.argtypes = [ctypes.POINTER(Display), # display
                             ctypes.c_int, # deviceid 
                             ctypes.c_ulong # win
                             ]

XIChangeHierarchy = libXInput.XIChangeHierarchy
XIChangeHierarchy.restype = ctypes.c_int
XIChangeHierarchy.argtypes = [ctypes.POINTER(Display), # display
                              ctypes.POINTER(XIAnyHierarchyChangeInfo), # changes
                              ctypes.c_int # num_changes
                              ]

XISetClientPointer = libXInput.XISetClientPointer
XISetClientPointer.restype = ctypes.c_int
XISetClientPointer.argtypes = [ctypes.POINTER(Display), # display
                               ctypes.c_ulong, # win
                               ctypes.c_int # deviceid
                               ]

XIGetClientPointer = libXInput.XIGetClientPointer
XIGetClientPointer.restype = ctypes.c_bool
XIGetClientPointer.argtypes = [ctypes.POINTER(Display), # dpy
                               ctypes.c_ulong, # win
                               ctypes.POINTER(ctypes.c_int) # deviceid
                               ]

XISelectEvents = libXInput.XISelectEvents
XISelectEvents.restype = ctypes.c_int
XISelectEvents.argtypes = [ctypes.POINTER(Display), # dpy
                           ctypes.c_ulong, # win
                           ctypes.POINTER(XIEventMask), # masks
                           ctypes.c_int # num_masks
                           ]

XIGetSelectedEvents = libXInput.XIGetSelectedEvents
XIGetSelectedEvents.restype = ctypes.POINTER(XIEventMask)
XIGetSelectedEvents.argtypes = [ctypes.POINTER(Display), # dpy
                                ctypes.c_ulong, # win
                                ctypes.POINTER(ctypes.c_int) # num_masks_return
                                ]
XIQueryVersion = libXInput.XIQueryVersion
XIQueryVersion.restype = ctypes.c_int
XIQueryVersion.argtypes = [ctypes.POINTER(Display), # dpy
                           ctypes.POINTER(ctypes.c_int), # major_version_inout
                           ctypes.POINTER(ctypes.c_int) # minor_version_inout
                           ]

XIQueryDevice = libXInput.XIQueryDevice
XIQueryDevice.restype = ctypes.POINTER(XIDeviceInfo)
XIQueryDevice.argtypes = [ctypes.POINTER(Display), # dpy
                          ctypes.c_int, # deviceid
                          ctypes.POINTER(ctypes.c_int) # ndevices_return
                          ]

XISetFocus = libXInput.XISetFocus
XISetFocus.restype = ctypes.c_int
XISetFocus.argtypes = [ctypes.POINTER(Display), # dpy
                       ctypes.c_int, # deviceid
                       ctypes.c_ulong, # focus
                       ctypes.c_ulong # time
                       ]

XIGetFocus = libXInput.XIGetFocus
XIGetFocus.restype = ctypes.c_int
XIGetFocus.argtypes = [ctypes.POINTER(Display), # dpy
                       ctypes.c_int, # deviceid
                       ctypes.POINTER(ctypes.c_ulong) # focus_return
                       ]

XIGrabDevice = libXInput.XIGrabDevice
XIGrabDevice.restype = ctypes.c_int
XIGrabDevice.argtypes = [ctypes.POINTER(Display), # dpy
                         ctypes.c_int, # deviceid
                         ctypes.c_ulong, # grab_window
                         ctypes.c_ulong, # time
                         ctypes.c_ulong, # cursor
                         ctypes.c_int, # grab_mode
                         ctypes.c_int, # paired_device_mode
                         ctypes.c_bool, # owner_events
                         ctypes.POINTER(XIEventMask) # mask
                         ]

XIUngrabDevice = libXInput.XIUngrabDevice
XIUngrabDevice.restype = ctypes.c_int
XIUngrabDevice.argtypes = [ctypes.POINTER(Display), # dpy
                           ctypes.c_int, # deviceid
                           ctypes.c_ulong # time
                           ]

XIAllowEvents = libXInput.XIAllowEvents
XIAllowEvents.restype = ctypes.c_int
XIAllowEvents.argtypes = [ctypes.POINTER(Display), # display
                          ctypes.c_int, # deviceid
                          ctypes.c_int,  # event_mode
                          ctypes.c_ulong # time
                          ]

XIAllowTouchEvents = libXInput.XIAllowTouchEvents
XIAllowTouchEvents.restype = ctypes.c_int
XIAllowTouchEvents.argtypes = [ctypes.POINTER(Display), # display
                               ctypes.c_int, # deviceid
                               ctypes.c_uint, # touchid
                               ctypes.c_ulong, # grab_window
                               ctypes.c_int # event_mode
                               ]

XIGrabButton = libXInput.XIGrabButton
XIGrabButton.restype = ctypes.c_int
XIGrabButton.argtypes = [ctypes.POINTER(Display), # display
                         ctypes.c_int, # deviceid
                         ctypes.c_int, # button
                         ctypes.c_ulong, # grab_window
                         ctypes.c_ulong, # cursor
                         ctypes.c_int, # grab_mode
                         ctypes.c_int, # paired_device_mode
                         ctypes.c_int, # owner_event
                         ctypes.POINTER(XIEventMask), # mask
                         ctypes.c_int, # num_modifiers
                         ctypes.POINTER(XIGrabModifiers) # modifiers_inout
                         ]

XIGrabKeycode = libXInput.XIGrabKeycode
XIGrabKeycode.restype =  ctypes.c_int
XIGrabKeycode.argtypes = [ctypes.POINTER(Display), # display
                          ctypes.c_int, # deviceid
                          ctypes.c_int, # keycode
                          ctypes.c_ulong, # grab_window
                          ctypes.c_int, # grab_mode
                          ctypes.c_int, # paired_device_mode
                          ctypes.c_int, # owner_events
                          ctypes.POINTER(XIEventMask), # mask
                          ctypes.c_int, # num_modifiers
                          ctypes.POINTER(XIGrabModifiers) # modifiers_inout
                          ]

XIGrabEnter = libXInput.XIGrabEnter
XIGrabEnter.restype = ctypes.c_int
XIGrabEnter.argtypes = [ctypes.POINTER(Display), # display
                        ctypes.c_int, # deviceid
                        ctypes.c_ulong, # grab_window
                        ctypes.c_ulong, # cursor
                        ctypes.c_int, # grab_mode
                        ctypes.c_int, # paired_device_mode
                        ctypes.c_int, # owner_events
                        ctypes.POINTER(XIEventMask), # mask
                        ctypes.c_int, # num_modifiers
                        ctypes.POINTER(XIGrabModifiers) # modifiers_inout
                        ]

XIGrabFocusIn = libXInput.XIGrabFocusIn
XIGrabFocusIn.restype = ctypes.c_int
XIGrabFocusIn.argtypes = [ctypes.POINTER(Display), # display
                          ctypes.c_int, # deviceid
                          ctypes.c_ulong, # grab_window
                          ctypes.c_int, # grab_mode
                          ctypes.c_int, # paired_device_mode
                          ctypes.c_int, # owner_events
                          ctypes.POINTER(XIEventMask), # mask
                          ctypes.c_int, # num_modifiers
                          ctypes.POINTER(XIGrabModifiers) # modifiers_inout
                          ]

XIGrabTouchBegin = libXInput.XIGrabTouchBegin
XIGrabTouchBegin.restype = ctypes.c_int
XIGrabTouchBegin.argtypes = [ctypes.POINTER(Display), # display
                             ctypes.c_int, # deviceid
                             ctypes.c_ulong, # grab_window
                             ctypes.c_int, # owner_events
                             ctypes.POINTER(XIEventMask), # mask
                             ctypes.c_int, # num_modifiers
                             ctypes.POINTER(XIGrabModifiers) # modifiers_inout
                             ]

XIGrabPinchGestureBegin = libXInput.XIGrabPinchGestureBegin
XIGrabPinchGestureBegin.restype = ctypes.c_int
XIGrabPinchGestureBegin.argtypes = [ctypes.POINTER(Display), # display
                                    ctypes.c_int, # deviceid
                                    ctypes.c_ulong, # grab_window
                                    ctypes.c_int, # grab_mode
                                    ctypes.c_int, # paired_device_mode
                                    ctypes.c_int, # owner_events 
                                    ctypes.POINTER(XIEventMask), # mask
                                    ctypes.c_int, # num_modifiers 
                                    ctypes.POINTER(XIGrabModifiers) # modifiers_inout
                                    ]

XIGrabSwipeGestureBegin = libXInput.XIGrabSwipeGestureBegin
XIGrabSwipeGestureBegin.restype = ctypes.c_int
XIGrabPinchGestureBegin.argtypes = [ctypes.POINTER(Display), # display
                                    ctypes.c_int, # deviceid
                                    ctypes.c_ulong, # grab_window
                                    ctypes.c_int, # grab_mode
                                    ctypes.c_int, # paired_device_mode
                                    ctypes.c_int, # owner_events 
                                    ctypes.POINTER(XIEventMask), # mask
                                    ctypes.c_int, # num_modifiers 
                                    ctypes.POINTER(XIGrabModifiers) # modifiers_inout
                                    ]


XIUngrabButton = libXInput.XIUngrabButton
XIUngrabButton.restype = ctypes.c_int
XIUngrabButton.argtypes = [ctypes.POINTER(Display), # display 
                           ctypes.c_int, # deviceid
                           ctypes.c_int, # button
                           ctypes.c_ulong, # grab_window
                           ctypes.c_int, # num_modifiers
                           ctypes.POINTER(XIGrabModifiers) # modifiers
                           ]

XIUngrabKeycode = libXInput.XIUngrabKeycode
XIUngrabKeycode.restype = ctypes.c_int
XIUngrabKeycode.argtypes = [ctypes.POINTER(Display), # display 
                            ctypes.c_int, # deviceid
                            ctypes.c_int, # keycode
                            ctypes.c_ulong, # grab_window
                            ctypes.c_int, # num_modifiers
                            ctypes.POINTER(XIGrabModifiers) # modifiers
                            ]


XIUngrabEnter = libXInput.XIUngrabEnter
XIUngrabEnter.restype = ctypes.c_int
XIUngrabEnter.argtypes = [ctypes.POINTER(Display), # display 
                          ctypes.c_int, # deviceid
                          ctypes.c_ulong, # grab_window
                          ctypes.c_int, # num_modifiers
                          ctypes.POINTER(XIGrabModifiers) # modifiers
                          ]

XIUngrabFocusIn = libXInput.XIUngrabFocusIn
XIUngrabFocusIn.restype = ctypes.c_int
XIUngrabFocusIn.argtypes = [ctypes.POINTER(Display), # display 
                            ctypes.c_int, # deviceid
                            ctypes.c_ulong, # grab_window
                            ctypes.c_int, # num_modifiers
                            ctypes.POINTER(XIGrabModifiers) # modifiers
                            ]

XIUngrabTouchBegin = libXInput.XIUngrabTouchBegin
XIUngrabTouchBegin.restype = ctypes.c_int
XIUngrabTouchBegin.argtypes = [ctypes.POINTER(Display), # display 
                               ctypes.c_int, # deviceid
                               ctypes.c_ulong, # grab_window
                               ctypes.c_int, # num_modifiers
                               ctypes.POINTER(XIGrabModifiers) # modifiers
                               ]

XIUngrabPinchGestureBegin = libXInput.XIUngrabPinchGestureBegin
XIUngrabPinchGestureBegin.restype = ctypes.c_int
XIUngrabPinchGestureBegin.argtypes = [ctypes.POINTER(Display), # display 
                                      ctypes.c_int, # deviceid
                                      ctypes.c_ulong, # grab_window
                                      ctypes.c_int, # num_modifiers
                                      ctypes.POINTER(XIGrabModifiers) # modifiers
                                      ]



XIUngrabSwipeGestureBegin = libXInput.XIUngrabSwipeGestureBegin
XIUngrabSwipeGestureBegin.restype = ctypes.c_int
XIUngrabSwipeGestureBegin.argtypes = [ctypes.POINTER(Display), # display 
                                      ctypes.c_int, # deviceid
                                      ctypes.c_ulong, # grab_window
                                      ctypes.c_int, # num_modifiers
                                      ctypes.POINTER(XIGrabModifiers) # modifiers
                                      ]

XIListProperties = libXInput.XIListProperties
XIListProperties.restype = ctypes.POINTER(ctypes.c_ulong)
XIListProperties.argtypes = [ctypes.POINTER(Display), # display
                             ctypes.c_int, # deviceid
                             ctypes.POINTER(ctypes.c_int) # num_props_return
                             ]

XIChangeProperty = libXInput.XIChangeProperty
XIChangeProperty.restype = None
XIChangeProperty.argtypes = [ctypes.POINTER(Display), # display
                             ctypes.c_int, # deviceid
                             ctypes.c_ulong, # property
                             ctypes.c_ulong, # type
                             ctypes.c_int, # format
                             ctypes.c_int, # mode
                             ctypes.POINTER(ctypes.c_char), # data
                             ctypes.c_int # num_items
                             ]

XIDeleteProperty = libXInput.XIDeleteProperty
XIDeleteProperty.restype = None
XIDeleteProperty.argtypes = [ctypes.POINTER(Display), # display
                             ctypes.c_int, # deviceid
                             ctypes.c_ulong # property
                             ]

XIGetProperty = libXInput.XIGetProperty
XIGetProperty.restype = ctypes.c_int
XIGetProperty.argtypes = [ctypes.POINTER(Display), # display
                          ctypes.c_int, # deviceid
                          ctypes.c_ulong, # property
                          ctypes.c_long, # offset
                          ctypes.c_long, # length
                          ctypes.c_bool, # delete_property
                          ctypes.c_ulong, # type
                          ctypes.POINTER(ctypes.c_ulong), # type_return
                          ctypes.POINTER(ctypes.c_int), # format_return
                          ctypes.POINTER(ctypes.c_ulong), # num_items_return
                          ctypes.POINTER(ctypes.c_ulong), # bytes_after_return
                          ctypes.POINTER(ctypes.POINTER(ctypes.c_char)) # data
                          ]

XIBarrierReleasePointers = libXInput.XIBarrierReleasePointers
XIBarrierReleasePointers.restype = None
XIBarrierReleasePointers.argtypes = [ctypes.POINTER(Display), # display
                                     ctypes.POINTER(XIBarrierReleasePointerInfo), # barriers
                                     ctypes.c_int # num_barriers
                                     ]

XIBarrierReleasePointer = libXInput.XIBarrierReleasePointer
XIBarrierReleasePointer.restype = None
XIBarrierReleasePointer.argtypes = [ctypes.POINTER(Display), # display
                                    ctypes.c_int, # deviceid
                                    ctypes.c_ulong, # barrier
                                    ctypes.c_uint # eventid
                                    ]

XIFreeDeviceInfo = libXInput.XIFreeDeviceInfo
XIFreeDeviceInfo.restype = None
XIFreeDeviceInfo.argtypes = [ctypes.POINTER(XIDeviceInfo) # info
                             ]

