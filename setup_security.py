import subprocess
import os
import sys

# 1. Define the list of packages we want to install
# 'ufw' is a firewall, 'fail2ban' protects against brute force attacks, 
# 'git' is for version control, 'htop' is a system monitor.
PACKAGES_TO_INSTALL = ["ufw", "fail2ban", "git", "htop", "neofetch"]

def run_command(command):
    """
    Runs a shell command and prints the output.
    If the command fails, it stops the script.
    """
    try:
        print(f"[*] Running: {command}")
        # subprocess.run allows Python to execute terminal commands
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"[!] Error running command: {command}")
        sys.exit(1)

def main():
    # 2. Check if the script is being run as root (sudo)
    if os.geteuid() != 0:
        print("This script must be run as root. Try 'sudo python3 setup_pi.py'")
        sys.exit(1)

    print("=== Starting Raspberry Pi 5 Automated Setup ===")

    # 3. Update the System
    print("\n--- Updating Package Lists ---")
    run_command("apt-get update")
    
    print("\n--- Upgrading Existing Packages ---")
    # '-y' automatically answers 'yes' to prompts
    run_command("apt-get upgrade -y")

    # 4. Install Essentials & Security Tools
    print(f"\n--- Installing Packages: {', '.join(PACKAGES_TO_INSTALL)} ---")
    run_command(f"apt-get install -y {' '.join(PACKAGES_TO_INSTALL)}")

    # 5. Configure Firewall (UFW)
    print("\n--- Configuring Firewall ---")
    # default deny incoming traffic
    run_command("ufw default deny incoming")
    # default allow outgoing traffic
    run_command("ufw default allow outgoing")
    # allow SSH connections (critical, otherwise you lock yourself out!)
    run_command("ufw allow ssh")
    # Enable the firewall
    print("Enabling UFW... (Press 'y' if prompted)")
    # We use --force to avoid the prompt asking for confirmation
    run_command("ufw --force enable")

    print("\n=== Setup Complete! ===")
    print("Your Pi is now updated, secured with a firewall, and ready for work.")
    print("Run 'neofetch' to see your system stats.")

if __name__ == "__main__":
    main()
