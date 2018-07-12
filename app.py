from tornado.web import Application
from tornado.ioloop import IOLoop
import jwt

secret_key = "my_secret_key"

class InitialiseApp(Application):
    def __init__(self):
        handlers = [
            (r"/regiser")
        ]

        server_settings = {
            "debug": True,
            "autoreload": True
        }

        Application.__init__(self, handlers, **server_settings)


def run_server():
    app = InitialiseApp()
    app.listen(3000)
    IOLoop.instance().start()


if __name__ == '__main__':
    # import and run database
    run_server()
