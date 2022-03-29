from . import create_engine
# DB_HOST = config('DB_HOST')
# DB_NAME = config('DB_NAME')
# DB_USERNAME = config('DB_USERNAME')
# DB_PASSWORD = config('DB_PASSWORD')
DB_HOST = "localhost"
DB_NAME = "rassam"
DB_USERNAME = "root"
DB_PASSWORD = ""


def get_engine():
    try:
        return create_engine(f"mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}", echo=True)
    except Exception as e:
        print('some error when database connection occur: ', e)