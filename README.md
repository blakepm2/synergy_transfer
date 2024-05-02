# 🧬 Synergy Transfer

**Synergy Transfer** is a deep learning model that can predict synergies between various drugs to aid in cancer research.

> [!NOTE]
> This project is an attempt to reproduce the results from the paper **"Anti-Cancer Drug Synergy Prediction in Understudied Tissues Using Transfer Learning"** by [Kim et al. (2020)](https://doi.org/10.1101/2020.02.05.932657). Most of the original code has been reused, with only necessary modifications made to resolve dependency issues and perform ablation studies. 

The original publication can be accessed [here](https://academic.oup.com/jamia/article-abstract/28/1/42/5920819?redirectedFrom=fulltext&login=false). And the original publication GitHub repoitory can be accessed [here](https://github.com/yejinjkim/synergy-transfer). 

## 🎯 Purpose

A significant challenge faced in the drug discovery for cancer research is the uneven distribution of data for particular types of cancers and tissues. [Kim et al. (2020)](https://doi.org/10.1101/2020.02.05.932657) present a novel solution using a deep neural network that uses transfer learning to learn from the abundance of examples within data-rich tissues and enhance predictions in data-poor tissues.

## 🚀  Usage

### Step 1: Clone this Repository

First you need to clone this repo to your local machine. The instructions below are adapted from [GitHub's documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) on cloning repositories; for more information, please refer to the [docs](https://docs.github.com/en).

<details><summary><b>Show instructions</b></summary>

1. Navigate to the main page of the repository.

2. Above the list of files, click **<> Code**.

3. Copy the URL for the repository.
    - To clone the repository using HTTPS, under "HTTPS", click **Copy**.

4. Open Git Bash.

5. Change the current working directory to the location where you want the cloned repository. e.g.
    ```
    cd path/to/folder
    ```

6. Type `git clone`, and then paste the URL you copied earlier, e.g.
    ```
    git clone https://github.com/blakepm2/synergy_transfer
    ```

7. Press **Enter** to create your local clone.

</details>


### Step 2: Download the data

### Step 3: Set up your environment

### Step 4: Run `final.ipynb`

