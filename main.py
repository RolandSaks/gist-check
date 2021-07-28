import logging
import time
from typing import List
from cmreslogging.handlers import CMRESHandler


from gitgist import GitGist
from gitmonitor import GitGistMonitor
from repository import save_gists, load_gists
from pipecrmdeal import create_new_deal

USERNAMES = ["antomer", "RolandSaks"]
# logging.basicConfig(level=logging.INFO)
handler = CMRESHandler(hosts=[{'host': 'elasticsearch', 'port': 9200}],
                           auth_type=CMRESHandler.AuthType.NO_AUTH,
                           es_index_name="pipedrive_test")                   
log = logging.getLogger("RolandTest")
log.setLevel(logging.DEBUG)
log.addHandler(handler)




def callback_func(user, gists: List[GitGist]) -> None:
    log.info("Monitor reported user [%s] gists: %s", user, [x.id for x in gists])

    if gists:
        save_gists(gists)
        id = [x.id for x in gists]
        for username in id:
           create_new_deal(user, username)
     

def run() -> None:

    gists = load_gists()
    log.info("Loaded %s gists from storage: %s", len(gists), [gist.id for gist in gists])

    monitor = GitGistMonitor(GitGistMonitor.Parameters(usernames=USERNAMES,
                                                       callback=callback_func,
                                                       interval=400))
    monitor.start()


if __name__ == "__main__": 
    run()                      

