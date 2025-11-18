from tables.users import User


class UserService:
    @staticmethod
    def get_user_by_email(email):
        try:
            return User.objects.get(email=email, deleted=False)
        except User.DoesNotExist:
            return None

    @staticmethod
    def create_user(first_name, last_name, email, password):
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        return user
