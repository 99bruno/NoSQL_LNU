## Homework 4 Assignment

1. On the topic of the course project in the discipline **"Organization of databases and data warehouses"**, which you performed in the 2nd year, design a documentary database that would consist of 2 collections. 
   - In each collection, describe 5 documents in JSON format
   - One of the documents must contain an array
   - One of the documents must contain an attachment

## Homework 4 Report

1. **[Create and load data to MongoD](Create_and_load_data_to_MongoDB.ipynb)** 
    #### Steps to run the script:
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
    jupyter notebook Create_and_load_data_to_MongoDB.ipynb
    ```