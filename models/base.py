"""Base Model definition"""

import json
import datetime


class Base():
    """Base Model"""

    def to_dict(self) -> dict:
        """Serialize document to a python dictionary

        Returns:
          dict: document as python dictionary

        """

        obj = json.loads(self.to_json())
        obj["_id"] = obj["_id"]["$oid"]
        return obj

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        return super().save(*args, **kwargs)
