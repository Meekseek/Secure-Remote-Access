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
*(Place your screenshot here. Drag and drop the image file into this text box while editing, and GitHub will automatically generate the code for it.)*

### 🚀 Usage
To connect to the node, I use the following localized command:

```bash
ssh -i ~/.ssh/id_rsa_pi jeremy@10.0.0.X -p [CustomPort]
