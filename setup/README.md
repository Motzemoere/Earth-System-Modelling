# 🌍 Earth-System-Modelling -> Setup

Here you find everything to set you up to start programming.

You can either install python and all the necessary programs on your laptop or use google colab to work entirely in the browser, then you don't have to install anything.

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

Now you are setup to start coding!

Next
👉 **[Go to Tutorials](tutorials/README.md)**