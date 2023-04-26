from django import forms
from django.contrib.auth import authenticate
from main_app.models import Post, Comment


class AuthenticationForm(forms.Form):
    username = forms.CharField(label='Login', max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                raise forms.ValidationError('Incorrect credentials')


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__' #['slug', 'title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 68, 'rows': 18}),
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'author']


# class CreateUserForm(forms.Form):
#     username = forms.CharField(label='Username', max_length=100)
#     password_1 = forms.CharField(label='Password', widget=forms.PasswordInput(render_value=False))
#     password_2 = forms.CharField(label='Re-type', widget=forms.PasswordInput(render_value=False))
#     email = forms.EmailField(label='email', max_length=100)
#     first_name = forms.CharField(label='Firstname', max_length=100)
#     last_name = forms.CharField(label='Lastname', max_length=100)
#
#     def clean_password(self):
#         if 'password_1' in self.cleaned_data and 'password_2' in self.cleaned_data:
#             if self.cleaned_data['password_1'] != self.cleaned_data['password_2']:
#                 e = forms.ValidationError('You must type the same password each time.')
#                 self._errors['password_2'] = e.messages
#                 raise e
#         return self.cleaned_data
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user

