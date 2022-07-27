from socket import timeout
import time
from turtle import title

from pip import main
from plyer import notification

if __name__ == "__main__":
    while True:

        notification.notify(
            title = "Boss Drink water",
            message = "Boss , To improve your Skin Complexion your doctor told you to drink water in every 2 hourse,here's the reminder for that.",
            app_icon = "C:\\sanchit\\py project\\reminder\\Glass.ico",
            timeout = 12
        )
        time.sleep(60*120)
