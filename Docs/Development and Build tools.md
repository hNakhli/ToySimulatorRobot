The following tools and packages have been used in making this project:
- **Operating System**: Windows 10 - Version 22H2
- **Notes and documentation:** Obsidian - Version 1.7.7 https://obsidian.md/
- **Version Control:** Git CMD (windows) - Version 2.4.5.0.windows.1 https://gitforwindows.org/
- **Python Package manager:** UV 0.7.8
- **Python version:** 3.12.10 (cpython-3.12.10-windows-x86_64-none
- **IDE**: Visual Studio Code - April 2025 (version 1.100)
	- Official Microsoft Python Extension (version 2025.6.1)

Note that in the project we would be using .toml file for package versions used inside the project, and visual studio recommended packages are located in .vscode folder

## Python and package manager installation
In order to ensure the build system is common between all computers UV package management and virtual environments have been used. Although this is a fairly new package manager, but it provides lots of functionality which should allow an easier development. UV also handles dependency management and allows the team to sync their versions and libraries
### Steps to install uv:
1. Create a new folder on the local drive D:\\TempInstallationFolder\
2. Navigate to the folder
3. Download "uv-installer.ps1" from https://github.com/astral-sh/uv/releases/download/0.7.8/uv-installer.ps1 and move it to the temp folder
	1. **Note 1:** It would be possible to run the command directly from PowerShell but you might face some restrictions based on your firewall / antivirus setup. I have found it easier to download the package
	2. In my case the package name was "uv-x86_64-pc-windows-msvc"
4. Execute the PowerShell script by:
```
powershell -ExecutionPolicy Bypass
.\uv-installer.ps1
```
6. Add uv to the Paths by executing the following command in the PowerShell:
```
$env:Path = "C:\Users\Hmnak\.local\bin;$env:Path"
```
6. Set the execution policy back to Default 
```
powershell -ExecutionPolicy Default
```
7. Run/Test uv in PowerShell or cmd by typing uv - and delete the TempInstallationFolder:
![[uvCommand.png]]
### Steps to install python
After uv is installed, attempt to install the required python version using the following command:
```
uv python install
```
This would install the latest python version, for this package project - try to install the required version as specified above in the above section - as an example, you can install python v3.12 by executing the following command in PowerShell or cmd:
```
uv python install 3.12
```
### Useful links:
- Installation of UV: https://docs.astral.sh/uv/getting-started/installation/#installation-methods
- Installing Python: https://docs.astral.sh/uv/guides/install-python/
- Commands / Features: https://docs.astral.sh/uv/getting-started/features/#python-versions

## Visual Studio Code
Ensure the recommended extensions are installed - since the development is on windows, the pytest.exe and python.exe paths on visual studio are changed to be relative to the .venv folder (in Scripts). Please feel free to adjust this if required.


