# NSAD — ROOT Notebooks

These notebooks are used in the 02NSAD course at the Faculty of Nuclear Sciences and Physical Engineering (FNSPE), Czech Technical University in Prague. They provide a compact, hands‑on introduction to data analysis with ROOT from Python.

[![Open in GitHub Codespaces](https://img.shields.io/badge/open-GH_Codespaces-blue?logo=github)](https://codespaces.new/matonoli/nsad-root-notebooks?quickstart=1)

## Objective

The main goal is to give you practical experience with:

- Creating and filling histograms and graphs in ROOT from Python.
- Reading and writing ROOT files (`TFile`) and basic work with `TTree`.
- Understanding the basic ROOT workflow used in HEP data analysis.

The **core focus for this NSAD class** is on the following two notebooks:

- `course/notebooks/core/01-histograms-and-graphs.ipynb`
- `course/notebooks/core/02-tfile-read-write-ttree.ipynb`

The remaining notebooks and exercises in this repository are considered **bonus** material. They are useful if you want to explore ROOT further, but they are not the primary focus of the NSAD course.

## How to use

You can use these materials in two main ways:

- **GitHub Codespaces (recommended)** — simplest, everything is preconfigured, ROOT is already installed.
- **Local installation on your own computer** — also possible, using e.g. `conda`, if you prefer to run everything locally.

Both options are described below.

### Option A: Run in GitHub Codespaces (recommended)

If you have a GitHub account, you can open this repository in GitHub Codespaces. This launches a cloud environment with the repository preloaded and ROOT already set up.

1. Click this badge and then press **“Create codespace”**:

   [![Open in GitHub Codespaces](https://img.shields.io/badge/open-GH_Codespaces-blue?logo=github)](https://codespaces.new/matonoli/nsad-root-notebooks?quickstart=1)

   Alternatively, open the repository page on GitHub, click the green **“Code”** button → **“Codespaces”** and create a new codespace.

2. VS Code will open in the browser with the repository already checked out. Wait a bit for the environment to finish installing any needed components.

3. Open the notebook you want to work with, e.g.:

   - `course/notebooks/core/01-histograms-and-graphs.ipynb`
   - `course/notebooks/core/02-tfile-read-write-ttree.ipynb`

4. When you run the first cell, VS Code will ask you to select a kernel. Choose the Python kernel that has ROOT available (this should be called `venv` and preselected).

5. Run cells in order from top to bottom.

### Option B: Run locally using conda

If you prefer to run the notebooks on your own machine (Linux, macOS, or Windows with WSL), you can set up an environment with ROOT and Jupyter using `conda` (which you need to install before, look up e.g. miniconda installation).

1. Clone this repository:

   ```bash
   git clone https://github.com/matonoli/nsad-root-notebooks.git
   cd nsad-root-notebooks
   ```

2. Create a new conda environment with Python and ROOT. One simple option is to use the `conda-forge` channel:

   ```bash
   conda create -n nsad-root -c conda-forge python=3.11 root jupyterlab
   conda activate nsad-root
   ```

   Notes:
   - This installs ROOT together with Python bindings and JupyterLab.
   - On some systems the exact version of ROOT may vary; any reasonably recent 6.xx version is fine for this course.  


3. Start Jupyter:

   ```bash
   jupyter notebook
   ```

4. In your browser, open:

   - `course/notebooks/core/01-histograms-and-graphs.ipynb`
   - `course/notebooks/core/02-tfile-read-write-ttree.ipynb`

5. Run the cells in order from top to bottom. If you get import errors related to ROOT, double‑check that:
   - The correct conda environment is active.
   - The selected Jupyter kernel corresponds to that environment.


## Notebook order and short descriptions

For the NSAD course, please at minimum complete these two core notebooks:

1. `course/notebooks/core/01-histograms-and-graphs.ipynb`  
   - Introduction to ROOT from Python.  
   - Creating and filling 1D histograms.  
   - Basic styling and drawing.  
   - ROOT graphs and simple plotting.
   - Exercise: Convert a histogram to a graph  

2. `course/notebooks/core/02-tfile-read-write-ttree.ipynb`  
   - Creating and reading ROOT files (`TFile`).  
   - Basic work with `TTree` (branches, reading data).  
   - Simple analysis patterns: reading, projecting into histograms, basic selections.
   - Basic work with `RDataFrame` (alternative analysis of `TTree`)
   - Exercise: Calculate the di-muon mass spectrum from CMS Open Data

The solutions to the exercises can be found in

- `course/notebooks/core/extra/solutions


## Quick Jupyter tips

- Always run cells from top to bottom the first time you open a notebook. Cells that import modules or open ROOT files must be executed before later cells that use them.
- If you run cells out of order and get `NameError`, missing histogram objects, or problems with open files, restart the kernel and run from the top.
- In VS Code / Codespaces:
  - When you run the first cell, you may be asked to select a kernel; choose the Python kernel that belongs to this project/environment.
  - Use `Shift+Enter` to run the current cell, or use the Run menu to execute all cells.
- If ROOT plotting windows do not appear as you expect, check whether:
  - The notebook is configured to draw in the notebook (inline) or in external windows.
  - You accidentally closed or hid the figure output cells.

## Credits and license

These notebooks are **adapted from** the official ROOT course for students:

- ROOT course for students — https://github.com/root-project/student-course/

The original course was developed by the ROOT team and provides a comprehensive introduction to ROOT for young scientists and engineers. This NSAD version follows that structure but simplifies and re‑targets a subset of the material for our class.

Some parts are heavily based on from:

- ROOT workshop materials — https://github.com/aprozo/root_workshop

which were further modified into Python‑based workflows.

All credit for the core content, examples, and pedagogical structure goes to the original authors and maintainers of these two repositories. This fork only makes small adjustments to fit the needs of the 02NSAD course at FNSPE CTU.

Feel free to use these materials for study and teaching. If you adapt them further, please make sure to credit:

- The ROOT project and authors of `student-course`,
- The authors of `root_workshop`,
- And this NSAD fork where relevant.