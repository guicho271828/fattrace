
# Fattrace

Provides an informative (fat) stacktrace that shows everything on the stack.

## Examples

Before:

<img src="imgs/std.png">

After:

<img src="imgs/fat.png">


## Highlights

* Removes the need for printf and debugger
* Special handling for array-like objects which have members that are named one of:
  * dtype
  * shape
  * device
  * layout

## Usage

Run `fattrace.install()` anywhere to replace the standard stack-trace hook ([`sys.excepthook`](https://docs.python.org/3/library/sys.html#sys.excepthook)).

Customization is done by the keyword arguments:

``` python
def install(threshold=3,
            include_self=True,
            ignore={},
            ignore_type={},
            include_private=False):
    ...
```

* `threshold` : the maximum number of elements to print in a list, tuple, dict, etc.
* `include_self` : in a method call, whether to print the members of `self`.
* `ignore` : A set of strings. Variables and members matching any of the names are excluded from the trace.
* `ignore_type` : A set of types. Variables and members matching any of the types are excluded from the trace.
* `include_private` : If true, private variables and members whose names start with "__" are excluded from the trace.

