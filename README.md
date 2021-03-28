# Zolve Wallet Backend.

Zolve wallet allows user to signup to create their wallet, can do transactions from their wallet and
also allow them to get the list of transactions done.


### API Collection
[Postman Collection](https://www.getpostman.com/collections/66828e66412ff6d4205b)


### Prerequisites

- Python 3.6 and pip 3
- Postgres - 9.6+
- Redis 4

## Setup steps

1. Virtual Environment Setup:

    * Create and activate virtual environment

        virtualenv -p python3 /path/to/Envs/zolve
        source /path/to/Envs/zolve/bin/activate

    * Install the requirements by using command:
        `pip install -r requirements.txt`

1. Set Environment Values

    * Copy the .env_template to .env
    * Fill the values of .env as required

1. Run Migrations

    python manage.py migrate

1. To Runserver Locally (Not for Prod or staging):

    python manage.py runserver 8000

    The above command will run the server on port 8000

