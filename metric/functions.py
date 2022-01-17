# Length Conversions
def length_conversion(input, user_metric, converter):

    # Millimeters(mm)
    if user_metric == 'mm' and converter == 'mm':
        return input
    elif user_metric == 'mm' and converter == 'cm':
        return input / 10
    elif user_metric == 'mm' and converter == 'dm':
        return input / 100
    elif user_metric == 'mm' and converter == 'm':
        return input / 1000
    elif user_metric == 'mm' and converter == 'dam':
        return input / 10000
    elif user_metric == 'mm' and converter == 'hm':
        return input / 100000
    elif user_metric == 'mm' and converter == 'km':
        return input / 1000000
    elif user_metric == 'mm' and converter == 'in':
        return input * 0.0393701
    elif user_metric == 'mm' and converter == 'ft':
        return input * 0.00328084
    elif user_metric == 'mm' and converter == 'yd':
        return input * 0.00109361
    elif user_metric == 'mm' and converter == 'mi':
        return input * (6.21371 * (10**-7))

    # Centimeters(cm)
    if user_metric == 'cm' and converter == 'mm':
        return input * 10
    elif user_metric == 'cm' and converter == 'cm':
        return input
    elif user_metric == 'cm' and converter == 'dm':
        return input / 10
    elif user_metric == 'cm' and converter == 'm':
        return input / 100
    elif user_metric == 'cm' and converter == 'dam':
        return input / 1000
    elif user_metric == 'cm' and converter == 'hm':
        return input / 10000
    elif user_metric == 'cm' and converter == 'km':
        return input / 100000
    elif user_metric == 'cm' and converter == 'in':
        return input * 0.393701
    elif user_metric == 'cm' and converter == 'ft':
        return input * 0.0328084
    elif user_metric == 'cm' and converter == 'yd':
        return input * 0.0109361
    elif user_metric == 'cm' and converter == 'mi':
        return input * 0.00000621371

    # Decimeters(dm)
    if user_metric == 'dm' and converter == 'mm':
        return input * 100
    elif user_metric == 'dm' and converter == 'cm':
        return input * 10
    elif user_metric == 'dm' and converter == 'dm':
        return input
    elif user_metric == 'dm' and converter == 'm':
        return input / 10
    elif user_metric == 'dm' and converter == 'dam':
        return input / 100
    elif user_metric == 'dm' and converter == 'hm':
        return input / 1000
    elif user_metric == 'dm' and converter == 'km':
        return input / 10000
    elif user_metric == 'dm' and converter == 'in':
        return input * 3.93701
    elif user_metric == 'dm' and converter == 'ft':
        return input * 0.328084
    elif user_metric == 'dm' and converter == 'yd':
        return input * 0.109361
    elif user_metric == 'dm' and converter == 'mi':
        return input * 0.0000621371

    # Meters(m)
    if user_metric == 'm' and converter == 'mm':
        return input * 1000
    elif user_metric == 'm' and converter == 'cm':
        return input * 100
    elif user_metric == 'm' and converter == 'dm':
        return input * 10
    elif user_metric == 'm' and converter == 'm':
        return input
    elif user_metric == 'm' and converter == 'dam':
        return input / 10
    elif user_metric == 'm' and converter == 'hm':
        return input / 100
    elif user_metric == 'm' and converter == 'km':
        return input / 1000
    elif user_metric == 'm' and converter == 'in':
        return input * 39.3701
    elif user_metric == 'm' and converter == 'ft':
        return input * 3.28084
    elif user_metric == 'm' and converter == 'yd':
        return input * 1.09361
    elif user_metric == 'm' and converter == 'mi':
        return input * 0.000621371

    # Decameters(dam)
    if user_metric == 'dam' and converter == 'mm':
        return input * 10000
    elif user_metric == 'dam' and converter == 'cm':
        return input * 1000
    elif user_metric == 'dam' and converter == 'dm':
        return input * 100
    elif user_metric == 'dam' and converter == 'm':
        return input * 10
    elif user_metric == 'dam' and converter == 'dam':
        return input
    elif user_metric == 'dam' and converter == 'hm':
        return input / 10
    elif user_metric == 'dam' and converter == 'km':
        return input / 100
    elif user_metric == 'dam' and converter == 'in':
        return input * 393.701
    elif user_metric == 'dam' and converter == 'ft':
        return input * 32.8084
    elif user_metric == 'dam' and converter == 'yd':
        return input * 10.9361
    elif user_metric == 'dam' and converter == 'mi':
        return input * 0.00621371

    # Hectometers(hm)
    if user_metric == 'hm' and converter == 'mm':
        return input * 100000
    elif user_metric == 'hm' and converter == 'cm':
        return input * 10000
    elif user_metric == 'hm' and converter == 'dm':
        return input * 1000
    elif user_metric == 'hm' and converter == 'm':
        return input * 100
    elif user_metric == 'hm' and converter == 'dam':
        return input * 10
    elif user_metric == 'hm' and converter == 'hm':
        return input
    elif user_metric == 'hm' and converter == 'km':
        return input / 10
    elif user_metric == 'hm' and converter == 'in':
        return input * 3937.01
    elif user_metric == 'hm' and converter == 'ft':
        return input * 328.084
    elif user_metric == 'hm' and converter == 'yd':
        return input * 109.361
    elif user_metric == 'hm' and converter == 'mi':
        return input * 0.0621371

    # Kilometers(km)
    if user_metric == 'km' and converter == 'mm':
        return input * 1000000
    elif user_metric == 'km' and converter == 'cm':
        return input * 100000
    elif user_metric == 'km' and converter == 'dm':
        return input * 10000
    elif user_metric == 'km' and converter == 'm':
        return input * 1000
    elif user_metric == 'km' and converter == 'dam':
        return input * 100
    elif user_metric == 'km' and converter == 'hm':
        return input * 10
    elif user_metric == 'km' and converter == 'km':
        return input
    elif user_metric == 'km' and converter == 'in':
        return input * 39370.1
    elif user_metric == 'km' and converter == 'ft':
        return input * 3280.84
    elif user_metric == 'km' and converter == 'yd':
        return input * 1093.61
    elif user_metric == 'km' and converter == 'mi':
        return input * 0.621371

    # Inch(in)
    if user_metric == 'in' and converter == 'mm':
        return input * 25.4
    elif user_metric == 'in' and converter == 'cm':
        return input * 2.54
    elif user_metric == 'in' and converter == 'dm':
        return input * 0.254
    elif user_metric == 'in' and converter == 'm':
        return input * 0.0254
    elif user_metric == 'in' and converter == 'dam':
        return input * 0.00254
    elif user_metric == 'in' and converter == 'hm':
        return input * 0.000254
    elif user_metric == 'in' and converter == 'km':
        return input * 0.0000254
    elif user_metric == 'in' and converter == 'in':
        return input
    elif user_metric == 'in' and converter == 'ft':
        return input / 12
    elif user_metric == 'in' and converter == 'yd':
        return input / 36
    elif user_metric == 'in' and converter == 'mi':
        return input / 63360

    # Foot(ft)
    if user_metric == 'ft' and converter == 'mm':
        return input * 304.8
    elif user_metric == 'ft' and converter == 'cm':
        return input * 30.48
    elif user_metric == 'ft' and converter == 'dm':
        return input * 3.048
    elif user_metric == 'ft' and converter == 'm':
        return input * 0.3048
    elif user_metric == 'ft' and converter == 'm':
        return input * 0.03048
    elif user_metric == 'ft' and converter == 'dam':
        return input * 0.003048
    elif user_metric == 'ft' and converter == 'hm':
        return input * 0.0003048
    elif user_metric == 'ft' and converter == 'km':
        return input * 0.00003048
    elif user_metric == 'ft' and converter == 'in':
        return input * 12
    elif user_metric == 'ft' and converter == 'ft':
        return input
    elif user_metric == 'ft' and converter == 'yd':
        return input * (1 / 3)
    elif user_metric == 'ft' and converter == 'mi':
        return input / 5280

    # Yard(yd)
    if user_metric == 'yd' and converter == 'mm':
        return input * 914.4
    elif user_metric == 'yd' and converter == 'cm':
        return input * 91.44
    elif user_metric == 'yd' and converter == 'dm':
        return input * 9.144
    elif user_metric == 'yd' and converter == 'm':
        return input * 0.9144
    elif user_metric == 'yd' and converter == 'dam':
        return input * 0.09144
    elif user_metric == 'yd' and converter == 'hm':
        return input * 0.009144
    elif user_metric == 'yd' and converter == 'km':
        return input * 0.0009144
    elif user_metric == 'yd' and converter == 'in':
        return input * 36
    elif user_metric == 'yd' and converter == 'ft':
        return input * 3
    elif user_metric == 'yd' and converter == 'yd':
        return input
    elif user_metric == 'yd' and converter == 'mi':
        return input / 1760

    # Miles(mi)
    if user_metric == 'mi' and converter == 'mm':
        return input * 1609340
    elif user_metric == 'mi' and converter == 'cm':
        return input * 160934
    elif user_metric == 'mi' and converter == 'dm':
        return input * 16093.4
    elif user_metric == 'mi' and converter == 'm':
        return input * 1609.34
    elif user_metric == 'mi' and converter == 'dam':
        return input * 160.934
    elif user_metric == 'mi' and converter == 'hm':
        return input * 16.0934
    elif user_metric == 'mi' and converter == 'km':
        return input * 1.60934
    elif user_metric == 'mi' and converter == 'in':
        return input * 63360
    elif user_metric == 'mi' and converter == 'ft':
        return input * 5280
    elif user_metric == 'mi' and converter == 'yd':
        return input * 1760
    elif user_metric == 'mi' and converter == 'mi':
        return input


def formula_display_length(user_metric, converter):

    # Millimeters(mm)
    if user_metric == 'mm' and converter == 'mm':
        return 'Multiply the value by 1'
    elif user_metric == 'mm' and converter == 'cm':
        return 'Divide the value by 10'
    elif user_metric == 'mm' and converter == 'dm':
        return 'Divide the value by 100'
    elif user_metric == 'mm' and converter == 'm':
        return 'Divide the value by 1000'
    elif user_metric == 'mm' and converter == 'dam':
        return 'Divide the value by 10000'
    elif user_metric == 'mm' and converter == 'hm':
        return 'Divide the value by 1e+5'
    elif user_metric == 'mm' and converter == 'km':
        return 'Divide the value by 1e+6'
    elif user_metric == 'mm' and converter == 'in':
        return 'Multiply the value by 0.0393701'
    elif user_metric == 'mm' and converter == 'ft':
        return 'Multiply the value by 0.00328084'
    elif user_metric == 'mm' and converter == 'yd':
        return 'Multiply the value by 0.00109361'
    elif user_metric == 'mm' and converter == 'mi':
        return 'Multiply the value by 6.21371\u00d710^-7'

    # Centimeters(cm)
    if user_metric == 'cm' and converter == 'mm':
        return 'Multiply the value by 10'
    elif user_metric == 'cm' and converter == 'cm':
        return 'Multiply the value by 1'
    elif user_metric == 'cm' and converter == 'dm':
        return 'Divide the value by 10'
    elif user_metric == 'cm' and converter == 'm':
        return 'Divide the value by 100'
    elif user_metric == 'cm' and converter == 'dam':
        return 'Divide the value by 1000'
    elif user_metric == 'cm' and converter == 'hm':
        return 'Divide the value by 10000'
    elif user_metric == 'cm' and converter == 'km':
        return 'Divide the value by 1e+5'
    elif user_metric == 'cm' and converter == 'in':
        return 'Multiply the value by 0.393701'
    elif user_metric == 'cm' and converter == 'ft':
        return 'Multiply the value by 0.0328084'
    elif user_metric == 'cm' and converter == 'yd':
        return 'Multiply the value by 0.0109361'
    elif user_metric == 'cm' and converter == 'mi':
        return 'Multiply the value by 0.00000621371'

    # Decimeters(dm)
    if user_metric == 'dm' and converter == 'mm':
        return 'Multiply the value by 100'
    elif user_metric == 'dm' and converter == 'cm':
        return 'Multiply the value by 10'
    elif user_metric == 'dm' and converter == 'dm':
        return 'Multiply the value by 1'
    elif user_metric == 'dm' and converter == 'm':
        return 'Divide the value by 10'
    elif user_metric == 'dm' and converter == 'dam':
        return 'Divide the value by 100'
    elif user_metric == 'dm' and converter == 'hm':
        return 'Divide the value by 1000'
    elif user_metric == 'dm' and converter == 'km':
        return 'Divide the value by 1e+5'
    elif user_metric == 'dm' and converter == 'in':
        return 'Multiply the value by 3.93701'
    elif user_metric == 'dm' and converter == 'ft':
        return 'Multiply the value by 0.328084'
    elif user_metric == 'dm' and converter == 'yd':
        return 'Multiply the value by 0.109361'
    elif user_metric == 'dm' and converter == 'mi':
        return 'Multiply the value by 0.0000621371'

    # Meters(m)
    if user_metric == 'm' and converter == 'mm':
        return 'Multiply the value by 1000'
    elif user_metric == 'm' and converter == 'cm':
        return 'Multiply the value by 100'
    elif user_metric == 'm' and converter == 'dm':
        return 'Multiply the value by 10'
    elif user_metric == 'm' and converter == 'm':
        return 'Multiply the value by 1'
    elif user_metric == 'm' and converter == 'dam':
        return 'Divide the value by 10'
    elif user_metric == 'm' and converter == 'hm':
        return 'Divide the value by 100'
    elif user_metric == 'm' and converter == 'km':
        return 'Divide the value by 1000'
    elif user_metric == 'm' and converter == 'in':
        return 'Multiply the value by 39.3701'
    elif user_metric == 'm' and converter == 'ft':
        return 'Multiply the value by 3.28084'
    elif user_metric == 'm' and converter == 'yd':
        return 'Multiply the value by 1.09361'
    elif user_metric == 'm' and converter == 'mi':
        return 'Multiply the value by 0.000621371'

    # Decameters(dam)
    if user_metric == 'dam' and converter == 'mm':
        return 'Multiply the value by 10000'
    elif user_metric == 'dam' and converter == 'cm':
        return 'Multiply the value by 1000'
    elif user_metric == 'dam' and converter == 'dm':
        return 'Multiply the value by 100'
    elif user_metric == 'dam' and converter == 'm':
        return 'Multiply the value by 10'
    elif user_metric == 'dam' and converter == 'dam':
        return 'Multiply the value by 1'
    elif user_metric == 'dam' and converter == 'hm':
        return 'Divide the value by 10'
    elif user_metric == 'dam' and converter == 'km':
        return 'Divide the value by 100'
    elif user_metric == 'dam' and converter == 'in':
        return 'Multiply the value by 393.701'
    elif user_metric == 'dam' and converter == 'ft':
        return 'Multiply the value by 32.8084'
    elif user_metric == 'dam' and converter == 'yd':
        return 'Multiply the value by 10.9361'
    elif user_metric == 'dam' and converter == 'mi':
        return 'Multiply the value by 0.00621371'

    # Hectometers(hm)
    if user_metric == 'hm' and converter == 'mm':
        return 'Multiply the value by 1e+5'
    elif user_metric == 'hm' and converter == 'cm':
        return 'Multiply the value by 10000'
    elif user_metric == 'hm' and converter == 'dm':
        return 'Multiply the value by 1000'
    elif user_metric == 'hm' and converter == 'm':
        return 'Multiply the value by 100'
    elif user_metric == 'hm' and converter == 'dam':
        return 'Multiply the value by 10'
    elif user_metric == 'hm' and converter == 'hm':
        return 'Multiply the value by 1'
    elif user_metric == 'hm' and converter == 'km':
        return 'Divide the value by 10'
    elif user_metric == 'hm' and converter == 'in':
        return 'Multiply the value by 3937.01'
    elif user_metric == 'hm' and converter == 'ft':
        return 'Multiply the value by 328.084'
    elif user_metric == 'hm' and converter == 'yd':
        return 'Multiply the value by 109.361'
    elif user_metric == 'hm' and converter == 'mi':
        return 'Multiply the value by 0.0621371'

    # Kilometers(km)
    if user_metric == 'km' and converter == 'mm':
        return 'Multiply the value by 1e+6'
    elif user_metric == 'km' and converter == 'cm':
        return 'Multiply the value by 1e+5'
    elif user_metric == 'km' and converter == 'dm':
        return 'Multiply the value by 10000'
    elif user_metric == 'km' and converter == 'm':
        return 'Multiply the value by 1000'
    elif user_metric == 'km' and converter == 'dam':
        return 'Multiply the value by 100'
    elif user_metric == 'km' and converter == 'hm':
        return 'Multiply the value by 10'
    elif user_metric == 'km' and converter == 'km':
        return 'Multiply the value by 1'
    elif user_metric == 'km' and converter == 'in':
        return 'Multiply the value by 39370.1'
    elif user_metric == 'km' and converter == 'ft':
        return 'Multiply the value by 3280.84'
    elif user_metric == 'km' and converter == 'yd':
        return 'Multiply the value by 1093.61'
    elif user_metric == 'km' and converter == 'mi':
        return 'Multiply the value by 0.621371'

    # Inch(in)
    if user_metric == 'in' and converter == 'mm':
        return 'Multiply the value by 25.4'
    elif user_metric == 'in' and converter == 'cm':
        return 'Multiply the value by 2.54'
    elif user_metric == 'in' and converter == 'dm':
        return 'Multiply the value by 0.254'
    elif user_metric == 'in' and converter == 'm':
        return 'Multiply the value by 0.0254'
    elif user_metric == 'in' and converter == 'dam':
        return 'Multiply the value by 0.00254'
    elif user_metric == 'in' and converter == 'hm':
        return 'Multiply the value by 0.000254'
    elif user_metric == 'in' and converter == 'km':
        return 'Multiply the value by 0.0000254'
    elif user_metric == 'in' and converter == 'in':
        return 'Multiply the value by 1'
    elif user_metric == 'in' and converter == 'ft':
        return 'Divide the value by 12'
    elif user_metric == 'in' and converter == 'yd':
        return 'Divide the value by 36'
    elif user_metric == 'in' and converter == 'mi':
        return 'Divide the value by 63360'

    # Foot(ft)
    if user_metric == 'ft' and converter == 'mm':
        return 'Multiply the value by 304.8'
    elif user_metric == 'ft' and converter == 'cm':
        return 'Multiply the value by 30.48'
    elif user_metric == 'ft' and converter == 'dm':
        return 'Multiply the value by 3.048'
    elif user_metric == 'ft' and converter == 'm':
        return 'Multiply the value by 0.3048'
    elif user_metric == 'ft' and converter == 'm':
        return 'Multiply the value by 0.03048'
    elif user_metric == 'ft' and converter == 'dam':
        return 'Multiply the value by 0.003048'
    elif user_metric == 'ft' and converter == 'hm':
        return 'Multiply the value by 0.0003048'
    elif user_metric == 'ft' and converter == 'km':
        return 'Multiply the value by 0.00003048'
    elif user_metric == 'ft' and converter == 'in':
        return 'Multiply the value by 12'
    elif user_metric == 'ft' and converter == 'ft':
        return 'Multiply the value by 1'
    elif user_metric == 'ft' and converter == 'yd':
        return 'Divide the value by 3'
    elif user_metric == 'ft' and converter == 'mi':
        return 'Divide the value by 5280'

    # Yard(yd)
    if user_metric == 'yd' and converter == 'mm':
        return 'Multiply the value by 914.4'
    elif user_metric == 'yd' and converter == 'cm':
        return 'Multiply the value by 91.44'
    elif user_metric == 'yd' and converter == 'dm':
        return 'Multiply the value by 9.144'
    elif user_metric == 'yd' and converter == 'm':
        return 'Multiply the value by 0.9144'
    elif user_metric == 'yd' and converter == 'dam':
        return 'Multiply the value by 0.09144'
    elif user_metric == 'yd' and converter == 'hm':
        return 'Multiply the value by 0.009144'
    elif user_metric == 'yd' and converter == 'km':
        return 'Multiply the value by 0.0009144'
    elif user_metric == 'yd' and converter == 'in':
        return 'Multiply the value by 36'
    elif user_metric == 'yd' and converter == 'ft':
        return 'Multiply the value by 3'
    elif user_metric == 'yd' and converter == 'yd':
        return 'Multiply the value by 1'
    elif user_metric == 'yd' and converter == 'mi':
        return 'Divide the value by 1760'

    # Miles(mi)
    if user_metric == 'mi' and converter == 'mm':
        return 'Multiply the value by 1609340'
    elif user_metric == 'mi' and converter == 'cm':
        return 'Multiply the value by 160934'
    elif user_metric == 'mi' and converter == 'dm':
        return 'Multiply the value by 16093.4'
    elif user_metric == 'mi' and converter == 'm':
        return 'Multiply the value by 1609.34'
    elif user_metric == 'mi' and converter == 'dam':
        return 'Multiply the value by 160.934'
    elif user_metric == 'mi' and converter == 'hm':
        return 'Multiply the value by 16.0934'
    elif user_metric == 'mi' and converter == 'km':
        return 'Multiply the value by 1.60934'
    elif user_metric == 'mi' and converter == 'in':
        return 'Multiply the value by 63360'
    elif user_metric == 'mi' and converter == 'ft':
        return 'Multiply the value by 5280'
    elif user_metric == 'mi' and converter == 'yd':
        return 'Multiply the value by 1760'
    elif user_metric == 'mi' and converter == 'mi':
        return 'Multiply the value by 1'


# Temperature Conversions
def temperature_conversion(input, user_selection, conversion):

    # Celsius
    if user_selection == 'c' and conversion == 'c':
        return input
    elif user_selection == 'c' and conversion == 'f':
        return (input * 9 / 5) + 32
    elif user_selection == 'c' and conversion == 'k':
        return input + 273.15

    # Kelvin
    if user_selection == 'k' and conversion == 'c':
        return input - 273.15
    elif user_selection == 'k' and conversion == 'f':
        return (input - 273.15) * 9 / 5 + 32
    elif user_selection == 'k' and conversion == 'k':
        return input

    # Fahrenheit
    if user_selection == 'f' and conversion == 'c':
        return (input - 32) * 5 / 9
    elif user_selection == 'f' and conversion == 'f':
        return input
    elif user_selection == 'f' and conversion == 'k':
        return (input - 32) * 5 / 9 + 273.15


def formula_display_temperature(user_selection, converter):

    # Celsius
    if user_selection == 'c' and converter == 'c':
        return 'Multiply the value by 1'
    elif user_selection == 'c' and converter == 'f':
        return '(a°C \u00d7 9/5) + 32 = b°F'
    elif user_selection == 'c' and converter == 'k':
        return 'a°C + 273.15 = bK'

    # Kelvin
    if user_selection == 'k' and converter == 'c':
        return 'aK - 273.15 = b°C'
    elif user_selection == 'k' and converter == 'f':
        return '(aK - 273.15) \u00d7 9/5 + 32 = b°F'
    elif user_selection == 'k' and converter == 'k':
        return 'Multiply the value by 1'

    # Fahrenheit
    if user_selection == 'f' and converter == 'c':
        return '(a°F - 32) \u00d7 5/9 = b°C'
    elif user_selection == 'f' and converter == 'f':
        return 'Multiply the value by 1'
    elif user_selection == 'f' and converter == 'k':
        return '(a°F - 32) \u00d7 5/9 + 273.15 = b°C'


def formula_display_weight(user_selection, converter):
    if user_selection == 'kg' and converter == 'kg':
        return 'Multiply the value by 1'
    elif user_selection == 'kg' and converter == 'g':
        return 'Multiply the value by 1000'
    elif user_selection == 'kg' and converter == 'mg':
        return 'Multiply the value by 1e+6'
    elif user_selection == 'kg' and converter == 'mcg':
        return 'Multiply the value by 1e+9'
    elif user_selection == 'kg' and converter == 't':
        return 'Divide the value by 1000'
    elif user_selection == 'kg' and converter == 'lt':
        return 'Divide the value by 1016'
    elif user_selection == 'kg' and converter == 'tn':
        return 'Divide the value by 907'
    elif user_selection == 'kg' and converter == 'st':
        return 'Divide the value by 6.35'
    elif user_selection == 'kg' and converter == 'lb':
        return 'Multiply the value by 2.20462'
    elif user_selection == 'kg' and converter == 'oz':
        return 'Multiply the value by 35.274'