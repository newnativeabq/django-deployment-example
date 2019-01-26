from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserSignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['username.label'] = 'Display Name' #Customizing labels here isn't workign this way.  Can do in html, or figure this out.
        # self.fields['email.label'] = 'Email Address'