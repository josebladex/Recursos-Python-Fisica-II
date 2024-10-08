# RC Circuit Analysis for Capacitor Charging and Discharging

## Summary
This report aims to study the behavior of voltage, current, and charge in an RC circuit during the charging and discharging processes of a capacitor over time. Experiments were conducted in a physics laboratory to analyze the electrical characteristics of an RC circuit composed of a resistor (R) and a capacitor (C) connected in series to a power supply. In the first part of the experiment, the capacitor was charged from a fully discharged state to maximum charge, recording voltage and current values as a function of time. In the second part, the discharging of the capacitor was studied after disconnecting the power supply. The primary goal is to obtain a quantitative description of the circuit's behavior, using regression techniques to fit experimental results to mathematical equations that describe the charging and discharging processes over time. This will enable a better understanding and modeling of the RC circuit's electrical behavior.

**Keywords:** RC Circuit, Electrical Behavior, Capacitor Charging and Discharging, Laboratory Experiments, Regression Techniques

## 1. Introduction
RC circuits, also known as resistance-capacitance circuits, are fundamental in electronics and play a crucial role in a variety of applications. These circuits are a combination of resistors and capacitors that work together to store and release electrical charges. Their temporal response nature makes them ideal for functions such as filtering, timing, and signal attenuation.

An RC circuit consists of a resistor (R) and a capacitor (C) connected in series or parallel. The resistor limits the flow of electrical current, while the capacitor stores electrical charge in its dielectric structure. When a voltage is applied to an RC circuit, the capacitor charges gradually through the resistor. During the charging process, the voltage across the capacitor increases exponentially until it reaches the input voltage.

## 2. Materials and Methods
Materials used in the experiment included a voltage source set to 20V, a 20 kΩ resistor, a 4700 μF capacitor, a breadboard, a voltmeter, an ammeter, and copper wires. The experiment began with the capacitor fully discharged. The RC circuit was assembled with the voltmeter connected in parallel with the capacitor and the ammeter in series with the resistor. Voltage and current readings were recorded during the charging process and after disconnecting the power supply during the discharging process. Data was analyzed using regression techniques to fit mathematical equations describing the capacitor's charging and discharging processes over time.

## 3. Results and Discussion
Results from the capacitor charging were observed, and the software generated scatter plots with blue points for the variables studied over time, along with a red regression curve fitting the behavior of the data. Exponential regressions were necessary for describing charge and voltage, while current was treated with a standard exponential regression. The results show correlation between circuit parameters and fundamental equations, with accurate estimates of the resistance used.

## 4. Conclusions
Laboratory experiments provided accurate data on voltage, current, and charge as a function of time, compared to theoretical equations. During the capacitor's charging, both current and voltage followed an exponential behavior, adjusted using modified exponential regression techniques, providing equations that describe the electrical charge stored in the capacitor over time. During discharging, current and voltage also followed an exponential law, with standard exponential regressions sufficient for describing these variables. These findings are essential for understanding how the RC circuit stores and releases electrical energy.

## 5. References
- H. D. and R. A. F. YOUNG, University Physics with Modern Physics Volume 2, Mexico: PEARSON EDUCATION, 2009.
- J. Plata, "Github," 2023. Available at: [https://github.com/josebladex/Recursos-Python-Fisica-II.git](https://github.com/josebladex/Recursos-Python-Fisica-II.git)
