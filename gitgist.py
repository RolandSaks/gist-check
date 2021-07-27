from __future__ import annotations


class GitGist:
    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"

    def __init__(self, id: str, owner: str, updated_at: str):
        self.id = id
        self.owner = owner
        self.updated_at = updated_at

    @staticmethod
    def from_json(gist_json: {}) -> GitGist:
        return GitGist(gist_json["id"],
                       gist_json["owner"]["login"],
                       gist_json["updated_at"])
