from tornado.web import Application
from tornado.ioloop import IOLoop
from resources.user import UserRegister
from resources.spending import SpendingItems, SpendingItem
from tornado.options import define, parse_config_file
import jwt

secret_key = "my_secret_key"

class InitialiseApp(Application):
    def __init__(self):
        handlers = [
            (r"/register", UserRegister),
            (r"/items", SpendingItems),
            (r"/item", SpendingItem)
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
    parse_config_file("./config/local.conf")
    run_server()