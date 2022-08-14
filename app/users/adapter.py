from allauth.account.adapter import DefaultAccountAdapter
from django.http import HttpRequest


class AccountAdapter(DefaultAccountAdapter):
    redirect_url = "/contact/"

    def get_login_redirect_url(self, request: HttpRequest):
        return self.redirect_url
    
    def get_signup_redirect_url(self, request: HttpRequest):
        return self.redirect_url
    
