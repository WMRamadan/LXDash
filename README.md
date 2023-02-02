# LXDash

A Dashboard for LXD/LXC

## Requirements

- Python3
- python3-virtualenv
- python3-pip

## Setup

1. Create and activate virtual environment and install dependencies:
```bash
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

2. Copy `.env-example` to `.env`:
```bash
cp .env-example .env
```

3. Run django server:
```bash
cd lxdash/
python3 manage.py runserver
```

## Generate a New Django Secret Key with the following:
```bash
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
