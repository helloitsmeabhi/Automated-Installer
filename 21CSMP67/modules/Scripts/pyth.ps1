
# Define download URL and installer location
$pythonUrl = "https://www.python.org/ftp/python/3.12.4/python-3.12.4-amd64.exe"
$installer = "$env:TEMP\python-3.12.4-amd64.exe"

# Download Java 17 installer
Invoke-WebRequest -Uri $pythonUrl -OutFile $installer

# Install Java 17 silently
Start-Process -FilePath $installer -ArgumentList "/s" -Wait

# Remove installer
Remove-Item $installer

