# Homework 8 Assignment

1. Design Graph Database
2. Create Graph Database
3. Load Data
4. CRUD Operations

# Design Graph Database

### **Nodes:**
- **Pharmacy**: represents the pharmacy.
- **Medication**: represents medication.
- **Booking**: Represents a medication booking.
- **Manufacturer**: represents the drug manufacturer.
- **Sales**: represents drug sales.
- **Residues**: represents the remaining medication in the pharmacy.

### **Connections:**
* **HAS**: connection between pharmacy and balances.
* **MANUFACTURES**: The connection between the manufacturer and the medicine.
* **SELLS**: connection between pharmacy and sales.
* **RESERVES**: the connection between the pharmacy and the reservation.
* **CONTAINS**: relationship between residues and medicines.
* **SELLS**: The connection between sales and medicine.
* **BOOKS**: the connection between booking and medicine.


# Homework 8 Report

1. Design Graph Database in  **[Design Graph Database](#design-graph-database)**
2. Implement Custom Class for working with Neo4j in **[neo4j_functions.py](neo4j_functions.py)**
3. Implement CRUD operations in **[Neo4j.ipynb](Neo4j.ipynb)**
4. Implement tests by pytest in **[test_neo4j.py](test_neo4j.py)**