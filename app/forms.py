from django.contrib.auth.forms import UserCreationForm

from app.models import Login


class TrainerForm(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2', 'name', 'age', 'address', 'email', 'contact_no')


class CustomerForm(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2', 'name', 'age', 'address', 'email', 'contact_no', 'photo')




