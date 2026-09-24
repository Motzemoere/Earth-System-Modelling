# 🌍 Earth-System-Modelling -> Local Setup (Optional)

This guide is only needed if you want to work on your own laptop instead of [Google Colab](../README.md#getting-started-with-google-colab) (e.g. no reliable internet connection or to work offline).

We only need a handful of packages, so a plain Python installation with a virtual environment is enough.

## 1. Install Git

If you do not have Git installed on your system, download and install **Git** for your system:

🌐 [Git Downloads](https://git-scm.com/downloads)

## 2. Clone the Repository

Open up a terminal (Windows: search "Git Bash" in the Start menu; Mac: search "Terminal" in Spotlight), navigate to the folder where you want to store the course materials (e.g. `cd Documents`), and clone this repo:

```bash
git clone https://github.com/Motzemoere/Earth-System-Modelling.git
cd Earth-System-Modelling
```

Now you have this repository on your computer and can use and work with all the files.

## 3. Install Python
Download and install Python (3.10 or newer) from 🌐 [python.org](https://www.python.org/downloads/).

- **Windows:** tick **"Add python.exe to PATH"** at the bottom of the first installer screen.
- **macOS:** use the installer from python.org (the preinstalled system Python may be outdated).
- **Linux:** Python is usually already installed; you may need to install the `venv` module, e.g. `sudo apt install python3-venv`.

Check that it works by opening a terminal (Windows: "Command Prompt") and running `python --version` (macOS/Linux: `python3 --version`).

## 4. Create a Virtual Environment and Install the Packages
A virtual environment is a separate folder that holds the packages for this course, so they don't interfere with anything else on your laptop. In the terminal, go to the `Earth-System-Modelling` folder and run:

**Windows (Command Prompt):**
```bash
python -m venv .venv
.venv\Scripts\activate
pip install pandas numpy matplotlib ipykernel
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pandas numpy matplotlib ipykernel
```

You only need to do this once. `(.venv)` at the start of your terminal line shows the environment is active.

## 5. Install Your IDE of Choice
The IDE (integrated development environment) will facilitate coding with syntax highlighting, file browsing and many more useful things.

For this course it doesn't matter which IDE you use, but here are some examples. I would recommend VS Code (with the *Python* and *Jupyter* extensions).

[VS Code](https://code.visualstudio.com/) most commonly used in our field

[Spyder](https://www.spyder-ide.org/) most similar to R-Studio

[PyCharm](https://www.jetbrains.com/pycharm/) mostly used in web development

In any IDE, open the `Earth-System-Modelling` folder and select the `.venv` environment you created earlier as your Python interpreter / notebook kernel.

**Opening your first notebook in VS Code:**
1. Open the `Earth-System-Modelling` folder in VS Code (`File > Open Folder...`).
2. Install the **Jupyter** extension (one-time setup): click the Extensions icon in the left sidebar (or press `Ctrl+Shift+X`), search for "Jupyter", and click **Install** on the extension published by Microsoft.
3. In the file explorer on the left, click `tutorials/01_Python_Basics_and_Data_Structures.ipynb` to open it.
4. In the top-right corner of the notebook, click **Select Kernel** and choose the `.venv` environment you created in step 4.
5. Click into the first code cell and press **Shift+Enter** to run it and move to the next one. Repeat top to bottom for the whole notebook.

Now you are setup to start coding!

**Working offline:** the notebooks load the data from GitHub via the variable `DATA_URL`. Without internet, change it to the local `data` folder of your cloned repository:

```python
DATA_URL = '../data/'
```

## 6. Keeping Your Copy Up to Date

More materials will be added to this repository as the course progresses. Whenever new content is announced, open a terminal in the `Earth-System-Modelling` folder and run:

```bash
git pull
```

**Important:** Don't edit the tutorial notebooks directly, since git can't merge your changes with updates to the same file. Instead, work in a copy (e.g. save `tutorial_2.ipynb` as `tutorial_2_mywork.ipynb`) or in your own separate files. That way `git pull` will always go smoothly and never overwrite your work.

**If `git pull` refuses because of local changes:**

If you did edit a tracked file and see an error like `Your local changes would be overwritten by merge`, temporarily set your changes aside, pull, then bring them back:

```bash
git stash
git pull
git stash pop
```

This stores your edits, updates the repo, and then reapplies your edits on top. If `git stash pop` reports a conflict, don't try to resolve it blindly — reach out (see [Contact](../README.md#contact)) since it usually means you and the update changed the same lines.

Next
👉 **[Go to Tutorials](../tutorials/README.md)** skip the google colab part
