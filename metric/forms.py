from django import forms


class LengthForm(forms.Form):

    LENGTH_VALUES = (
        ('mm', 'Millimeters(mm)'),
        ('cm', 'Centimeters(cm)'),
        ('dm', 'Decimeters(dm)'),
        ('m', 'Meters(m)'),
        ('dam', 'Decameters(dam)'),
        ('hm', 'Hectometers(hm)'),
        ('km', 'Kilometers(km)'),
        ('in', 'Inch(in)'),
        ('ft', 'Foot(ft)'),
        ('yd', 'Yard(yd)'),
        ('mi', 'Miles(mi)'),
    )

    user_input = forms.IntegerField(label='input',
                                    required=True,
                                    initial=0,
                                    localize=False,
                                    widget=forms.NumberInput(attrs={'class': 'form-control user-input'}))
    user_selection = forms.ChoiceField(choices=LENGTH_VALUES,
                                       label='From',
                                       required=False,
                                       widget=forms.Select(attrs={'class': 'form-select form-select-sm'}))
    length_selection = forms.ChoiceField(choices=LENGTH_VALUES,
                                         label='To',
                                         required=False,
                                         widget=forms.Select(attrs={'class': 'form-select form-select-sm'}))


class TemperatureForm(forms.Form):

    TEMPERATURE_VALUES = (
        ('c', 'Celsius'),
        ('k', 'Kelvin'),
        ('f', 'Fahrenheit'),
    )

    user_input = forms.IntegerField(label='input',
                                    required=True,
                                    initial=0,
                                    localize=False,
                                    widget=forms.NumberInput(attrs={'class': 'form-control user-input'}))
    user_selection = forms.ChoiceField(choices=TEMPERATURE_VALUES,
                                       label='From',
                                       required=False,
                                       widget=forms.Select(attrs={'class': 'form-select form-select-sm'}))
    temperature_selection = forms.ChoiceField(choices=TEMPERATURE_VALUES,
                                              label='To',
                                              required=False,
                                              widget=forms.Select(attrs={'class': 'form-select form-select-sm'}))


class WeightForm(forms.Form):
    
    WEIGHT_VALUES = (
        ('kg', 'Kilogram(kg)'),
        ('g', 'Gram(g)'),
        ('mg', 'Milligram(mg)'),
        ('mcg', 'Microgram(µg)'),
        ('t', 'Metric Ton(T)'),
        ('lt', 'Long Ton(lt)'),
        ('tn', 'Short Ton(tn)'),
        ('st', 'Stone(st)'),
        ('lb', 'Pound(lb)'),
        ('oz', 'Ounce(oz)'),
    )

    user_input = forms.IntegerField(label='input',
                                    required=True,
                                    initial=0,
                                    localize=False,
                                    widget=forms.NumberInput(attrs={'class': 'form-control user-input'}))
    user_selection = forms.ChoiceField(choices=WEIGHT_VALUES,
                                       label='From',
                                       required=False,
                                       widget=forms.Select(attrs={'class': 'form-select form-select-sm'}))
    weight_selection = forms.ChoiceField(choices=WEIGHT_VALUES,
                                         label='To',
                                         required=False,
                                         widget=forms.Select(attrs={'class': 'form-select form-select-sm'}))
