# Project Setup Guide

## Setting up the environment:

1. **Create a virtual environment** in the project directory:
    ```bash
    python3 -m venv venv
    ```

2. **Activate the virtual environment**:
    - For macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
    - For Windows:
      ```bash
      .\venv\Scripts\activate
      ```

3. **Install dependencies** from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

4. **Adding new packages**:
    - If you add a new package, don't forget to update the `requirements.txt` by running the following command in the project directory:
      ```bash
      pip freeze > requirements.txt
      ```

---

## Setting up the Scraping File:

- To run the scraping file, you should create a `.env` file in the main directory to define the project directory in your system. This file **is not uploaded on GitHub**.

    Example `.env` file:
    ```
    PROJECT_DIR=/path/to/main/directory/
    ```

This environment setup will ensure that your project runs smoothly and dependencies are properly managed.
