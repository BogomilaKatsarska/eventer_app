from django import forms
from eventer_app.web.models import Profile, Event


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'profile_picture', 'password',)
        widgets = {
            'password': forms.PasswordInput(),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Event.objects.all().delete()
            self.instance.delete()
        else:
            return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class EditEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class DeleteEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'