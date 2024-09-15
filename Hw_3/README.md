## Homework 3 Assignment

1. Familiarize yourself with general information about the MongoDB database, which is provided in the lecture material, as well as in sources [1, 2, 3].
2. Read the MongoDB database installation instructions below.
3. Install the MongoDB DBMS and its graphical client Compass on the workstation.
4. Configure the operating system for working with the MongoDB database on the workstation.
5. Make a report on laboratory work.

## Homework 3 Report

1. **[Connection to MongoDB Atlas using Python](Connect_to_MongoDB.py)**
    #### Steps to run the script:

   - **Create a env file:**
   ```sh
    touch .env
   ```
   - **Open env file:**
   ```sh
   nano .env 
   ```
    - **Add the URI password to the env file:**
    ```sh
    URI=mongodb+srv://<db_user>:<db_password>@<cluster_url>/?retryWrites=true&w=majority&appName=<Cluster_name>
    ```
   <br>

   1. Replace `<db_user>` with your database user.
   2. Replace `<db_password>` with your database password.
   3. Replace `<cluster_url>` with your cluster URL.
   4. Replace `<Cluster_name>` with your cluster name.
   <br><br>
    - **Run the script:**
    ```sh
    python3 Connect_to_MongoDB.py
    ```

    