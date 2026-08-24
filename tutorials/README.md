# 🌍 Earth-System-Modelling -> Tutorials

Welcome! These tutorials teach you Python from scratch with the goal of building and understanding environmental models like the Soil-Water-Balance Model (SWBM).

## Opening Your First Notebook

**In VS Code:**
1. Open the `Earth-System-Modelling` folder in VS Code (`File > Open Folder...`).
2. Install the **Jupyter** extension (one-time setup): click the Extensions icon in the left sidebar (or press `Ctrl+Shift+X`), search for "Jupyter", and click **Install** on the extension published by Microsoft.
3. In the file explorer on the left, click `tutorials/01_Python_Basics_and_Data_Structures.ipynb` to open it.
4. In the top-right corner of the notebook, click **Select Kernel** and choose the `esm` environment you created in [Setup](../setup/README.md).
5. Click into the first code cell and press **Shift+Enter** to run it and move to the next one. Repeat top to bottom for the whole notebook.

**In Google Colab:**
1. Upload `01_Python_Basics_and_Data_Structures.ipynb` to your Google Drive.
2. Right-click the file in Google Drive and choose **Open with > Google Colaboratory**.
3. Click into the first code cell and press **Shift+Enter** to run it and move to the next one. Repeat top to bottom for the whole notebook.
4. At some point you will need the provided additional data for the tutorials, so you also need to upload the **[data](../data)** folder to Google Drive.

Once you're comfortable opening and running a notebook this way, work through Notebooks 2-5 below the same way, in order.

---

## Tutorial Overview

### Notebook 1: Python Basics and Data Structures
**Duration:** ~2 hours | **Level:** Beginner

Learn the fundamentals of Python:
- Variables, data types, and basic operations
- Lists and dictionaries
- Writing and using functions
- First water balance calculation

**What you'll build:** A simple function to calculate daily water balance.

---

### Notebook 2: Working with Data - Pandas and NumPy
**Duration:** ~2 hours | **Level:** Beginner to Intermediate

Master the tools for handling real environmental data:
- Loading and exploring CSV files with Pandas
- NumPy arrays and vectorized operations
- Filtering and analyzing datasets
- Basic statistics and visualization

**What you'll work with:** Real precipitation and soil moisture data from Germany, Spain, and Sweden.

---

### Notebook 3: Functions, Loops, and Control Flow
**Duration:** ~2 hours | **Level:** Intermediate

Build more complex simulations:
- Writing functions with multiple parameters
- Loops for time-based simulations
- Conditional logic in models
- Debugging and testing

**What you'll build:** A reservoir water model that simulates water storage, evaporation, and temperature changes over time.

---

### Notebook 4: Building Your Own Environmental Model
**Duration:** ~2.5 hours | **Level:** Intermediate

Learn the universal structure of environmental models:
- Defining state variables and parameters
- Organizing model processes
- Running multi-step simulations
- Analyzing model sensitivity

**What you'll build:** A complete plant growth model that you can modify and extend, preparing you to build the SWBM independently.

---

### Notebook 5: Advanced Python & Beyond
**Duration:** Variable | **Level:** Advanced (Optional)

Work with real-world data quality issues and model evaluation:
- Handling missing values (NaN) and plausibility checks
- Time series analysis
- Comparing multiple datasets
- Evaluating a model against observations

**Note:** This notebook goes beyond what you need for SWBM. It's optional for students interested in advancing their Python skills for future research or data science work.

---

## Getting Started

1. **Start with Notebook 1** - you don't need any prior Python experience
2. **Work through sequentially** - each notebook builds on previous ones
3. **Follow along with the code** - type the examples, don't just read them
4. **Do the exercises** - this is where learning happens
5. **Feel free to experiment** - try changing values and see what happens

## What You'll Learn by the End

✓ Read, manipulate, and analyze environmental data  
✓ Write functions and loops for scientific calculations  
✓ Build and run dynamic environmental models  
✓ Understand the SWBM and build your own implementation  
✓ Create publication-quality visualizations  

## Prerequisites

- Python 3.7+ (via Anaconda/Miniconda or similar)
- Jupyter Notebook
- Libraries: pandas, numpy, matplotlib (install via `pip install pandas numpy matplotlib`, or see the [setup guide](../setup/README.md) for the Conda option)
- No prior programming experience needed!

## Tips for Success

- **Don't skip the exercises** - they're essential for learning
- **Run all code cells** - sometimes cells depend on previous ones
- **Experiment!** - modify the code and see what breaks
- **Take notes** - writing down concepts helps retention
- **Ask questions** - reach out 
