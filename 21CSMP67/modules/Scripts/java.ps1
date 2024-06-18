
# Define download URL and installer location
$java17Url = "https://download.oracle.com/java/17/latest/jdk-17_windows-x64_bin.exe"
$installer = "$env:TEMP\jdk-17_windows-x64_bin.exe"

# Download Java 17 installer
Invoke-WebRequest -Uri $java17Url -OutFile $installer

# Install Java 17 silently
Start-Process -FilePath $installer -ArgumentList "/s" -Wait

# Remove installer
Remove-Item $installer

