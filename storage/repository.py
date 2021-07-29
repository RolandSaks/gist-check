import logging
import os
import pickle
from typing import List

from client.gitgist import GitGist

HISTORY = os.path.join(os.path.dirname(__file__), 'history.pkl')
GISTS = os.path.join(os.path.dirname(__file__), 'gists.pkl')


def save_gists(update: List[GitGist]) -> None:
    if update:
        gists = load_gists()
        gists += update

        with open(GISTS, 'wb') as o:
            pickle.dump(gists, o, protocol=pickle.HIGHEST_PROTOCOL)
            logging.debug('Gists saved.')


def load_gists() -> List[GitGist]:
    try:
        with open(GISTS, 'rb') as i:
            return pickle.load(i)
    except (FileNotFoundError, EOFError):
        return []


def save_log(update: dict) -> None:
    if update:
        history = load_log()

        for user, last_checked_at in update.items():
            history[user] = last_checked_at

        with open(HISTORY, 'wb') as o:
            pickle.dump(history, o, protocol=pickle.HIGHEST_PROTOCOL)
            logging.debug("Request log updated.")


def load_log() -> dict:
    try:
        with open(HISTORY, 'rb') as i:
            history = pickle.load(i)

            for user, last_checked_at in history.items():
                history[user] = last_checked_at

            return history
    except (FileNotFoundError, EOFError):
        return {}
