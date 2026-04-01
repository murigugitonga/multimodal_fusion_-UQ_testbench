# Resilient Multimodal Fusion & UQ Testbench

This is a modular python framework for simulating **Late Fusion** and **Kalman Filter-based state estimation** in contested environments. It incorporates an **Uncertainty Quantification** to detect and reject spoofed sensor data in a single, simulated Mobile Ad-hoc Network node.

## Key Features

- **Late Fusion Gate:** Implements weighted probability fusion, allowing for dynamic sensor weighting based on environmental degradation.
- **Recursive Kalman Filtering:** Provides 1D state estimation that balances physics-based prediction with sensor-based correction.
- **Innovation-based UQ:** Detects adversarial spoofing by monitoring the **residual**. If a measurement falls outside the statistical confidence interval ( e.g 3rd-order Sigma), the gate automatically rejects the input to maintain system integrity.
- **MOSA Compliant Design:** The fusion engine is agnostic to the sensor source, enabling plug-and-play capability for different modalities.

## Installation and Execution

Clone the project and install the requirements

```bash
git clone https://github.com/murigugitonga/fusion-testbench.git

cd fusion-testbench

uv add requirements.text
uv lock

uv run streamlit run src/app.py

```
