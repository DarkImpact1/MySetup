from installer_module import Installer

def main():
    # Define applications to be downloaded and installed
    applications = [
        {"name": "Chrome", "url": "https://dl.google.com/chrome/install/latest/chrome_installer.exe"},
        # {"name": "VSCode", "url": "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user"},
    ]

    # Download and install each application
    for app in applications:
        installer = Installer(app_name=app["name"], download_url=app["url"])
        installer.download_and_install()

if __name__ == "__main__":
    main()
    # installer = Installer(app_name="Python", download_url="https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe")
    # installer.download()
    # installer.cleanup()
