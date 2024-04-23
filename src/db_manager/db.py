import json
import os
from datetime import datetime
from typing import Optional

from src.config import Config


class DB:
    """
    Currently handling db with json files is easier
    than to have a dedicated database

    # TODO methods can be optimized by using a single file handler and data
    # TODO models can be added
    """

    def __init__(self) -> None:
        self.db_loc = os.path.join(Config.cwd, "src", "db_manager", "db")

    def get(self, collection_name: str, key: Optional[str] = "", _id: Optional[int] = -1) -> dict:
        """
        Get DB instance
        :return: {"result": data}
        """
        if not collection_name:
            raise ValueError("Collection Name can not ve empty")

        collection_loc = os.path.join(self.db_loc, f"{collection_name}.json")

        with open(collection_loc, "r") as f:
            data = json.load(f)

        if key:
            data = data.get(key)

        if _id >= 0 and isinstance(data, list):
            for d in data:
                if _id == d.get("_id"):
                    data = d
                    break
        result = {"result": data}
        return result

    def insert(self, collection_name: str, key: str, value: dict) -> int:
        """
        No uniqueness check, no models
        """
        collection_loc = os.path.join(self.db_loc, f"{collection_name}.json")

        with open(collection_loc, "r") as f:
            data = json.load(f)
            val = data.get(key)
            current_id = len(val) + 1
            data["current_id"] = current_id
            value["_id"] = current_id
            value["created_at"] = str(datetime.now())
            val.append(value)

        with open(collection_loc, "w") as f:
            json.dump(data, f)

        return current_id

    def get_collection_size(self, collection_name: str, key: str) -> int:
        collection_loc = os.path.join(self.db_loc, f"{collection_name}.json")

        with open(collection_loc, "r") as f:
            data = json.load(f)
            val = data.get(key)

        return len(val)
