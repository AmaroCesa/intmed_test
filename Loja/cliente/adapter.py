from allauth.account.adapter import DefaultAccountAdapter
from .models import Cliente

class ClienteAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        """
        saves adapter for new `Cliente` instance using information provided in the
        signup form. 
        """
        from allauth.account.utils import user_field
    
        user = super().save_user(request, user, form, False)
        
        user_field(user, 'address', request.data.get('address', ''))
        user_field(user, 'first_name', request.data.get('first_name', ''))
        user_field(user, 'last_name', request.data.get('last_name', ''))
        user_field(user, 'telefone', request.data.get('telefone', ''))
        user.save()
        return user