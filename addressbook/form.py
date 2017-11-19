from django import forms

class AddressForm(forms.Form):

    name = forms.CharField(max_length=40,
            widget = forms.TextInput(
                attrs = {
                    "placeholder": "Enter name"
                }
            )
        )

    email = forms.EmailField(max_length=60,
             widget = forms.TextInput(
                attrs = {
                    "placeholder": "Enter email"
                }
            )
         )

    def clean(self):
        cleaned_data = super(AddressForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        if not name and not email:
            raise forms.ValidationError('All fields are required!')

