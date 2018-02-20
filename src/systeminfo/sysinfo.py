
import platform
def get_platform_info():
    return platform.platform()

if __name__ == '__main__':
    print("Hi there!!", get_platform_info())
