# prediction_validation

I implemented my solution using Python 3.x.

I developed this on Windows 10 and tested in Ubuntu.

My initial idea was to limit the amount of memory required by looping over the
files, grabbing the data for each hour, parsing it into meaningful objects,
and continuing until all files were read. This took VERY LONG to get through
the loops, and I found that my implementation of nested loops causes more
overhead in Python than was necessary.
Instead, I decided to rely on Python's list comprehension and dictionary
objects for speed, and to keep the nested loops to a minimum.

I also wrote a small script to check my results against the correct results,
considering the +-0.01 difference mentioned in the readme.

## packages
### decimal
I used the decimal.Decimal object to maintain precision for the stock values.

### sys
I used sys.argv to receive command line arguments and sys.exit to quit the
program in the event that there were not enough command line arguments.