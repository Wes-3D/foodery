1) Copy Repo

    git clone https://github.com/Wes-3D/foodery.git
    cd foodery

2) Create Certs

    mkdir -p assets/certs
    cd assets/certs

    # Generate a private key and certificate valid for 1 year
    openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes

3) Install packages & run app (on local port 5000)

    uv sync
    uv run main.py
