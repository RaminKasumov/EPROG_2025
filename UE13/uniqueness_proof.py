"""
Assume two normalized representations of x:

x = (1.a₂a₃...aₘ)₂ * 2^e
x = (1.b₂b₃...bₘ)₂ * 2^f

Assume e ≠ f.
Then dividing both expressions gives:

2^(e-f) = (1.b...)/(1.a...)

Left side is an integer power of 2.
Right side is in (1/2, 2), impossible unless e = f.

Thus exponents equal ⇒ mantissas equal ⇒ representation unique.
"""