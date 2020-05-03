from django import forms
from .models import HelpRequests, HelpRequestsDetail

class ReqEditForm(forms.ModelForm):
    class Meta:
        model = HelpRequests
        fields = [
            'city', 'title', 'expected_ppl_cnt', 'valid_days',
        ]

class ReqDetEditForm(forms.ModelForm):
    description = forms.CharField(required=False, 
                                    widget=forms.Textarea(                                     
                                        attrs={
                                            "placeholder" : "additional text (optional field)",
                                            "rows" : 2,
                                            "cols" : 30,
                                        }
                                    )
                                )
    phone = forms.CharField(required=False)
    Facebook = forms.URLField(required=False)
    instagram = forms.URLField(required=False)
    email = forms.URLField(required=False)

    class Meta:
        model = HelpRequestsDetail
        fields = [
            'description', 'phone', 'Facebook', 'instagram', 'email', 'clinics',
        ]

