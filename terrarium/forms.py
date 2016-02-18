from django import forms

from .models import Terrarium, I2CActor


class TerrariumForm(forms.ModelForm):
    class Meta:
        model = Terrarium
        fields = ('title', 'temperature_min', 'temperature_max', 'sunrise', 'sunset',)


class ActorForm(forms.ModelForm):
    title = forms.TextInput(attrs={'size': 10, 'title': 'Your name',})

    class Meta:
        model = I2CActor
        fields = ('title', 'terrarium', 'chip_address', 'data_address', 'value_address',)

        # apply css class 'form-control' to each form template field for bootstrap style
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',}),
            'terrarium': forms.Select(attrs={'class': 'form-control'}),
            'chip_address': forms.TextInput(attrs={'class': 'form-control',}),
            'data_address': forms.TextInput(attrs={'class': 'form-control',}),
            'value_address': forms.TextInput(attrs={'class': 'form-control',}),
        }
