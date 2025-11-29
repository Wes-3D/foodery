1) Copy Repo

    git clone https://github.com/Wes-3D/foodery.git

    cd foodery


3) Create Certs

    mkdir -p certs

    cd certs

    # Generate a private key and certificate valid for 1 year
   
    openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes


5) Install packages & run app

    uv sync
   
    uv run main.py
