from plyer import notification

def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = r"C:\Users\Cliffex-Lead\Downloads\srk.ico",
        timeout = 2
    )

if __name__ == '__main__':
    notifyMe("Piyush","lets stopes this")


