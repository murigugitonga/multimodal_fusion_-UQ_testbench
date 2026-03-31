import streamlit as st
import pandas as pd
from engine import UQKalmanFilter
from sensors import get_sensor_reading

st.set_page_config(page_title="Resilient Fusion", layout="wide")
st.title("Resilient Systems: Anti-Spoofing Fusion")

# Config
st.sidebar.header("Attack Vector")
spoofing_active = st.sidebar.toggle("Activate Sensor Spoofing", value=False)
sensitivity = st.sidebar.slider("UQ Gate Sensitivity", 1.0, 10.0, 3.0)

# Init Filter
kf = UQKalmanFilter(q=0.1, r=1.0)
kf.threshold = sensitivity

# Run Simulation
true_pos = 20.0
results = []

for i in range(100):
    #predict
    kf.predict()

    # Get Measurement (spoofing starts at step 40)
    is_attack = spoofing_active and i > 40
    z = get_sensor_reading(true_pos, 1.0, spoof=is_attack)

    #Update with UQ
    estimate, flagged, nis = kf.update(z, 1.0)

    results.append({
        "Step": i,
        "True": true_pos,
        "Measured": z,
        "Fused Estimate": estimate
        "Spoof Flag": 1 if flagged else 0,
        "NIS Score": nis
    })

df = pd.DataFrame(results)

#Plotting
st.subheader("Tracking Performance")
st.line_chart(df.set_index("Step")[["True","Measured","Fused Estimate"]])

st.subheader("Anomaly Detection(UQ Logic)")
st.bar_chart(df.set_index("Step")["Spoof Flag"])
st.caption("A, '1' indicates the system detected a statistical anomaly and rejected the sensor data.")