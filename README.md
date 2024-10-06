# Computational-entropy-of-numbers

Don't think I've seen this in the literature; if it exists, please sent send my way!

Something i'm terming Computational Entropy of Numbers; it classifies numbers based on the diversity of Turing complete programs (eg: Number of distinct turing programs) that can compute them. If Kolmogorov Complexity reveals how concise a description can be, Computational Entropy tells us how versatile the computation of that value is.

Formally, for a number x, the Computational Entropy PD(x) is defined as the cardinality of the set of all distinct Turing programs p such that a universal Turing machine U produces x as an output:

PD(x) = |{ p : U(p) = x }|


... After thinking about this for a fair bit, going down the path of calculating all of the different ways you can possibly think through computing a number (eg infinite series, addition + subtraction and the countably infinite ways you can add countably infinite numbers together, probablistic programs like Buffon's needle and pi) I actually think there is an easier way; My intuition says that Kolmogorov Complexity is actully relavent here; because once the shortest piece of code is established, one can code in to ignore any other part of the programs. Once you have established the shortest piece of code that can compute a given number, you can essentially disregard all the trivial extensions or modifications that don't add meaningful information. In a strict sense, all those variants—whether they involve adding no-operations, redundant steps, or changing the structure without affecting the output—would still count as distinct different programs. This is because, from the perspective of a Turing machine, each of these programs has a unique sequence of states, instructions, or symbols, even if they ultimately produce the same output.
