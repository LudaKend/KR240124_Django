from django import forms
from client.models import Client


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        #fields = '__all__'
        exclude = ('user_email',)

    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user_email', None) # Извлекаем пользователя из аргументов формы
    #     #user = self.request.user
    #     print(user)
    #     super(ClientForm, self).__init__(*args, **kwargs)

        # Ограничиваем queryset для выбора клиентов только теми, которых создал текущий пользователь
        #self.fields['clients'].queryset = Client.objects.filter(user=user)
