# 🌍 Earth-System-Modelling -> Setup

Here you find everything to set you up to start programming.

You can either install python and all the necessary programs on your laptop or use [Google Colab](https://colab.research.google.com/) to work entirely in the browser, then you don't have to install anything.

## Install Necessary Software on Your Laptop

### 1. Install Conda
If you do not have Conda installed, download and install **Miniforge** for your system. This allows you to have separate working environments to install programs and packages.

🌐 [Miniforge Releases](https://github.com/conda-forge/miniforge/releases?after=4.10.3-0)

You should now have access to the Miniforge prompt command terminal

### 2. Install Python and Required Packages
The easiest way is to just create the environment manually by running these commands in the miniforge prompt:
```bash
conda create -n esm python pandas numpy matplotlib ipykernel -y
conda activate esm
```

### 3. Install Your IDE of Choice
The IDE (integrated development environment) will facilitate coding with syntax highlighting, file browsing and many more useful things.

For this course it doesn't matter which IDE you use, but here are some examples. I would recommend VS Code.

[VS Code](https://code.visualstudio.com/) most commonly used in our field

[Spyder](https://www.spyder-ide.org/) most similar to R-Studio

[PyCharm](https://www.jetbrains.com/pycharm/) mostly used in web development

After installing the IDE you should be able to select your python environment "esm" you created earlier.

Now you are setup to start coding!

New materials get added to the repository as the course goes on — see [Keeping Your Copy Up to Date](../README.md#3-keeping-your-copy-up-to-date) in the main README for how to fetch them.

Next
👉 **[Go to Tutorials](tutorials/README.md)**


## Using Google Colab

Go to [Google Colab](https://colab.research.google.com/) and open up a new notebook

All the packages we need are already installed in google colab you can just import them by running:

```python
import pandas
import numpy
import matplotlib
```

### Getting the Data into Colab

Colab can't see the files on your laptop, so put the data on Google Drive and connect ("mount") your Drive to the notebook:

1. Download the `data` folder from this repository and upload it to your [Google Drive](https://drive.google.com/), e.g. into a folder `MyDrive/ESM/data`.
2. In your Colab notebook, mount Google Drive by running the following cell and allowing access when asked:

```python
from google.colab import drive
drive.mount('/content/drive')
```

3. Your Drive files are now available under `/content/drive/MyDrive/`, so you can load the data like this:

```python
import pandas as pd
data = pd.read_csv('/content/drive/MyDrive/ESM/data/Data_swbm_Germany.csv')
```

You can also browse your Drive files via the 📁 folder icon on the left sidebar of Colab (right-click a file → "Copy path" to get its path). You need to re-run the mount cell every time you open the notebook in a new session.

Now you are setup to start coding!

Since Colab doesn't use git, when new materials are announced just re-open or re-upload the updated notebook rather than reusing your old copy — keep any of your own work in a separate copy first.

Next
👉 **[Go to Tutorials](tutorials/README.md)**
