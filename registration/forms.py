from django.contrib.auth.forms import UserCreationForm
from .models import User,Coach
from django import forms


class CoachSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    school = forms.CharField(required=True)
    position = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User


    def save(self):
        user = super().save(commit=False)
        user.is_coach = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        coach = Coach.objects.create(user=user)
        coach.school = self.cleaned_data.get('school')
        coach.position = self.cleaned_data.get('position')
        coach.save()
        return user