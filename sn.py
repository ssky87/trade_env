import platform
import psutil
import os
import sys
import struct
import fcntl


def computer_data():
    perfil_information = ['architecture', 'machine', 'release', 'system', 'version', 'node', 'platform', 'processor']
    print(' ')
    print('='*40, 'System Information', '='*40)
    # recorremos lista para obtener los datos
    for data in perfil_information:
        if hasattr(platform, data):
            print('[+] %s: %s' % (data, getattr(platform,data)()))

def getSeialNumber():
    # serial number HDD
    os_type = sys.platform.lower()
    if 'darwin' in os_type:
        command = "ioreg -l | grep IOPlatformSerialNumber"
        print('[+] Serial Number: %s' % os.popen(command).read().split()[-1])
    elif 'win' in os_type:
        command = "wmic bios get serialnumber"
        print('[+] Serial Number: %s' % os.popen(command).read().split()[-1])
    elif 'linux' in os_type:
        '''
        serialnumber = "hdparm -I /dev/sda | grep 'Serial Number'"
        modelnumber = "hdparm -I /dev/sda | grep 'Model'"
        print('[+] Serial Number: %s' % os.popen(serialnumber).read().split()[-1])
        print('[+] Model Number: %s' % os.popen(modelnumber).read().split()[-2])
        '''
        with open('/dev/sblkdev0', 'rb') as fd:
            hd_driveid_format_str = "@ 10H 20s 3H 8s 40s 2B H 2B H 4B 6H 2B I 36H I Q 152H"

            HDIO_GET_IDENTITY = 0x030d 
            sizeof_hd_driveid = struct.calcsize(hd_driveid_format_str)

            assert sizeof_hd_driveid == 512
            buf = fcntl.ioctl(fd, HDIO_GET_IDENTITY, " " * sizeof_hd_driveid) 
            fields = struct.unpack(hd_driveid_format_str, buf)
            serial_no = fields[10].strip()
            model = fields[15].strip()
            print("[+] Hard Disk Model: %s" % model)
            print("[+] Serial Number: %s" % serial_no)

getSeialNumber()
