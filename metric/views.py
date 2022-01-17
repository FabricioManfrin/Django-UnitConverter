from django.shortcuts import render
from .forms import LengthForm, TemperatureForm, WeightForm
from .functions import length_conversion, formula_display_length, temperature_conversion, formula_display_temperature

# Conversion Function


def length_converter(request):
    form = LengthForm()
    if request.method == 'POST':
        form = LengthForm(request.POST)
        if form.is_valid():

            # Get Values
            user_input = form.cleaned_data['user_input']
            user_selection = form['user_selection'].value()
            length_selection = form['length_selection'].value()
            result = length_conversion(input=user_input, user_metric=user_selection, converter=length_selection)
            formula = formula_display_length(user_metric=user_selection, converter=length_selection)
            # Insert Values
            context = {'form': form, 'result': result, 'formula': formula}
            return render(request, 'metric/length-converter.html', context)

    context = {
        'form': form,
    }
    return render(request, 'metric/length-converter.html', context)


def temperature_converter(request):
    form = TemperatureForm()
    if request.method == 'POST':
        form = TemperatureForm(request.POST)
        if form.is_valid():

            # Get Values
            user_input = form.cleaned_data['user_input']
            user_selection = form['user_selection'].value()
            temperature_selection = form['temperature_selection'].value()
            result = temperature_conversion(user_input, user_selection, temperature_selection)
            formula = formula_display_temperature(user_selection, temperature_selection)
            # Insert Values
            context = {'form': form, 'result': result, 'formula': formula}
            return render(request, 'metric/temperature-converter.html', context)

    context = {
        'form': form,
    }
    return render(request, 'metric/temperature-converter.html', context)


# def weight_converter(request):
#     form = WeightForm()
#     if request.method == 'POST':
#         form = WeightForm(request.POST)
#         if form.is_valid():

#             # Get Values
#             user_input = form.cleaned_data['user_input']
#             user_selection = form['user_selection'].value()
#             weight_selection = form['temperature_selection'].value()
#             result = weight_conversion(user_input, user_selection, weight_selection)
#             formula = formula_display_weight(user_selection, weight_selection)
#             # Insert Values
#             context = {'form': form, 'result': result, 'formula': formula}
#             return render(request, 'metric/weight-converter.html', context)

#     context = {
#         'form': form,
#     }
#     return render(request, 'metric/weight-converter.html', context)