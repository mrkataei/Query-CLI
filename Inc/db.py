from . import create_engine

# create mysql or postgresql and change line bellow
# if you use postgresql change mysql engine
DB_HOST = "localhost"
DB_NAME = "rassam"
DB_USERNAME = "root"
DB_PASSWORD = ""


def get_engine():
    try:
        return create_engine(f"mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}", echo=True)
    except Exception as e:
        print('some error when database connection occur: ', e)
