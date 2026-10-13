"""Safe process-monitoring utilities for the detection project."""

import os
import platform
from datetime import datetime


def get_system_info() -> dict:
    """Return basic system information without collecting keystrokes."""

    return {
        "platform": platform.system(),
        "platform_release": platform.release(),
        "process_id": os.getpid(),
        "checked_at": datetime.now().astimezone().isoformat(
            timespec="seconds"
        ),
    }


if __name__ == "__main__":
    info = get_system_info()

    print("SYSTEM MONITOR")
    print("-" * 30)

    for key, value in info.items():
        print(f"{key}: {value}")
