from django import forms


class StudentForm(forms.Form):
    email = forms.EmailField(
        max_length=256,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
        required=True,
        error_messages={
            'required': 'Email harus diisi'
        }
    )
    name = forms.CharField(max_length=256, error_messages={'required': 'Email harus diisi'})
