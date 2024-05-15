## How to run?

### Requirements
- Python 3.11
- a Unix based environment
- Docker installed

### Run the API locally
1. Create a `.env` file with the `.env.example` info
2. Run the commands below to create and run the venv
    ```sh
        python -m venv venv
        source ./venv/bin/activate
    ```
3. Update your packages and run the api locally
    ```sh
        pip install -r requirements.txt
        python app.py
    ```

### Run the API and the collector with Docker
1. Create a `.env` file with the `.env.example` info
2. Just run
    ```sh
        docker compose up -d
    ```
3. Test the API and Collector