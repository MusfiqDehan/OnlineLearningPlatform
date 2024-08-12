import logging
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

logger = logging.getLogger(__name__)


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        logger.info("pre_social_login called")
        user = sociallogin.user

        if sociallogin.is_existing:
            return

        user_type = request.session.get('user_type', '')
        logger.info(f"User type in pre_social_login: {user_type}")
        if user_type == 'student':
            user.is_student = True
            user.is_instructor = False
        elif user_type == 'instructor':
            user.is_instructor = True
            user.is_student = False

    def save_user(self, request, sociallogin, form=None):
        logger.info("save_user called")
        user = super().save_user(request, sociallogin, form)

        user_type = request.session.get('user_type', '')
        logger.info(f"User type in save_user: {user_type}")
        if user_type == 'student':
            user.is_student = True
            user.is_instructor = False
        elif user_type == 'instructor':
            user.is_instructor = True
            user.is_student = False

        user.save()
        return user
