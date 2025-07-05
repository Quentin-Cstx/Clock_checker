import psutil
import time
from plyer import notification
from datetime import datetime, timedelta

def check_uptime():
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    now = datetime.now()
    uptime = now - boot_time

    if uptime > timedelta(days=1):
        days = uptime.days
        hours = uptime.seconds // 3600
        plural_days = "s" if days > 1 else ""
        plural_hours = "s" if hours > 1 else ""
        notification.notify(
            title="Alert : uptime reached!",
            message=f"Your processor is up since {str(days)} day{plural_days} and {str(hours)} hour{plural_hours}. Time to reboot!",
            timeout=10  # en secondes
        )

if __name__ == "__main__":
    check_uptime()
