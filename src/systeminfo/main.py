import sysinfo # your own sysinfo module

def main():
    output = sysinfo.get_platform_info()
    print(output)
    return
