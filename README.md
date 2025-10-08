💻 System Information Tool (System Info Skript)
A Python script designed to retrieve and display detailed information about the host system's OS, CPU, RAM, and Disk Usage.

Note: The script's console output (labels and descriptions) is intentionally displayed in German.

🛠️ Requirements
This script relies on external Python packages (psutil and py-cpuinfo) for system access. You must install them using pip:

Installation
pip install psutil py-cpuinfo

psutil: Used for cross-platform system monitoring (CPU counts, RAM, Disk usage).

py-cpuinfo (imported as cpuinfo): Used to gather detailed CPU model information.

platform: (Standard library) Used for basic OS identification.

🚀 Getting Started
Running the Script
Save the code as a Python file (e.g., system_info.py).

Ensure all required dependencies are installed.

Execute the script from your terminal:

python system_info.py

📊 Example Output
The script provides an organized output structure with German labels:

📦 System
  OS: macOS 14.5 (arm64)

🧠 CPU
  Modell: Apple M3 Max
  Kerne: 14
  Threads: 14

💾 RAM
  Gesamt: 32.0 GB
  Benutzt: 18.5 GB (57.8%)
  Frei: 13.5 GB

🗄️ Festplatte (/)
  Gesamt: 1000.0 GB
  Benutzt: 450.0 GB (45.0%)
  Frei: 550.0 GB

⚙️ Functionality Details
The script is structured around two main functions:

getSystemInfo():

Collects raw data from the imported libraries.

Converts RAM and Disk statistics into Gigabytes (GB), rounding values to one decimal place.

Includes special handling to rename the "darwin" OS kernel name to "macOS" for better readability.

Returns all collected data as a Python dictionary.

printSystemInfo(info):

Takes the gathered data dictionary and formats it into the clean, emoji-enhanced, human-readable output you see above.

Uses German labels (Gesamt, Benutzt, Frei, Kerne, etc.) for all printed statistics.
