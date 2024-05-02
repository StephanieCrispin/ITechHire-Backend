from models.talent import Talent
from bson import ObjectId


class TalentServices:
    """Utility class for handling common talent logic"""

    @staticmethod
    def get_talent_by_email(email: str):
        """Get talent by email

        Args:
          email(str): user email
        """

        try:
            talent = Talent.objects(email=email).first()
            return talent
        except Exception as e:
            raise e
            return None

    @staticmethod
    def get_talent_by_id(id: str):
        """Get talent by id

        Args:
          id(str): user id
        """

        try:
            talent = Talent.objects.get(id=ObjectId(id))
            return talent
        except Exception as e:
            raise e
            return None
