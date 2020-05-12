from django import forms
from .models import HelpRequests, HelpRequestsDetail, Cities, Clinics

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

class CityForm(forms.Form): 
    city = forms.ModelChoiceField(queryset=Cities.objects.all(), label_suffix='*')

class ClinicForm(forms.Form): 
    clinic = forms.ModelChoiceField(queryset=Clinics.objects.all(), required=False, empty_label="(optional)")

class RawCreateForm(forms.Form):
    title = forms.SlugField( label_suffix='*')
    expected_ppl_cnt = forms.IntegerField(initial=1, label_suffix='*')
    valid_days = forms.IntegerField(initial=7, label_suffix='*')

    description = forms.CharField(required=False, 
                                    widget=forms.Textarea(                                     
                                        attrs={
                                            "placeholder" : "additional text (optional field)",
                                            "rows" : 2,
                                            "cols" : 30,
                                        }
                                    )
                                )
    phone = forms.CharField(max_length=20, empty_value =None, required=False)
    Facebook = forms.URLField(empty_value =None, required=False)
    instagram = forms.URLField(empty_value =None, required=False)
    email = forms.URLField(empty_value =None, required=False)
