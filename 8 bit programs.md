# Program Structure for 8 Bits

**Program Length:** 8 bits  
**Opcode:** Bits 1-2 (2 bits)  
**Operand1:** Bits 3-5 (3 bits)  
**Operand2:** Bits 6-8 (3 bits)  

**Total Programs:**  
\[
2^8 = 256
\]

## Instruction Set

### Opcodes (2 bits)
- **00:** Output Operand1 (Operand2 is ignored)
- **01:** Add Operand1 and Operand2
- **10:** Multiply Operand1 and Operand2
- **11:** Bitwise AND of Operand1 and Operand2

### Operands (3 bits each)
Can represent values from 0 to 7 (binary 000 to 111)

## Full Table of Outputs and Program Counts

| Output | Opcode 00 | Opcode 01 | Opcode 10 | Opcode 11 | Total Programs |
|--------|------------|------------|------------|------------|----------------|
| 0      | 8          | 1          | 15         | 27         | 51             |
| 1      | 8          | 2          | 1          | 9          | 20             |
| 2      | 8          | 3          | 2          | 9          | 22             |
| 3      | 8          | 4          | 2          | 3          | 17             |
| 4      | 8          | 5          | 3          | 9          | 25             |
| 5      | 8          | 6          | 2          | 3          | 19             |
| 6      | 8          | 7          | 4          | 3          | 22             |
| 7      | 8          | 8          | 2          | 1          | 19             |
| 8      | 0          | 7          | 2          | 0          | 9              |
| 9      | 0          | 6          | 1          | 0          | 7              |
| 10     | 0          | 5          | 2          | 0          | 7              |
| 11     | 0          | 4          | 0          | 0          | 4              |
| 12     | 0          | 3          | 4          | 0          | 7              |
| 13     | 0          | 2          | 0          | 0          | 2              |
| 14     | 0          | 1          | 2          | 0          | 3              |
| 15     | 0          | 0          | 2          | 0          | 2              |
| 16     | 0          | 0          | 1          | 0          | 1              |
| 18     | 0          | 0          | 2          | 0          | 2              |
| 20     | 0          | 0          | 2          | 0          | 2              |
| 21     | 0          | 0          | 2          | 0          | 2              |
| 24     | 0          | 0          | 2          | 0          | 2              |
| 25     | 0          | 0          | 1          | 0          | 1              |
| 28     | 0          | 0          | 2          | 0          | 2              |
| 30     | 0          | 0          | 2          | 0          | 2              |
| 35     | 0          | 0          | 2          | 0          | 2              |
| 36     | 0          | 0          | 1          | 0          | 1              |
| 42     | 0          | 0          | 2          | 0          | 2              |
| 49     | 0          | 0          | 1          | 0          | 1              |
| **Total** | **64**     | **64**     | **64**     | **64**     | **256**        |
