# PY-CERT-DAEMON

*All-in-One Python based daemon to sync CA and SSL Certificates*

![Last Commit](https://img.shields.io/github/last-commit/pingmyheart/Py-Cert-Daemon)
![Repo Size](https://img.shields.io/github/repo-size/pingmyheart/Py-Cert-Daemon)
![Issues](https://img.shields.io/github/issues/pingmyheart/Py-Cert-Daemon)
![Pull Requests](https://img.shields.io/github/issues-pr/pingmyheart/Py-Cert-Daemon)
![License](https://img.shields.io/github/license/pingmyheart/Py-Cert-Daemon)
![Top Language](https://img.shields.io/github/languages/top/pingmyheart/Py-Cert-Daemon)
![Language Count](https://img.shields.io/github/languages/count/pingmyheart/Py-Cert-Daemon)

## 🚀 Overview

**Py-Cert-Daemon** is a lightweight daemon service designed to automate the renewal of SSL certificates issued by the
*Py-Cert-Server*. It periodically checks for certificates updates and sync them with devices or services that rely on
these.

## ✨ Features

- 🔄 **Automatic Renewal:** Periodically checks and sync CA and SSL certificates.
- 🛠️ **Lightweight:** Minimal resource usage, ideal for running on servers or edge devices.
- 🔧 **Configurable:** Easy to set up and customize according to your needs

## 🛠️ Getting Started

### Prerequisites

- Python 3.10+

### Installation

1. Download the executable to a desired location

```bash
wget https://github.com/pingmyheart/Py-Cert-Daemon/releases/download/{release_version}/py-cert-daemon-Linux
```

2. Create systemd service file

```bash
sudo touch /etc/systemd/system/pycertdaemon.service
```

3. Add the following content to the service file

```ini
[Unit]
Description=Python based Daemon to sync CA and SSL Certificates

[Service]
ExecStart=/usr/bin/bash /path/to/py-cert-daemon-Linux
Restart=always
User=nobody
WorkingDirectory=/tmp

[Install]
WantedBy=multi-user.target
```

4. Configure environment variables

```bash
export PCD_PY_CERT_SERVER_HOST=http://<py-cert-server-ip>:5000
export PCD_CLIENT_CONFIG_FILE=/path/to/application-client.yml
export PCD_SERVER_CONFIG_FILE=/path/to/application-server.yml
```

5. Enable and start the service

```bash
sudo systemctl enable pycertdaemon.service
sudo systemctl start pycertdaemon.service
```

### Usage

1. Configure correctly the `application-client.yml` and `application-server.yml` files with the necessary details.

#### Application Server Configuration

```yml
daemon:
  server:
    certificates:
      - id: 0645f0df-c8c4-45d8-adaa-984950c8a824
        destinations:
          certificate: /destination/workspace/domain.crt
          key: /destination/workspace/domain.key
```

#### Application Client Configuration

```yml
daemon:
  server:
    cas:
      - id: a678c663-4356-4fc5-825b-46266404dfbf           
```