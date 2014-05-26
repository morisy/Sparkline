#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Here are the six Sparkline options: ▁▂▃▅▆▇
# See Zach Seward: http://zachseward.com/sparktweets/

# Pass in a Tuple, get out a sparkline.
import unicodecsv

def sparkitize(numbers):
    graph = ""
    for number in numbers:
        if max(numbers)-(max(numbers)/6) <= number <= max(numbers):
            graph+= "▇"
        elif max(numbers)-(2*(max(numbers)/6)) <= number <= max(numbers):
            graph+= "▆"
        elif max(numbers)-(3*(max(numbers)/6)) <= number <= max(numbers):
            graph+= "▅"
        elif max(numbers)-(4*(max(numbers)/6)) <= number <= max(numbers):
            graph+= "▃"
        elif max(numbers)-(5*(max(numbers)/6)) <= number <= max(numbers):
            graph+= "▂"
        elif number > 0:
            graph+= "▁"
        elif number == 0:
            graph+= "▁"
        else:
            graph+= "▁"
    return graph