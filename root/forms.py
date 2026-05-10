from django import forms
from .models import Registered, Wilaya, Commune
from captcha.fields import CaptchaField



class CaptchaForm(forms.Form):
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['captcha'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "ادخل الرمز",
        })




class RegisteredForm(forms.ModelForm):

    commune = forms.ModelChoiceField(
        queryset=Commune.objects.none(),
        required=True,
        empty_label="اختر البلدية"
    )

    wilaya = forms.ModelChoiceField(
    queryset=Wilaya.objects.all(),
    required=True,
    empty_label="اختر الولاية"
)

    class Meta:
        model = Registered
        fields = [
            'nin',
            'first_name',
            'last_name',
            'birthday',
            'phone',
            'genre',
            'wilaya',
            'commune',
            'status',
            'attestation_file',
        ]

        widgets = {
            'nin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رقم التعريف الوطني','maxlength': '18'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control' ,'placeholder': ' الاسم '}),
            'last_name': forms.TextInput(attrs={'class': 'form-control' ,'placeholder': ' اللقب '}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رقم الهاتف  '}),
            'genre': forms.Select (attrs={'class': 'form-select arbl label-input','placeholder': 'الجنس'} ),
           'attestation_file': forms.FileInput (attrs={'class': 'form-control label-input arbl','name': 'certificate_file','id': 'certificate_file',  'type' : 'file',}),
          

        }
                
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["nin"].required = True
        self.fields["nin"].error_messages["required"] = "هذا الحقل إجباري"

        self.fields["first_name"].required = True
        self.fields["first_name"].error_messages["required"] = "هذا الحقل إجباري"

        self.fields["last_name"].required = True
        self.fields["last_name"].error_messages["required"] = "هذا الحقل إجباري"

        self.fields["birthday"].required = True
        self.fields["birthday"].error_messages["required"] = "هذا الحقل إجباري"

        self.fields["phone"].required = True
        self.fields["phone"].error_messages["required"] = "هذا الحقل إجباري"

        self.fields["genre"].required = True
        self.fields["genre"].error_messages["required"] = "هذا الحقل إجباري"

        if self.data.get('wilaya'):
            try:
                wilaya_id = int(self.data.get('wilaya'))
                self.fields['commune'].queryset = Commune.objects.filter(wilaya_id=wilaya_id)
            except (ValueError, TypeError):
                self.fields['commune'].queryset = Commune.objects.none()

        elif self.instance.pk and self.instance.wilaya:
            self.fields['commune'].queryset = Commune.objects.filter(
                wilaya=self.instance.wilaya
            )


    def clean_nin(self):
        nin = self.cleaned_data.get("nin")

        if nin and len(nin) != 18:
            raise forms.ValidationError("رقم التعريف الوطني يجب أن يكون 18 رقمًا")

        return nin       