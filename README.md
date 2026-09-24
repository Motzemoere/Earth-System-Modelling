# 🌍 Earth-System-Modelling

This repository contains **materials** used in the **Earth System Modelling** course.  
It is designed to set you up with everything you need to finish the course. More materials will be added during the course.

---

## Getting Started with Google Colab

We work in [Google Colab](https://colab.research.google.com/) — it runs entirely in the browser, all packages we need are already installed and you don't have to install anything. Go to Colab and sign in with a Google account.

*Want to work offline on your own laptop instead? See the [local setup guide](setup/README.md).*


### Loading the Data

You don't need to download the data — pandas loads it directly from this repository on GitHub.

```python
import pandas as pd

DATA_URL = 'https://raw.githubusercontent.com/Motzemoere/Earth-System-Modelling/main/data/'
data = pd.read_csv(DATA_URL + 'Data_swbm_Germany.csv')
```

Just replace the file name to load `Data_swbm_Spain.csv` or `Data_swbm_Sweden.csv`. See the [data description](data/README.md) for the locations, columns and units of the datasets.

---

## Python Tutorials

**New to Python?** No problem — Colab is all you need, just work through the tutorial series that teaches you everything you need to understand and build environmental models!

### 5 Progressive Notebooks
1. **Python Basics** - Variables, functions, and data types
2. **Data Handling** - Working with pandas and real environmental datasets
3. **Simulation Logic** - Loops, functions, and building models
4. **Model Building** - Complete guide to creating environmental models
5. **Advanced Skills** - Real-world data quality issues and model evaluation (optional)

👉 **[Go to Tutorials](tutorials/README.md)**

These tutorials are designed for complete beginners and guide you from Python fundamentals all the way to building your own version of the SWBM. By the end, you'll understand not just *how* such a model works, but why it works that way.

---

### Contact

If you have any questions, feel free to reach out:

✉️ [mattis.pfenning@futureforests.uni-freiburg.de](mailto:mattis.pfenning@futureforests.uni-freiburg.de)
