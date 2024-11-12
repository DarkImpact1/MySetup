from installer_module import Installer

def main():
    # Define applications to be downloaded and installed
    applications = [
            {"name": "Chrome", "url": "https://dl.google.com/chrome/install/latest/chrome_installer.exe"},
            {"name": "VSCode", "url": "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user"},
            {"name": "Git", "url": "https://github.com/git-for-windows/git/releases/download/v2.42.0.windows.1/Git-2.42.0-64-bit.exe"},
            {"name": "WhatsApp", "url": "https://web.whatsapp.com/desktop/windows/release/ia32/WhatsAppSetup.exe"}
        ]

    # Download and install each application
    for app in applications:
        installer = Installer(app_name=app["name"], download_url=app["url"])
        installer.download_and_install()

if __name__ == "__main__":
    main()

