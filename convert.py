def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """

    # convert unit_in and unit_out to lowercase for checking
    unit_in = unit_in.lower()
    unit_out = unit_out.lower()

    # check if unit_in and unit_out is valid
    if (unit_in == "c" or unit_in == "f") and (unit_out == "c" or unit_out == "f"):
        # if they are valid proceed ahead
        # if unit_in is in c and unit_out is f use the formula f = (c * 1.8) + 32 to convert to fahrenheit
        if unit_in == "c" and unit_out == "f":
            temp_in_fahrenheit = (temp * 1.8) + 32
            # return the converted temp
            return temp_in_fahrenheit
        # if unit_in is f and unit_out is c in f use the formula c = (f - 32) * 5/9 to convert to celsius
        elif unit_in == "f" and unit_out == "c":
            temp_in_celsius = (temp - 32) * 5/9
            # return the converted temp
            return temp_in_celsius
        # if both units are same do nothing and return the original temp
        else:
            return temp
    else:
        # if there are invalid unit check and return the invalid unit
        if (unit_in != "c" and unit_in != "f"):
            return f"Invalid unit {unit_in}"
        else:
            return f"Invalid unit {unit_out}"


print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")
