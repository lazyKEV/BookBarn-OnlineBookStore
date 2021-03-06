from django import forms
from django.contrib.auth.models import User
from BookBarnApp.models import UserProfiles



# User Signup Form Part 1
class UserSignupForm(forms.ModelForm):

    first_name = forms.CharField(
            required=True, 
            max_length=50,
            label='', 
            widget=forms.TextInput(
                    attrs={
                        "class":"form-control", 
                        "placeholder":"First Name", 
                        "id":"id_firstName",
                        }
                    )
            )

    last_name = forms.CharField(
            required=True,
            max_length=50,
            label='',
            widget=forms.TextInput(
                    attrs={
                        "class":"form-control", 
                        "placeholder":"Last Name", 
                        "id":"id_lastName",
                        }
                    )
            )

    username = forms.CharField(
            required=True,
            min_length=6,
            max_length=50,
            label='',
            widget=forms.TextInput(
                    attrs={
                        "class":"form-control", 
                        "placeholder":"Username", 
                        "id":"id_userName",
                        }
                    )
            )

    email = forms.EmailField(
            required=True,
            label='',
            widget=forms.EmailInput(
                    attrs={
                        "class":"form-control",
                        "placeholder":"Email",
                        "id":"id_email",
                        }
                    )
            )

    password = forms.CharField(
            label='',
            required=True,
            min_length=6,
            max_length=50,
            widget=forms.PasswordInput(
                    attrs={
                        "class":"form-control",
                        "placeholder":"Password",
                        "id":"id_password",
                        }
                    )
            )

    password2 = forms.CharField(
            label='',
            required=True,
            min_length=6,
            max_length=50,
            widget=forms.PasswordInput(
                    attrs={
                        "class":"form-control",
                        "placeholder":"Re-enter Password",
                        "id":"id_password2",
                        }
                    )
            )

    def clean_email(self):
        email=self.cleaned_data.get("email")
        qs=User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email already registered.")
        else:
            return email

    def clean(self):
        data=self.cleaned_data
        password=self.cleaned_data.get("password")
        password2=self.cleaned_data.get("password2")

        if password2 != password:
            raise forms.ValidationError("Passwords must match.")
        else:
            return data

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')



# User Signup Form Part 2
class UserProfileSignupForm(forms.ModelForm):

    phoneNumber = forms.CharField(
            required=True,
            label='',
            min_length=10,
            max_length=10,
            widget=forms.TextInput(
                    attrs={
                        "class":"form-control", 
                        "placeholder":"Phone Number", 
                        "id":"id_phoneNumber",
                        'oninput': 'onlyNumber(id)',
                        }
                    )
            )

    address1 = forms.CharField(
            required=True,
            label='',
            max_length=50,
            widget=forms.TextInput(
                    attrs={
                        "class":"form-control", 
                        "placeholder":"Address Line 1", 
                        "id":"id_address1",
                        }
                    )
            )

    address2 = forms.CharField(
            required=False,
            label='',
            max_length=50,
            widget=forms.TextInput(
                    attrs={
                        "class":"form-control", 
                        "placeholder":"Address Line 2", 
                        "id":"id_address2",
                        }
                    )
            )

    city = forms.CharField(
            required=True, 
            label='',
            max_length=50,
            widget=forms.TextInput(
                    attrs={
                        "class":"form-control", 
                        "placeholder":"City", 
                        "id":"id_city",
                        }
                    )
            )

    state = forms.CharField(
            required=True,
            label='',
            max_length=50,
            widget=forms.TextInput(
                    attrs={
                        "class":"form-control", 
                        "placeholder":"State", 
                        "id":"id_state",
                        }
                    )
            )

    # pinCode = forms.CharField(
    #         required=True, 
    #         label='', 
    #         min_length=6, 
    #         max_length=6, 
    #         widget=forms.TextInput(
    #                 attrs={
    #                     "class":"form-control", 
    #                     "placeholder":"PIN Code", 
    #                     "id":"id_pincode",
    #                     }
    #                 )
    #         )

    pinCode = forms.CharField(
            required=True, 
            label='', 
            min_length=6, 
            max_length=6, 
            widget=forms.TextInput(
                    attrs={
                        "class":"form-control", 
                        "placeholder":"PIN Code", 
                        "id":"id_pincode",
                        'pattern':'[0-9]+',
                        'autocomplete': 'off',
                        'oninput': 'onlyNumber(id)'
                        }
                    )
            )

    class Meta:
        model = UserProfiles
        fields = ('address1', 'address2', 'city', 'state', 'pinCode', 'phoneNumber')




# User Login Form
class LoginForm(forms.ModelForm):
    username = forms.CharField(
            required=True, 
            label='', 
            min_length=6, 
            max_length=50, 
            widget=forms.TextInput(
                    attrs={
                        "class":"form-control", 
                        "placeholder":"Username", 
                        "id":"id_userName",
                        }
                    )
            )

    password = forms.CharField(
            label='',
            required=True, 
            min_length=6, 
            max_length=50,
            widget=forms.PasswordInput( 
                    attrs={
                        "class":"form-control password", 
                        "placeholder":"Password", 
                        "id":"id_password",
                        } 
                    )
            )

    class Meta:
        model = User
        fields = ('username','password')