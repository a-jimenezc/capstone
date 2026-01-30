Potential idea for Capstone project:
•	Model: Morris–Lecar Model
•	Run simulations:
•	Ground truth data
•	Simulated noisy measurement
•	Joint parameter-state estimation:
•	UKF
•	Kalman Net / Unsupervised Kalman Net
•	Dynamical analysis and comparison
Main idea
Can a model-based Unscented Kalman Filter (UKF) and a data-driven learned filter (KalmanNet)  jointly estimate the system’s states and parameters from noisy voltage measurements well enough that the inferred model preserves the same qualitative dynamical behavior as the ground-truth model?
Similar to Moye paper.
Key resources
•	Matthew J. Moye · Casey O. Diekman. Data Assimilation Methods for Neuronal State and Parameter Estimation
•	G. Bard Ermentrout  David H. Terman Mathematical Foundations of Neuroscience
•	Terrence J. Sejnowski and Tomaso A. Poggio. Dynamical Systems in Neuroscience (chp 2,3, and 4)
•	https://www.coursera.org/learn/nonlinear-kalman-filters-parameter-estimation?specialization=kalman-filtering-applied (Theory and implementation for non-linear filtering and also join estimation)
•	G. Revach, N. Shlezinger, T. Locher, X. Ni, R. J. G. van Sloun and Y. C. Eldar, "Unsupervised Learned Kalman Filtering," 2022 30th European Signal Processing Conference (EUSIPCO), Belgrade, Serbia, 2022, pp. 1571-1575, doi: 10.23919/EUSIPCO55093.2022.9909801.
Relation to robotics
This project targets a core problem in human–machine interfacing: reliably estimating internal neural state from noisy biosignals so that a device can interpret intent and provide feedback. 
The present work aims to develop and compare model-based and data-driven state/parameter estimation methods that can recover neural dynamics and preserve key behavior under noise. That capability is a building block for closed-loop neuroprosthetic systems, where a controller must infer what the nervous system is doing, decide how to stimulate or assist, and update in real time. 
Therefore, the project contributes to robotics at the level of estimation and system modeling for neural interfaces, supporting the broader pipeline from neural decoding to control to actuation in prosthetic and assistive technologies.
What the program is looking for
Does the student show mastery of the material being presented in the document and of what he learned in the program?
Capstone Form

Title *
Provide a concise, descriptive title for your proposed capstone.
Model-based Extended Kalman Filter vs Learned KalmanNet for Joint State-Parameter Estimation in the Morris-Lecar Neuron Model
Description *
Provide a brief, high-level description of the project.
This project uses the Morris-Lecar biophysical neuron model to generate ground-truth data and noisy voltage-only measurements, then it compares a classical model-based estimator (EKF) with a learned filter (KalmanNet) for joint state and parameter estimation. Performance is evaluated quantitatively (state/parameter error) and qualitatively (by checking whether the estimated model parameters preserve key dynamical behavior), which motivates its relevance to neural interfaces and prosthetic control pipelines.
Objectives *
Describe the main objectives (e.g., two or three), along with two or three milestones associated with each objective.
1.	Build the simulation and evaluation pipeline
Milestone 1: Implement Morris-Lecar simulator and generate ground-truth trajectories.
Milestone 2: Generate noisy measurements.
Milestone 3: Define evaluation metrics and plotting suite.
2.	Implement the two estimators
Milestone 1: Implement augmented-state EKF and validate.
Milestone 2: Implement KalmanNet training/inference pipeline; verify learning on simulated data.
3.	Compare and report
Milestone 1: Run controlled comparisons across scenarios; produce true vs estimated parameter sets
Milestone 2: Summarize robustness and failure modes, write final report, and prepare presentation materials.
 
Scope *
Describe what work the project will include and what work the project will *not* include. Also, provide a good-faith estimate of how long the project may take, in semesters.
Includes: Morris-Lecar model simulation; synthetic noisy voltage measurement generation; joint state-parameter estimation with EKF and KalmanNet; quantitative and qualitative dynamical comparison; final report and presentation.
Does not include: hardware experiments; in-vivo data collection; large-scale prosthetic decoding datasets.
Estimated duration: 1 semester.
Methods *
Describe the overall approach(es) and methods you anticipate using throughout this project. Description should be both general (e.g., theoretical, experimental, computational, etc.) and specific (e.g., theoretical: model-based robust control, Bayesian statistics,...; experimental: prototype validation/testing, data collection/analysis; computational: reinforcement learning in simulation, finite element analysis,...;etc.).
Computational and simulation-based.
Modeling: Morris-Lecar nonlinear ODE neuron model; discretization for state-space estimation; augmented-state formulation for joint parameter-state estimation.
Classical estimation: Extended Kalman Filter (EKF) with process and measurement noise modeling.
Data-driven estimation: KalmanNet learned filtering for nonlinear state estimation, trained on simulated trajectories.
Analysis: statistical error metrics, robustness experiments, and dynamical/behavioral evaluation via comparisons.
Resources *
List any equipment and/or resources (e.g., VR goggles, 3D printer, RGB-D sensor, access to UMN high-power computational resources,...etc.) that you would need in order to do the proposed work

Laptop with Python and MATLAB environment.
Access to UMN high-performance computing.
Standard scientific libraries (NumPy/SciPy/PyTorch and MATLAB toolboxes).

