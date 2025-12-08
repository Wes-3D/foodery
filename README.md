## Prerequisites: uv

        curl -LsSf https://astral.sh/uv/install.sh | sh

## Install

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


## Structure

        ~/
        ├─ main.py
        ├─ app/
        │  ├─ core/
        │  │  ├─ config.py
        │  │  ├─ log.py
        │  │  └─ security.py
        │  │
        │  ├─ db/
        │  │  ├─ db.py
        │  │  ├─ models.py
        │  │  └─ seed.py
        │  │
        │  ├─ crud/
        │  │  ├─ products.py
        │  │  ├─ recipes.py
        │  │  ├─ units.py
        │  │  └─ users.py
        │  │
        │  └─ routers/
        │     ├─ main.py
        │     ├─ products.py
        │     └─ recipes.py
        │
        └─ assets/
           ├─ certs/
           │  ├─ cert.pem
           │  └─ key.pem
           │
           ├─ static/
           │  ├─ css/
           │  └─ js/
           │     ├─ products.js
           │     ├─ product-scan.js
           │     ├─ recipes.js
           │     └─ recipe-add.js
           │
           └─ templates/
              ├─ base.html
              ├─ products.html
              ├─ product-scan.html
              ├─ recipes.html
              ├─ recipe-add.html
              └─ example.html


### Alt

        app/
        │
        ├─ main.py
        ├─ core/
        │   └── log.py
        │
        ├─ api/
        │   ├── __init__.py
        │   ├── router.py
        │   ├── ingredients.py
        │   └── recipes.py
        │
        ├─ db/
        │   ├── __init__.py
        │   ├── base.py
        │   ├── session.py
        │   └── init_db.py
        │
        ├─ models/
        │   ├── __init__.py
        │   ├── product.py
        │   ├── recipe.py
        │   └── recipe_step.py
        │
        ├─ schemas/
        │   ├── __init__.py
        │   ├── product.py
        │   ├── recipe.py
        │   └── recipe_step.py
        │
        └─ crud/
           ├─ __init__.py
           ├─ product.py
           └─ recipe.py



## Migration

        uv run alembic revision --autogenerate -m ""
        uv run alembic upgrade head

