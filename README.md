This repository contains code accompanying the article (in press by *Biophys. J.*)

---

### **Stochastic Kinetics of mRNA Molecules in a General Transcription Model**  

#### *Yuntao Lu and Yunxin Zhang*  

#### School of Mathematical Sciences, Fudan University, Shanghai 200433, China  

#### Email: `yuntaolu22@m.fudan.edu.cn` and `xyz@fudan.edu.cn`  

---

### Contents

- **14** Jupyter Notebooks
- **1** Python file
- **5** PDF files
- **25** NumPy files

---

### Directory Tree Structure

```
Transcription/
├── README.md
├── Main.ipynb
├── Main_timing.ipynb
├── SSA.ipynb
├── SSA_timing.ipynb
├── FSP.ipynb
├── FSP_timing.ipynb
├── Renewal_timing.ipynb
├── Parameters_for_Figures.py
├── ParametersFig3.ipynb
│
├── Fig1/
│   ├── Fig1.ipynb
│   ├── Fig1.pdf              
│   ├── sample_paths_SSA.npy
│   └── sample_paths_ode.npy
│
├── Fig2/
│   ├── Fig2.ipynb
│   ├── Fig2.pdf                 
│   ├── Fig2_bound1.npy
│   ├── Fig2_bound2.npy
│   ├── Fig2_density.npy
│   └── Fig2_moment.npy
│
├── Fig3/
│   ├── Fig3.ipynb
│   ├── Fig3.pdf                 
│   ├── fig3_FSP_a.npy
│   ├── fig3_FSP_b.npy
│   ├── fig3_FSP_c.npy
│   ├── fig3_FSP_d.npy
│   ├── fig3_SSA_a.npy
│   ├── fig3_SSA_b.npy
│   ├── fig3_SSA_c.npy
│   ├── fig3_SSA_d.npy
│   ├── fig3_MAIN_a.npy
│   ├── fig3_MAIN_b.npy
│   ├── fig3_MAIN_c.npy
│   └── fig3_MAIN_d.npy
│
├── Fig4/
│   ├── Fig4.ipynb
│   ├── Fig4.pdf               
│   ├── FSP_times.npy
│   ├── SSA_times.npy
│   ├── Renewal_times.npy
│   └── Main_times.npy
│
└── Fig5/
    ├── Fig5.ipynb
    ├── Fig5.pdf          
    ├── Fig5_fano.npy
    ├── Fig5_noise.npy
    └── Fig5_transformed_noise.npy
```

---

Jupyter Notebook `Main.ipynb` contains the implementation of the main analytical results in our article, along with basic visualization capabilities.

Jupyter Notebook `SSA.ipynb` contains the implementation of the stochastic simulation algorithm for our model, including basic visualization. This notebook requires the Python package `gillespy2`. 

Jupyter Notebook `FSP.ipynb` contains the implementation of the finite state projection algorithm for our model, with basic visualization.

The following notebooks measure computational performance:

- `Main_timing.ipynb`
- `SSA_timing.ipynb` 
- `FSP_timing.ipynb`
- `Renewal_timing.ipynb`

Each notebook executes its respective method and outputs timing data to corresponding NumPy files (`Main_times.npy`, `SSA_times.npy`, `FSP_times.npy`, `Renewal_times.npy`), which are used to generate the performance comparison in Figure 4.

The Python file `Parameters_for_Figures.py` contains the model parameters used in Figures 1-5.

Jupyter Notebook `ParametersFig3.ipynb` explicitly displays the model parameters used in Figure 3.

Each of the five figure directories (`Fig1/`, `Fig2/`, `Fig3/`, `Fig4/`, and `Fig5/`) contains:

- A Jupyter Notebook that reproduces the corresponding figure;
- Supporting NumPy files containing the plotted data;
- A PDF version of the figure as used in our article.
