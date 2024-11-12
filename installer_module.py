import os
import requests
import subprocess

class Installer:
    def __init__(self, app_name, download_url, installer_path=None):
        self.app_name = app_name
        self.download_url = download_url
        # If no installer path is provided, use app_name as filename
        self.installer_path = installer_path if installer_path else f"{app_name}_installer.exe"

    def download(self):
        """Download the installer from the given URL."""
        print(f"Starting download for {self.app_name}...")
        response = requests.get(self.download_url, stream=True)
        if response.status_code == 200:
            with open(self.installer_path, 'wb') as installer_file:
                for chunk in response.iter_content(1024):
                    installer_file.write(chunk)
            print(f"{self.app_name} downloaded successfully: {self.installer_path}")
        else:
            print(f"Failed to download {self.app_name}.")
            response.raise_for_status()

    def install(self):
        """Run the installer to install the application."""
        print(f"Starting installation for {self.app_name}...")
        try:
            subprocess.run([self.installer_path, '/silent', '/install'], check=True)
            print(f"{self.app_name} installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Installation failed for {self.app_name}: {e}")

    def cleanup(self):
        """Delete the installer file after installation."""
        if os.path.exists(self.installer_path):
            os.remove(self.installer_path)
            print(f"Installer removed: {self.installer_path}")

    def download_and_install(self):
        """Download and install the application."""
        self.download()
        self.install()
        self.cleanup()
