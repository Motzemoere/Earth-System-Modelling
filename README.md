# 🌍 Earth-System-Modelling

This repository contains **materials** used in the **Earth System Modelling** course.  
It is designed to set you up with everything you need to finish the course. More materials will be added during the course.

---

## Download the Materials

### 1. Install Git

If you do not have Git installed on your system, download and install **Git** for your system:

🌐 [Git Downloads](https://git-scm.com/downloads)

### 2. Clone the Repository

Open up a terminal (Windows: search "Git Bash" in the Start menu; Mac: search "Terminal" in Spotlight), navigate to the folder where you want to store the course materials (e.g. `cd Documents`), and clone this repo:

```bash
git clone https://github.com/Motzemoere/Earth-System-Modelling.git
cd Earth-System-Modelling
```

Now you have this repository on your computer and can use and work with all the files.

### 3. Keeping Your Copy Up to Date

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

This stores your edits, updates the repo, and then reapplies your edits on top. If `git stash pop` reports a conflict, don't try to resolve it blindly — reach out (see [Contact](#contact)) since it usually means you and the update changed the same lines.


## Setup Python

**New to Python?** Start with installing the necessary software to work with this repository.

👉 **[Go to Setup](setup/README.md)**

These steps show you how to setup python on your local machine or use Google Colab in the browser.

---

## Python Tutorials

**New to Python?** Start with the tutorial series that teaches you everything you need to understand and build environmental models!

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
