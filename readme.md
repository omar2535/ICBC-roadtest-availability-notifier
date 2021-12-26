# ICBC roadtest booker

## Setup

```sh
python3 -m venv .env
source .env/bin/activate
```

## Install chrome driver

### 1

```sh
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb

google-chrome --version
```

### 2

Now go here and install the correct version of chrome-driver: [chromedriver-downloads](https://chromedriver.chromium.org/downloads)

### 3

Install the chrome-driver

```sh
wget https://chromedriver.storage.googleapis.com/96.0.4664.45/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
```

and clean up:

```sh
rm chromedriver_linux64.zip && rm google-chrome-stable_current_amd64.deb
```
