# NoSQL Labs - Ivan Franko University

This repository contains laboratory works for the NoSQL course at Ivan Franko University. The labs are designed to provide hands-on experience with NoSQL databases.

## Table of Contents

- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Running the Labs](#running-the-labs)
- [MongoDB Connection](#mongodb-connection)
- [License](#license)

## Repository Structure

- **[Hw_2/](Hw_2/)**: Contains the second laboratory work.
  - **[Trends_of_NoSQL.md](Hw_2%2FTrends_of_NoSQL.md)**: Trends of NoSQL databases.
  - **[SQL-NoSql_Comparison.md](Hw_2/SQL-NoSql_Comparison.md)**: Comparison between relational and NoSQL databases.
  - **[README.md](Hw_2/README.md)**: Instructions and details for the second lab.
- **[Hw_3/](Hw_3/)**: Contains the third laboratory work.
  - **[Connect_to_MongoDB.py](Hw_3/Connect_to_MongoDB.py)**: Python script to connect to MongoDB.
  - **[README.md](Hw_3/README.md)**: Instructions and details for the third lab.
- **[Hw_4/](Hw_4/)**: Contains the fourth laboratory work.
  - **[Create_and_load_data_to_MongoDB.ipynb](Hw_4/Create_and_load_data_to_MongoDB.ipynb)**: Ipynb file to work with MongoDB collections.
  - **[README.md](Hw_4/README.md)**: Instructions and details for the fourth lab. 

- **[.gitignore](.gitignore)**: Specifies files and directories to be ignored by Git.
- **[README.md](README.md)**: This file, providing an overview of the repository.
- **[LICENSE](LICENSE)**: The license for the repository.
- **[requirements.txt](requirements.txt)**: Contains the required Python packages for the labs.

## Getting Started

1. **Clone the repository:**
   ```sh
   git clone https://github.com/99bruno/NoSQL_LNU.git
   ```
2. **Go to the repository directory:**
   ```sh
   cd NoSQL_LNU
   ```
   
3. **Create a virtual environment:**
    ```sh
    python -m venv .venv
    ```
   
4. **Set up the virtual environment:**
    ```sh
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

5. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

## Running the Labs

Each lab can be run independently. Navigate to the respective lab directory and execute the Python script.

- ### For example, to run the first lab:

  1. **Navigate to the third lab directory:**
      ```sh
      cd Hw_3
      ```

  2. **Run the Python script:**
      ```sh
      python Connect_to_MongoDB.py
      ```

Repeat the above steps for others.

## MongoDB Connection

Ensure you have a MongoDB instance running and update the connection URI in each script as needed.

## License

This project is licensed under the MIT **[LICENSE](LICENSE)**. See the LICENSE file for details.