from src.domain.entities.user_profile import UserProfile

class IUserProfileUseCase:
    def create_user_profile(self, user_profile: UserProfile) -> UserProfile:
        raise NotImplementedError

    def get_user_profile(self, user_id: int) -> UserProfile:
        raise NotImplementedError

    def update_user_profile(self, user_profile: UserProfile) -> UserProfile:
        raise NotImplementedError

    def delete_user_profile(self, user_profile: UserProfile) -> None:
        raise NotImplementedError