from models.talent import Talent


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
