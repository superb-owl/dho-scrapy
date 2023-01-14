from pathlib import Path
from typing import List, Dict

from dho_scraper.items import DhOMessage


class MessageDB:

    def __init__(self, msgs: List[DhOMessage]):
        self._msgs = msgs

    @classmethod
    def from_file(cls, jsonl_path: Path) -> 'MessageDB':

        msgs = []

        with open(jsonl_path, 'r') as f:
            for line in f.readlines():
                msg = DhOMessage.parse_raw(line)
                msgs.append(msg)

        return cls(msgs=msgs)

    def get_all_messages(self) -> List[DhOMessage]:
        return self._msgs.copy()

    def sorted_by_date(self) -> 'MessageDB':
        sorted_msgs = sorted(self.get_all_messages(), key=lambda m: m.date)
        return MessageDB(msgs=sorted_msgs)

    def group_by_author(self) -> Dict[str, List[DhOMessage]]:

        author_msgs: dict = dict()

        for msg in self._msgs:
            author_msgs[msg.author] = author_msgs.get(msg.author, [])
            author_msgs[msg.author].append(msg)

        return author_msgs
