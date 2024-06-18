import subprocess
import ctypes
import sys
import requests
import google.generativeai as genai
import time
import random
import os


def install_java():
    try:
        j = subprocess.Popen(
        [
            "powershell.exe", 
            "-noprofile", "-c",
            r"""
            Start-Process -Verb RunAs -Wait powershell.exe -Args "
            -noprofile -c Set-Location \`"$PWD\`"; & .\modules\Scripts\java.ps1
            "
            """
        ],
        stdout=sys.stdout
        )
        j.communicate()
    except subprocess.CalledProcessError as e:
        print(f"Failed to run the PowerShell script as administrator. Error: {e}")
        return False
    return True


def install_cpp_c():

    try:
        c = subprocess.Popen(
        [
            "powershell.exe", 
            "-noprofile", "-c",
            r"""
            Start-Process -Verb RunAs -Wait powershell.exe -Args "
            -noprofile -c Set-Location \`"$PWD\`"; & .\modules\Scripts\cpp.ps1
            "
            """
        ],
        stdout=sys.stdout
        )
        c.communicate()

        package_name = "visualstudio2022buildtools"

        # Build the command list with arguments
        command = ["choco", "install", package_name, "-y"]

        # Add package parameters as separate arguments
        command.extend([
            "--add", "Microsoft.VisualStudio.Workload.MSBuildTools;includeRecommended",
            "--add", "Microsoft.VisualStudio.Workload.VCTools;includeRecommended",
            "--quiet"
        ])

        # Execute the choco install command using subprocess.run
        subprocess.run(command, check=True)

    except subprocess.CalledProcessError as e:
         print(f"Failed to run the PowerShell script as administrator. Error: {e}")
         return False
    return True
def install_python():
    try:
        p = subprocess.Popen(
        [
            "powershell.exe", 
            "-noprofile", "-c",
            r"""
            Start-Process -Verb RunAs -Wait powershell.exe -Args "
            -noprofile -c Set-Location \`"$PWD\`"; & .\modules\Scripts\pyth.ps1
            "
            """
        ],
        stdout=sys.stdout
        )
        p.communicate()
    except subprocess.CalledProcessError as e:
        print(f"Failed to run the PowerShell script as administrator. Error: {e}")
        return False
    return True
def install_node():
    s = subprocess.Popen(
    [
        "powershell.exe", 
            "./modules/Scripts/scoop.ps1"    
    ],
    stdout=sys.stdout
    )
    s.communicate()
    try:
        
        n = subprocess.Popen(
        [
            "powershell.exe", 
            "./modules/Scripts/node.ps1"    
        ],
        stdout=sys.stdout
        )
        n.communicate()
    except subprocess.CalledProcessError as e:
        print(f"Failed to run the PowerShell script as administrator. Error: {e}")
        return False
    return True
def vscode():
    try:
        v=subprocess.Popen(
            [   
                "powershell.exe", 
                "-noprofile", "-c",
                    r"""
                Start-Process -Verb RunAs -Wait powershell.exe -Args "
                -noprofile -c Set-Location \`"$PWD\`"; & .\modules\Scripts\Install-VSCode.ps1
                "
                """
            ],
            stdout=sys.stdout
            )
    except subprocess.CalledProcessError as e:
        print(f"Failed to run the PowerShell script as administrator. Error: {e}")
        return False
    return True
def gemini(max_retries, base_delay, question):
        retry_count = 0
        delay = base_delay
        model = genai.GenerativeModel('gemini-pro')
        os.environ["API_KEY"] = 'AIzaSyArPrXN78NBCpYel45TD_dnNd-M-NGOov4'# paste ur API Key
        genai.configure(api_key=os.environ["API_KEY"])
        while retry_count < max_retries:
            try:
                response = model.generate_content(str(question))
                return response.text
            except Exception as e:
                print(f"Error: {e}")
                # Increase delay with some randomness to avoid collisions
                delay *= 2  # Double the delay
                delay += random.uniform(0, delay)  # Add some randomness
                time.sleep(delay)
            retry_count += 1
        return None