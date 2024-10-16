This theory presents a formal framework for defining randomness in computational terms, using program size and computational exhaustion within a universal Turing machine context. It introduces the concept of **computational entropy** to quantify randomness based on the diversity of programs that can produce a given output. Randomness is characterized by the inability of smaller programs to generate or predict the outputs of larger programs.

## Context

The theory builds upon foundational concepts in **Algorithmic Information Theory (AIT)**, particularly notions of **Kolmogorov Complexity** and **algorithmic randomness**. In AIT, the complexity of a string is measured by the length of the shortest program that produces it. A string is considered random if it is incompressible, meaning no shorter program can generate it.

This theory extends these ideas by:

- Emphasizing the **relative nature of randomness**: Randomness is assessed concerning the set of smaller programs that fail to produce a given output.
- Introducing **computational entropy** as a quantitative measure: It accounts for the number of distinct programs that can generate an output, providing a spectrum of randomness rather than a binary classification.

## Mathematical Overview

### Universal Turing Machine and Programs

Let \( U(p) \) denote a **universal Turing machine** that executes program \( p \) and produces output \( x \). Programs are binary strings of length \( n \) bits, representing sequences of instructions.

- **Program Length (\( n \))**: The number of bits in the program \( p \).
- **Set of Programs of Length \( n \)**: \( P(n) = \{ p \mid \text{length}(p) = n \} \).

### Computational Entropy

The **computational entropy** \( PD(x) \) of an output \( x \) is defined as the number of distinct programs that produce \( x \):

\[
PD(x) = \left| \{ p \mid U(p) = x \} \right|
\]

- **High Computational Entropy**: Many programs produce \( x \), implying \( x \) is less random.
- **Low Computational Entropy**: Few programs produce \( x \), implying \( x \) is more random.

### Definition of Randomness

An output \( x \) is considered **random relative to programs of length \( k \)** if no program of length \( k \) or shorter can produce \( x \):

\[
\forall p \in P(k),\ U(p) \ne x
\]

where \( k < n \) and \( n \) is the length of the program that produces \( x \).

### Randomness and Program Size

Randomness arises when **shorter programs** cannot generate or predict the outputs of **longer programs**. This inability signifies that the output is incompressible relative to the smaller programs.

## Details and Examples

### Example 1: Programs of Lengths 2 and 3 Bits

#### Programs of Length 2 Bits

- **Total Programs**: \( 2^2 = 4 \)
- **Programs**: `00`, `01`, `10`, `11`
- **Possible Outputs** (using simple instruction sets): `0`, `1`, `2`

#### Programs of Length 3 Bits

- **Total Programs**: \( 2^3 = 8 \)
- **Programs**: `000`, `001`, `010`, `011`, `100`, `101`, `110`, `111`
- **Possible Outputs** (using more complex instruction sets): `0`, `1`, `2`, `3`, `4`, `5`

#### Analyzing Randomness

- **Output `4`**:
  - Produced by a 3-bit program (e.g., `111` in an instruction set that sums bits).
  - **No 2-bit program** can produce `4`.
  - **Conclusion**: `4` is random relative to 2-bit programs.

- **Output `1`**:
  - Produced by both 2-bit and 3-bit programs.
  - **Conclusion**: `1` is not random relative to 2-bit programs.

#### Computational Entropy Calculation

- **For Output `4`**:
  - **Computational Entropy**: \( PD(4) = 1 \) (only one 3-bit program produces `4`).
  - **High Randomness**: Low computational entropy implies higher randomness.

- **For Output `1`**:
  - **Computational Entropy**: \( PD(1) = 3 \) (multiple 2-bit and 3-bit programs produce `1`).
  - **Low Randomness**: High computational entropy implies lower randomness.

### Quantifying Randomness

Randomness can be quantified using computational entropy:

- **Randomness Measure**:
  \[
  R(x) = \frac{1}{PD(x)}
  \]
- **Example**:
  - \( R(4) = \frac{1}{1} = 1 \) (high randomness).
  - \( R(1) = \frac{1}{3} \approx 0.333 \) (lower randomness).

### Example 2: Programs of Length 1, 2, and 3 Bits

#### Programs of Length 1 Bit

- **Total Programs**: \( 2^1 = 2 \)
- **Programs**: `0`, `1`
- **Possible Outputs**: `0`, `1`, `-1` (limited by instruction sets).

#### Complete Analysis

- **Instruction Sets**: Exhaustively define all possible operations for programs of each length.
- **Outputs**:
  - **1-bit Programs**: Limited outputs due to program size.
  - **2-bit Programs**: Slightly more outputs.
  - **3-bit Programs**: Greater diversity of outputs, including those unattainable by shorter programs.

#### Randomness Relative to Program Length

- Outputs produced by 3-bit programs but not by 1-bit or 2-bit programs are considered random relative to the shorter program lengths.

## Conclusion

This theory formalizes randomness as a function of program size and computational exhaustion. By defining randomness relative to the inability of smaller programs to produce certain outputs and introducing computational entropy as a measure, it provides a quantitative and relative framework for understanding randomness in computational terms.

### Key Points

- **Relative Randomness**: Randomness is assessed concerning the set of programs considered, particularly smaller ones.
- **Computational Entropy**: Serves as a quantitative measure of randomness based on the number of programs producing an output.
- **Degrees of Randomness**: Outputs can be ranked by their computational entropy, allowing for a spectrum of randomness.

### Implications

- **Algorithmic Information Theory Alignment**: The theory aligns with concepts like Kolmogorov Complexity but adds the dimension of computational entropy.
- **Practical Applications**: Relevant in fields like cryptography, where understanding and quantifying randomness is crucial.
- **Theoretical Significance**: Offers a nuanced perspective on randomness, emphasizing its relative and quantifiable nature in computational contexts.
