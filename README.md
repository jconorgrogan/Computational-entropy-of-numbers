## Computational-entropy-of-numbers

 Kolmogorov complexity answers: What is the shortest description?  
 Computational entropy answers: How many descriptions exist? 

...Don't think I've seen this in the literature; if it exists, please send it my way!

---

1. Formal Definition

1.1 Breakdown of the Definition

Definition:
For a given number x, the Computational Entropy PD(x) is defined as:
PD(x) = |{ p | U(p) = x }|

where:
* U is a universal Turing machine.
* p represents distinct Turing machine programs.
* U(p) = x denotes that program p outputs the number x.

Components:
1. Universal Turing Machine (U):
   * Serves as the standard computational model.
   * Ensures that PD(x) is machine-independent up to a constant factor, similar to Kolmogorov Complexity.

2. Program p:
   * A finite binary string representing a valid Turing machine program.
   * Each distinct p potentially corresponds to a unique computational pathway to produce x.

3. Output Condition U(p) = x:
   * Ensures that only programs that correctly compute x are counted.
   * Programs that do not halt or produce different outputs are excluded.

1.2 Analysis of Each Component

1. Universal Turing Machine (U):
   * Choice of U affects PD(x) only up to a multiplicative constant, similar to invariance in Kolmogorov Complexity.
   * Different universal machines can be used, but results remain equivalent in a theoretical sense.

2. Program p:
   * Programs can vary in length, structure, and computational approach.
   * Includes all possible ways to compute x, ranging from minimal descriptions to highly redundant or inefficient algorithms.

3. Output Condition U(p) = x:
   * Ensures precise counting of computational pathways that result in x.
   * Excludes programs that either do not produce x or do not halt.
---

After thinking about this for a fair bit, going down the path of calculating all of the different ways you can possibly think through computing a number (e.g., infinite series, addition + subtraction, and the countably infinite ways you can add countably infinite numbers together, probabilistic programs like Buffon's needle for π), I actually think there is an easier way. My intuition says that **Kolmogorov Complexity** is actually relevant here; because once the shortest piece of code is established, one can code in to ignore any other part of the programs. Once you have established the shortest piece of code that can compute a given number, you can essentially disregard all the trivial extensions or modifications that don't add meaningful information. 

In a strict sense, all those variants—whether they involve adding no-operations, redundant steps, or changing the structure without affecting the output—would still count as distinct different programs. This is because, from the perspective of a Turing machine, each of these programs has a unique sequence of states, instructions, or symbols, even if they ultimately produce the same output.

Then I thought, even though the vast majority of random Turing programs are, effectively, "jibberish"—nonsensical sequences that either don't halt or don't yield anything meaningful—within that immense sea of randomness, there exist programs that compute something of significance, such as Buffon's needle for π, or perhaps a sequence that perfectly replicates some famous series like Gregory-Leibniz. Perhaps random paths, through sheer chance, would include programs that not only compute **x** but do so in fundamentally different ways (e.g., probabilistically, iteratively, geometrically).

---

### Thermodynamic Analogy

There’s a compelling analogy between computational entropy and thermodynamic entropy in statistical mechanics:

In thermodynamics, entropy quantifies the number of microstates corresponding to a particular macrostate. Here, the macrostate is the number **x**, and the microstates are the distinct Turing programs that compute **x**. In Boltzmann's formulation, entropy **S** is proportional to the logarithm of the number of microstates:

$$
S = k_B \log \Omega
$$

Similarly, you could think of **Computational Entropy** as quantifying the "computational microstates" that all converge to the same "computational macrostate"—the number itself.

If **Kolmogorov Complexity** is akin to minimizing the "energy" required to describe a number, **Computational Entropy** might correspond to the diversity of states or pathways that maintain the system at that energy level. High computational entropy could indicate that a number is "low-energy" in the sense that many different paths can reach it, making it more probable under random computation—just as low-energy configurations are more probable in physical systems.


**Ranking thus far:**
1. Chaitin’s Omega (Ω): Algorithmically random, incompressible, and extremely complex.

2. Prime Numbers Defined by Complex Mathematical Problems: Includes Mersenne primes, Fermat primes, and primes emerging from complex constructions such as Diophantine equations. These primes are rare due to both their primality and the additional complexity of their construction.

3. Numbers Defined by Complex Mathematical Problems (e.g., Busy Beaver Outputs): Numbers defined by extreme growth or by the behavior of Turing machines, such as Busy Beaver outputs.

4. Liouville Numbers: Transcendental numbers that have a specific representation but remain rare due to fewer redundant computational pathways.

5. Numbers from Hard-to-Converge Infinite Series or Continued Fractions: Numbers that are hard to compute due to irregular or slow convergence in their representations.

6. General Prime Numbers (Especially Larger Primes): Unique due to the absence of factorization pathways, making them computationally rare compared to composites.

7. Square Roots of Prime Numbers (e.g., √2, √3): These are algebraic numbers involving prime factors, adding additional complexity compared to composite roots.

8. Rational Numbers with Prime Numerators or Denominators: Rational numbers that have a prime in either the numerator or the denominator are less compressible and thus rarer than those involving only composite factors.

9. Numbers from Specific Algorithmic Randomness (e.g., Deterministic Chaos): Generated by deterministic but chaotic processes, making them rare due to sensitivity to initial conditions.

10. Square Roots of Small Composite Numbers (e.g., √4, √9): More compressible and less rare than roots involving primes due to factorization into smaller components.

11. The Golden Ratio (φ): Multiple ways to represent it, making it more common compared to numbers involving prime complexity.

12. Mathematical Constants with High Representational Versatility (π, e): Many different ways to compute these constants, leading to higher computational entropy and making them less rare.

13. General Simple Rational Numbers: Rational numbers involving larger numerators and denominators, which are more complex compared to simple fractions early in the Stern-Brocot tree.

14. Early Stern-Brocot Fractions (e.g., 1/2, 1/3, 2/3): Simple fractions that are frequently produced in computational processes due to their early generation in systematic constructions like the Stern-Brocot tree.

15. Highly Composite Numbers (e.g., 12, 24, 60): Numbers with many divisors and factorizations, making them less rare due to multiple pathways for generation.

16. Composite Numbers in General (e.g., 15, 36): Numbers with more pathways to generate due to multiple factors, making them more common than primes.

17. Small Positive Integers (2, 3, 4, etc.): These numbers are commonly produced in computational processes through counting or basic arithmetic, making them relatively common.

18. 0 and 1: The most common and least rare values, trivially produced by many different computational processes due to their simplicity and universality.


