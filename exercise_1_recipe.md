Problem:
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.


Function Signature:
def estimated_reading_time(text)
    prints a string that is the estimated reading time based on input text

Parameters:
    text: a long string of text to read

Returns:
    a new string, units are in hours, minutes and seconds

Side effects:
    This function should print the reading time integer, no other side effects


Examples:
"""
Given a text with 600 words
It returns a time of 3 minutes
"""
estimated_reading_time(text) => '3 minutes'

"""
Given a text with 20 words
It returns a time of 6 seconds
"""
estimated_reading_time(text) => '6 seconds'

"""
Given a text of 12,000 words
It returns a time of 1 hours
"""
estimated_reading_time(text) => '1 hour'

"""
Given a text of 2300 words
It returns a time of 11 minutes and 30 seconds
"""
estimated_reading_time(text) => '11 minutes, 30 seconds'

"""
Given a text of 32200 words
It returns a time of 2 hours and 41 minutes
"""
estimated_reading_time(text) => '2 hours, 41 minutes'

"""
Given anything other than a string, e.g. a number
It throws an error
"""
estimated_reading_time(123) => throws an error

