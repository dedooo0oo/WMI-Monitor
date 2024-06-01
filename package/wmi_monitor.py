'''
Matteo De Donno
wmi_monitor.py
'''

import time
import wmi
from icecream import ic
from utility import trace, csv_f_x, csv_f_1

ic.disable()

def get_process_info(out, process):
    '''
    Condition = A perfect call.
    Input     = List with the name of the values that u want to
                receive as a output on display (out).
                Object representing a connection with the 
                WMI service. 'process = wmi.WMI('.')'.
    Call      = No call.
    process   = Extracts information from the WMI service
                from the "Win32_process" class.
    Output    = The extracted information are printed on 
                the screen (selected ones).
    Return    = Two different list, one with all the names
                and one with all the values extracted from the
                WMI.
    '''
    prop_names = []
    prop_values = []
    for col_items in process.Win32_process():
        for prop in col_items.Properties_:
            prop_names.append(prop.Name)
            prop_values.append(prop.Value)
    prop_names = prop_names[:45]
    process_number = len(prop_values) // len(prop_names)
    if len(out) != 0:
        for j in range(process_number):
            ic("\nprocess number:", j + 1)
            for i, prop_name in enumerate(prop_names):
                prop_index = j * len(prop_names) + i
                if prop_name in out:
                    ic(prop_name, prop_values[prop_index])
    return prop_names, prop_values, process_number


def get_logical_disk_info(out, disks):
    '''
    Condition = A perfect call.
    Input     = List with the name of the values that u want to
                receive as a output on display (out).
                Object representing a connection with the 
                WMI service. 'disks = wmi.WMI('.')'.
    Call      = No call.
    process   = Extracts information from the WMI service
                from the "Win32_LogicalDisk" class.
    Output    = The extracted information are printed on 
                the screen (selected ones).
    Return    = Two different list, one with all the names
                and one with all the values extracted from the
                WMI.
    '''
    prop_names = []
    prop_values = []
    for col_items in disks.Win32_LogicalDisk():
        for prop in col_items.Properties_:
            prop_names.append(prop.Name)
            prop_values.append(prop.Value)
        free_space_percent = (int(col_items.FreeSpace) / int(col_items.Size)) * 100
        prop_names.append("FreeSpacePercentage")
        prop_values.append(str(round(free_space_percent)) + "%")
    prop_names = prop_names[:41]
    disk_number = len(prop_values) // len(prop_names)
    if len(out) != 0:
        for j in range(disk_number):
            ic("\nDisk Number:", j + 1)
            for i, prop_name in enumerate(prop_names):
                prop_index = j * len(prop_names) + i
                if prop_name in out:
                    ic(prop_name, prop_values[prop_index])
    return prop_names, prop_values, disk_number


def get_os_info(out, c):
    '''
    Condition = A perfect call.
    Input     = List with the name of the values that u want to
                receive as a output on display (out).
                Object representing a connection with the 
                WMI service. 'c = wmi.WMI('.')'.
    Call      = No call.
    process   = Extracts information from the WMI service
                from the "Win32_OperatingSystem" class.
    Output    = The extracted information are printed on 
                the screen (selected ones).
    Return    = Two different list, one with all the names
                and one with all the values extracted from the
                WMI.
    '''
    prop_names = []
    prop_values = []
    for col_items in c.Win32_OperatingSystem():
        for prop in col_items.Properties_:
            prop_names.append(prop.Name)
            prop_values.append(prop.Value)
    for prop_name in out:
        for col_items in c.Win32_OperatingSystem():
            if prop_name in [prop.Name for prop in col_items.Properties_]:
                for prop in col_items.Properties_:
                    if prop.Name == prop_name:
                        prop_value = prop.Value
                        break
                ic('Product', prop_name, prop_value)
    return prop_names, prop_values


def get_product_info(out, c):
    '''
    Condition = A perfect call.
    Input     = List with the name of the values that u want to
                receive as a output on display (out).
                Object representing a connection with the 
                WMI service. 'c = wmi.WMI('.')'.
    Call      = No call.
    process   = Extracts information from the WMI service
                from the "Win32_Product" class.
    Output    = The extracted information are printed on 
                the screen (selected ones).
    Return    = Two different list, one with all the names
                and one with all the values extracted from the
                WMI.
    '''
    prop_names = []
    prop_values = []
    for col_items in c.Win32_Product():
        for prop in col_items.Properties_:
            prop_names.append(prop.Name)
            prop_values.append(prop.Value)
    for prop_name in out:
        for col_items in c.Win32_Product():
            if prop_name in [prop.Name for prop in col_items.Properties_]:
                for prop in col_items.Properties_:
                    if prop.Name == prop_name:
                        prop_value = prop.Value
                        break
                ic('Product', prop_name, prop_value)
    return prop_names, prop_values


def main():
    '''
    Condition = A perfect call.
    Input     = None.
    Call      = No call.
    Process   = This function creates an instance of the WMI 
                service connection and attempts to extract
                operating system, product, logical disk, and 
                process information from the WMI service.
                It calls the corresponding functions to 
                retrieve and save this information to CSV files.
                It also handles and logs any exceptions 
                that occur during the execution of these 
                extraction processes.
    Output    = The extracted information is saved to CSV files.
    Return    = None.
    '''
    obj_wmi_service = wmi.WMI('.')
    try:
        ext_out_os = []
        prop_n_os, prop_val_os = get_os_info(ext_out_os, obj_wmi_service)
        csv_f_1(prop_n_os, prop_val_os, '../flussi/os.csv')
    except Exception as e:
        ic(f"An error occurred in OS information: {e}")
        trace(f"An error occurred in OS information: {e}", "../log/trace.log")

    try:
        ext_out_product = []
        prop_n_product, prop_val_product = get_product_info(ext_out_product, obj_wmi_service)
        csv_f_1(prop_n_product, prop_val_product, '../flussi/product.csv')
    except Exception as e:
        ic(f"An error occurred in product information: {e}")
        trace(f"An error occurred in product information: {e}", "../log/trace.log")

    try:
        ext_out_disk = []
        prop_n_disk, prop_val_disk, n = get_logical_disk_info(ext_out_disk, obj_wmi_service)
        csv_f_x(prop_n_disk, prop_val_disk, n, '../flussi/disk.csv')
    except Exception as e:
        ic(f"An error occurred in disk information: {e}")
        trace(f"An error occurred in disk information: {e}", "../log/trace.log")

    try:
        ext_out_process = []
        prop_n_process, prop_val_process, n = get_process_info(ext_out_process, obj_wmi_service)
        csv_f_x(prop_n_process, prop_val_process, n, '../flussi/process.csv')
    except Exception as e:
        ic(f"An error occurred in process information: {e}")
        trace(f"An error occurred in process information: {e}", "../log/trace.log")


if __name__ == "__main__":
    t1 = time.time()
    trace("Start", "../log/trace.log")
    try:
        main()
        trace("Good", "../log/trace.log")
    except Exception as er:
        trace(f"Error: {er}", "../log/trace.log")
    finally:
        t2 = time.time()
        ic(t2 - t1)
