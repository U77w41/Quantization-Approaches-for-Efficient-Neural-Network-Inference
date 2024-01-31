# Quantization-Approaches-for-Efficient-Neural-Network-Inference
An Investigation into Techniques for Efficient Neural Network Inference through the Survey of Various Quantization Methods and Approaches.


Quantization is a technique used for performing computations and storing tensors at lower bitwidths than floating-point precision. The process involves converting floating-point numbers to a lower bit representation, and later dequantizing them back to their original precision. Here are the formulas for quantization and dequantization:

### Quantization Formula

The quantization formula typically involves rounding the floating-point number to the nearest representable value within the reduced bitwidth. Let `x` be the original floating-point number, `q` be the quantized value, and `S` be the scaling factor:

\[ q = \text{round}(x \times S) \]

### Dequantization Formula

The dequantization process involves converting the quantized value back to the original floating-point precision. Let `q` be the quantized value, `x'` be the dequantized value, and `S` be the scaling factor:

\[ x' = \frac{q}{S} \]

In these formulas, `S` is often chosen to be a power of 2 to simplify the quantization process, and it is used to scale the floating-point numbers before rounding during quantization and after scaling during dequantization.

It's important to note that the choice of scaling factor and bitwidth greatly influences the precision and range of representable values after quantization and dequantization.

