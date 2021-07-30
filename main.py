import logging
from typing import List
import flask


from client.gitgist import GitGist
from config.configuration import Configuration
from monitor.gitmonitor import GitGistMonitor
from log.logging import LoggingConfig
from storage.repository import save_gists
from pipecrmdeal import create_new_deal
from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def heartbeat():
    resp = flask.make_response(jsonify(status="UP"), 200)
    return resp


def callback_func(user, gists: List[GitGist]) -> None:
    logging.info("Monitor reported back [USER: {}] gists {}"
                 .format(user, [x.gist_id for x in gists]))

    if gists:
        save_gists(gists)
        for id in [x.gist_id for x in gists]:
            create_new_deal(user, id)


def init_monitor() -> None:
    GitGistMonitor(GitGistMonitor.Parameters(
        usernames=configuration.property("gists.monitor.usernames"),
        callback=callback_func,
        interval=configuration.property("gists.monitor.interval"))).start()


configuration = Configuration("../configuration.json")
LoggingConfig(configuration, logging.INFO)
init_monitor()

