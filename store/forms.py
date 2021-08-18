from django import forms
from django.db.models import fields
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname', ]

        def signup(self, request, user):
            user.nickname = self.clean_data['nickname']
            user.save()
