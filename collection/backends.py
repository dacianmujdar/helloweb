from registration.backends.simple.views import RegistrationView


class MyRegistrationView(RegistrationView):
    def get_success_url(self, request=None, user=None):
        return 'registration_create_article'

