def estimated_reading_time(text):
    """make a variable assigned to empty list
    first element is hours, second is minutes, last is seconds
    convert the reading speed into separate seconds, hours and minutes
    add the units that are at least 1, keep the others 0
    go through that list, check if its 1 or more, if yes then convert it into a string
    put new strings into a list if they are 1 or more
    return combined strings joined together"""
    word_count = len(text)
    minutes = int(word_count / 200)
    hours = int(minutes / 60)
    seconds = int((word_count % 200) / 200 * 60)
    units = [hours, minutes, seconds]
    valid_units = []
    for unit in units:
        if unit >=1 and unit < 60:
            valid_units.append(unit)
        elif unit > 60:
            valid_units.append(unit % 60)
        else:
            valid_units.append(0)
    
    unit_strings = []
    for index in range(0, 3):
        if index == 0 and valid_units[index] > 0:
            unit_strings.append(f"{valid_units[index]} hours")
        elif index == 1 and valid_units[index] > 0:
            unit_strings.append(f"{valid_units[index]} minutes")
        elif index ==2 and valid_units[index] > 0:
            unit_strings.append(f"{valid_units[index]} seconds")
    
    final_string = ", ".join(unit_strings)
    return f"reading time: {final_string}"

