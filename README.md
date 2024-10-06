# Computational-entropy-of-numbers

Don't think I've seen this in the literature; if it exists, please sent send my way!

Computational Entropy of Numbers is a novel metric that classifies numbers based on the diversity of Turing programs that can compute them. If Kolmogorov Complexity reveals how concise a description can be, Computational Entropy tells us how versatile the computation of that value is.

Formally, for a number x, the Computational Entropy PD(x) is defined as the cardinality of the set of all distinct Turing programs p such that a universal Turing machine U produces x as an output:

PD(x) = |{ p : U(p) = x }|



