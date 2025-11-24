from time import time

limits = {}

def rate_limit(identifier: str, max_requests: int, window: int):
    current = time()
    windows = limits.get(identifier, [])
    windows = [t for t in windows if current - t < window]
    if len(windows) >= max_requests:
        return False
    windows.append(current)
    limits[identifier] = windows
    return True
