# WMI Monitor

![Language](https://img.shields.io/badge/Spellcheck-Pass-green?style=flat)
![Platform](https://img.shields.io/badge/OS%20platform%20supported-Windows,Linux-blue?style=flat)
![Language](https://img.shields.io/badge/Language-Python-yellowgreen?style=flat)
![Testing](https://img.shields.io/badge/PEP8%20CheckOnline-90+%-green)
![Testing](https://img.shields.io/badge/Test-Pass-green)

## Project Description

The **WMI Monitor** project is a Python script designed to extract information from the Windows operating system using the Windows Management Instrumentation (WMI) service. This script collects information about the operating system, installed products, logical disks and running processes, and saves this information in CSV files. In addition, the project manages error tracking and logging.

## Project Structure

- **Matteo De Donno**: Author of the project.
- **wmi_monitor.py**: Main script containing the extraction functions and management logic.

## Main Functions

### `get_process_info(out, process)`
Extracts information about running processes.

- **Parameters**:
    - `out`: List with the names of the properties to display.
    - `process`: Object representing the connection with the WMI service.
- **Returns**: Two lists containing the names and values ​​of the extracted properties, and the number of processes.

### `get_logical_disk_info(out, disks)`
Extracts information about the logical disks of the system.

- **Parameters**:
    - `out`: List with the names of the properties to display.
    - `disks`: Object representing the connection with the WMI service.
- **Returns**: Two lists containing the names and values ​​of the extracted properties, and the number of disks.

### `get_os_info(out, c)`
Extracts information about the operating system.

- **Parameters**:
    - `out`: List with the names of the properties to display.
    - `c`: Object representing the connection with the WMI service.
- **Returns**: Two lists containing the names and values ​​of the extracted properties.

### `get_product_info(out, c)`
Extracts information about the installed products.

- **Parameters**:
    - `out`: List with the names of the properties to display.
    - `c`: Object representing the connection with the WMI service.
- **Returns**: Two lists containing the names and values ​​of the extracted properties.

### `main()`
Main function that coordinates the extraction of information and its storage in CSV files. It also manages error logging.

## Usage

To run the project, make sure you have the following Python packages installed:
- ***`wmi`***
- ***`icecream`***
- ***`utility`*** (containing the functions `trace`, `csv_f_x` and `csv_f_1`)

## Run the script:
```
python wmi_monitor.py
```

## System Requirements
- Windows Operating System
- Python 3.x
- Access to the WMI service

## Tracing Logic
The script uses the trace function to record the start, end and any errors during the execution of the script.
The logs are saved in the file ***`./log/trace.log`***.

## Output Example
The extracted data is saved in CSV files in the following paths:

***`Informazioni sul sistema operativo: ./flussi/os.csv`***

***`Informazioni sui prodotti installati: ./flussi/product.csv`***

***`Informazioni sui dischi logici: ./flussi/disk.csv`***

***`Informazioni sui processi: ./flussi/process.csv`***

### Notes
The ic.disable() function disables debug prints to avoid unwanted output during script execution.
Make sure that the paths for CSV files and logs are valid and accessible by the system.

## Author
Matteo De Donno