from __future__ import annotations

import logging
import threading
from datetime import datetime
from typing import List, Callable

import schedule
import time

from gistsclient import GistsClient
from repository import load_log, save_log

log = logging.getLogger("RolandTest")


class GitGistMonitor:

    def __init__(self, parameters: Parameters):
        self.client = GistsClient()

        self.parameters = parameters
        self.stop_event = threading.Event()

        self.gists = {user: [] for user in parameters.usernames}
        self.last_check_log = {user: None for user in parameters.usernames}

        for user, last_checked_at in load_log().items():
            self.last_check_log[user] = last_checked_at

    def start(self) -> GitGistMonitor:
        log.info("Starting GitHub Gist monitor. Check interval: %ss", self.parameters.interval)

        schedule.every(self.parameters.interval).seconds.do(self.check_gists)
        thread = threading.Thread(target=self.run_timer)
        thread.start()

        self.check_gists()
        return self

    def stop(self) -> GitGistMonitor:
        log.info("Stopping GitHub gist monitor.")
        self.stop_event.set()
        return self

    def run_timer(self, interval_s: int = 1):
        while not self.stop_event.is_set():
            schedule.run_pending()
            time.sleep(interval_s)

    def check_gists(self) -> None:
        for user in self.parameters.usernames:
            gists = self.client.fetch_gists(user, self.last_check_log[user])
            log.info("Found %s new gists for user %s.", len(gists), user)
            self.set_checked(user)

            if len(gists) > 0:
                self.parameters.callback(user, gists)


    def set_checked(self, user: str, timestamp: datetime = datetime.utcnow()) -> None:
        self.last_check_log[user] = timestamp.isoformat()[:-4] + "Z"
        save_log(self.last_check_log)

    class Parameters:
        DEFAULT_INTERVAL_S = 15

        def __init__(self,
                     usernames: List[str],
                     interval: int = DEFAULT_INTERVAL_S,
                     callback: Callable = lambda *args: None):
            self.usernames = usernames
            self.interval = interval
            self.callback = callback
