## AltPy ETL

AltPy ETL is a layer of abstraction on top of Pandas, whose goal is to simplify building data ETL processes in Python and reduce the code complexity.

The AltPy library requires only 1 file: altpy.py

We also provide an example of application (run_altpy.py). As we are currently working on deploying altpy-etl on pypi.org to make it pip available, you might want to copy-past the altpy.py file next to the run_altpy.py file to execute it.

2 versions of the library exist: altpy_2.py (for Python 2.x), and altpy_3.py (for Python 3.x)

Functions available:

- inputdata (xlsx, csv)
- outputdata (xlsx, csv)
- browse (top, all)
- select (display, keep, drop, rename, retype)
- summarize (average, sum, median)
- transpose
- crosstab
- join (inner, outer, left, right, left_only, right_only)
- union
- sort (asc, desc)
- filter (true, false)
- formula
- comment
