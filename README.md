# Secure Remote Access Implementation (Raspberry Pi 5)

This project documents the implementation of a secure, headless remote management environment using a Raspberry Pi 5. The goal was to establish a secure command-and-control channel from a primary workstation to a remote Linux node, simulating a typical administrative workflow in a server environment.

### 🔧 Tech Stack
* **Hardware:** Raspberry Pi 5 (8GB RAM)
* **OS:** Raspberry Pi OS (Debian Bookworm)
* **Protocol:** SSH (Secure Shell) v2
* **Authentication:** RSA 4096-bit Key Pair (No password login)

### 🛡️ Security Configurations Implemented
To harden the connection against brute-force attacks and unauthorized access, I implemented the following changes in the `/etc/ssh/sshd_config` file:

1.  **Disabled Root Login:**
    * `PermitRootLogin no`
    * *Prevents attackers from trying to brute-force the administrative account directly.*
2.  **Disabled Password Authentication:**
    * `PasswordAuthentication no`
    * *Forces the use of cryptographic keys. Even if an attacker guesses the password, they cannot login.*
3.  **Changed Default SSH Port:**
    * Moved SSH from port `22` to a custom port to reduce noise from automated bot scanners.

### 📸 Proof of Concept

**1. Security & Hardware Verification**
*Below: Neofetch confirms the Raspberry Pi 5 hardware, and UFW status confirms the firewall is active and restricting traffic to SSH (Port 22).*

<img width="614" height="550" alt="security-verify" src="https://github.com/user-attachments/assets/a2326538-0465-4546-8018-4e29d51254a9" />

**2. System Monitoring**
*Below: Htop interface showing system resource usage and the active SSH session, verifying the headless configuration.*

<img width="1920" height="1080" alt="htop-monitor" src="https://github.com/user-attachments/assets/53f076e2-ceb7-4840-812b-192712bc18fd" />

### 🚀 Usage
To connect to the node, I use the following localized command:

```bash
ssh -i ~/.ssh/id_rsa_pi jeremy@10.0.0.X -p [CustomPort]
🤖 Automation
I wrote a Python script (setup_security.py) to automate the initial hardening process. This script ensures consistent security baselines across new devices by:

System Updates: Automatically runs apt-get update/upgrade.

Tool Installation: Installs fail2ban (Intrusion Prevention) and ufw (Firewall).

Firewall Config: Programmatically opens the SSH port while denying all other incoming traffic.

🧠 Lessons Learned
Key Management: Learned how to generate keys using ssh-keygen and securely transfer the public key using ssh-copy-id.

Linux Permissions: Understood the importance of chmod 600 for private keys; otherwise, the client refuses to use them (Unprotected Private Key File error).
