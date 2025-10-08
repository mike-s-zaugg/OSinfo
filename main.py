import platform, psutil, cpuinfo

def getSystemInfo():
    info = {}

    pName = platform.uname().system
    if "darwin" in pName.lower():
        pName = "macOS"

    info["os"] = pName
    info["osVersion"] = platform.uname().release
    info["osArch"] = platform.uname().machine

    info["cpu"] = cpuinfo.get_cpu_info()["brand_raw"]
    info["cpuCores"] = psutil.cpu_count(logical=False)
    info["cpuThreads"] = psutil.cpu_count(logical=True)

    ram = psutil.virtual_memory()
    info["ram"] = round(ram.total / 1024**3, 1)
    info["ramUsed"] = round((ram.total - ram.available) / 1024**3, 1)
    info["ramAvailable"] = round(ram.available / 1024**3, 1)
    info["ramPercent"] = ram.percent

    disk = psutil.disk_usage("/")
    info["disk"] = round(disk.total / 1024**3, 1)
    info["diskUsed"] = round((disk.total - disk.free) / 1024**3, 1)
    info["diskFree"] = round(disk.free / 1024**3, 1)
    info["diskPercent"] = disk.percent

    return info

def printSystemInfo(info):
    print("📦 System")
    print(f"  OS: {info['os']} {info['osVersion']} ({info['osArch']})\n")

    print("🧠 CPU")
    print(f"  Modell: {info['cpu']}")
    print(f"  Kerne: {info['cpuCores']}")
    print(f"  Threads: {info['cpuThreads']}\n")

    print("💾 RAM")
    print(f"  Gesamt: {info['ram']} GB")
    print(f"  Benutzt: {info['ramUsed']} GB ({info['ramPercent']}%)")
    print(f"  Frei: {info['ramAvailable']} GB\n")

    print("🗄️ Festplatte (/)")
    print(f"  Gesamt: {info['disk']} GB")
    print(f"  Benutzt: {info['diskUsed']} GB ({info['diskPercent']}%)")
    print(f"  Frei: {info['diskFree']} GB")

if __name__ == '__main__':
    info = getSystemInfo()
    printSystemInfo(info)
