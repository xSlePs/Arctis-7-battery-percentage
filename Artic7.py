#!/usr/bin/env python3

import time, sys, hid
from PySide2 import QtWidgets, QtGui 
from datetime import datetime

VENDOR_ID = 0x1038
PRODUCT_ID = 0x12ad
ENDPOINT = 5

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, battery, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip(f'{battery} %')

def open_device(vendor_id, product_id, endpoint):
    path = None
    device = hid.device()

    # Search the device
    for interface in hid.enumerate(vendor_id, product_id):
        if interface["interface_number"] == endpoint and interface["usage"] > 1:
            path = interface["path"]
            device.open_path(path)
            return device

    raise Exception("No device found")
                
def get_status():
    status = {
        "headset_connected": False,
        "headset_battery": 0,
        }

    try:
        device = open_device(VENDOR_ID, PRODUCT_ID, ENDPOINT)   
    except Exception:
        return status

    # check if the headset is on
    device.write(b"\x06\x14")
    data = device.read(31)
    if data[2] == 0x03:
        status["headset_connected"] = True

    # Get battery level
    device.write(b"\x06\x18")
    data = device.read(31)
    status["headset_battery"] = data[2]

    device.close()

    return status

def GetDate():
    today = datetime.now()
    d1 = today.strftime("%H:%M:%S")
    return d1

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    start = 0
    AlertUser = 0
    while True:
        if start != 0:
            tray_icon.hide()
        status = get_status()
        tray_icon = SystemTrayIcon(QtGui.QIcon(sys.path[0]+"\\images\\"+str(status["headset_battery"])+".png"),status["headset_battery"], w)
        tray_icon.show()
        if status["headset_battery"] <= 10 and status["headset_battery"] > 0 and AlertUser == 0:
            tray_icon.showMessage('SteelSeries - Artic 7', 'Warning ! Low battery')
            AlertUser = 1

        print(f"{GetDate()}  -  {status['headset_battery']}%")
        start = 1
        time.sleep(600)
        

if __name__ == '__main__':
    main()