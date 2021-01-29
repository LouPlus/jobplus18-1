from jobplus.app import create_app
from jobplus.config import configs

app = create_app('development')

if __name__ == '__main__':
    app.run()
