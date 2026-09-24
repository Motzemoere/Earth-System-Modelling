# 🌍 Earth-System-Modelling -> Tutorials

Welcome! These tutorials teach you Python from scratch with the goal of building and understanding environmental models like the Soil-Water-Balance Model (SWBM).

## Opening Your First Notebook

**In Google Colab (recommended):**
1. Go to [Google Colab](https://colab.research.google.com/) and sign in with a Google account.
2. Go to **File → Open notebook → GitHub**.
3. Paste the repository URL `https://github.com/Motzemoere/Earth-System-Modelling` and pick `tutorials/01_Python_Basics_and_Data_Structures.ipynb` from the list.
4. Save your own copy via **File → Save a copy in Drive** — otherwise your changes are lost when you close the tab.
5. Click into the first code cell and press **Shift+Enter** to run it and move to the next one. Repeat top to bottom for the whole notebook.
6. From Notebook 2 on, the notebooks load the provided data directly from GitHub — you don't need to download anything (see [Loading the Data](../README.md#loading-the-data)).

More materials will be added as the course progresses. When new content is announced, just open the updated notebook from GitHub again (steps 2–4) rather than reusing your old copy — your own saved copy in Drive stays untouched.

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

- A Google account for [Google Colab](../README.md#getting-started-with-google-colab) — or, to work offline, Python 3.10+ with pandas, numpy and matplotlib (see the [local setup guide](../setup/README.md))
- No prior programming experience needed!

## Tips for Success

- **Don't skip the exercises** - they're essential for learning
- **Run all code cells** - sometimes cells depend on previous ones
- **Experiment!** - modify the code and see what breaks
- **Take notes** - writing down concepts helps retention
- **Ask questions** - reach out 
