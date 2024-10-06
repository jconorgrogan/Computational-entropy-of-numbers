# Computational-entropy-of-numbers

Don't think I've seen this in the literature; if it exists, please sent send my way!

Something i'm terming Computational Entropy of Numbers; it classifies numbers based on the diversity of Turing complete programs (eg: Number of distinct turing programs) that can compute them. If Kolmogorov Complexity reveals how concise a description can be, Computational Entropy tells us how versatile the computation of that value is.

Formally, for a number x, the Computational Entropy PD(x) is defined as the cardinality of the set of all distinct Turing programs p such that a universal Turing machine U produces x as an output:

PD(x) = |{ p : U(p) = x }|


... After thinking about this for a fair bit, going down the path of calculating all of the different ways you can possibly think through computing a number (eg infinite series, addition + subtraction and the countably infinite ways you can add countably infinite numbers together, probablistic programs like Buffon's needle and pi) I actually think there is an easier way; My intuition says that Kolmogorov Complexity is actully relavent here; because once the shortest piece of code is established, one can code in to ignore any other part of the programs. Once you have established the shortest piece of code that can compute a given number, you can essentially disregard all the trivial extensions or modifications that don't add meaningful information. In a strict sense, all those variants—whether they involve adding no-operations, redundant steps, or changing the structure without affecting the output—would still count as distinct different programs. This is because, from the perspective of a Turing machine, each of these programs has a unique sequence of states, instructions, or symbols, even if they ultimately produce the same output.

Then I thought, even though the vast majority of random Turing programs are, effectively, "jibberish"—nonsensical sequences that either don't halt or don't yield anything meaningful—within that immense sea of randomness, there exist programs that compute something of significance, such as Buffon's needle for π, or perhaps a sequence that perfectly replicates some famous series like Gregory-Leibniz.Perhaps random paths, through sheer chance, would include programs that not only compute x but do so in fundamentally different ways (e.g., probabilistically, iteratively, geometrically).

There’s a compelling analogy between computational entropy and thermodynamic entropy in statistical mechanics:

In thermodynamics, entropy quantifies the number of microstates corresponding to a particular macrostate. Here, the macrostate is the number  x, and the microstates are the distinct Turing programs that compute x.  In Boltzmann's formulation, entropy 𝑆 S is proportional to the logarithm of the number of microstates ( 𝑆 = 𝑘 𝐵 log ⁡ Ω S=k B ​ logΩ).

 Similarly, you could think of Computational Entropy as quantifying the "computational microstates" that all converge to the same "computational macrostate"—the number itself.

If Kolmogorov Complexity is akin to minimizing the "energy" required to describe a number, Computational Entropy might correspond to the diversity of states or pathways that maintain the system at that energy level. High computational entropy could indicate that a number is "low-energy" in the sense that many different paths can reach it, making it more probable under random computation—just as low-energy configurations are more probable in physical systems.
