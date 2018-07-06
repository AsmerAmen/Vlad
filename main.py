from GUI import GUI
from wakeup import wake_up

import threading
from threading import Thread


if __name__ == '__main__':
    # Thread(target= GUI).start()
    # Thread(target= wake_up).start()
    wake_up()