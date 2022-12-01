from src.app import app

HOST = 'localhost'
PORTA = 4000
DEBUG = True

if __name__ == '__main__':
    app.run(HOST, PORTA, DEBUG)
