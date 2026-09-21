# Rent & Go Car Rental Management System
RENT & GO 🚗
Python-Based Car Rental Management System

RENT & GO is a command-line car rental management application developed using Python. The application allows users to manage vehicle data, perform CRUD operations, search and filter vehicles, sort vehicle data, manage rental and return transactions, and view vehicle statistics.

# 📌 Features

1. Read Data
-  View all vehicle data
-  Search by vehicle code
-  Search by vehicle brand
-  Search by rental price range
-  View available vehicles
-  Search by vehicle category
-  Filter by brand and status
-  Sort vehicle data
  
2. Create Data
   Users can add new vehicle data, including:
-  Vehicle code
-  Brand
-  Type
-  Category
-  Year
-  Daily rental price
-  Vehicle status
  
The system validates the vehicle code to ensure it is unique.

3. Update Data
   Users can update:
-  Brand
-  Type
-  Category
-  Year
-  Rental price
-  Status
  
The vehicle code is used to identify the vehicle that will be updated.

4. Delete Data
Users can:
-  Delete a single vehicle
-  Delete vehicles within a selected category
-  Vehicles with Rented status cannot be deleted.
-  The delete process includes confirmation steps to prevent accidental deletion.

5. Rental & Return
The rental menu allows users to:
-  View available vehicles
-  Rent an available vehicle
-  Calculate the total rental cost
-  Change vehicle status from Available to Rented
-  Return a rented vehicle
-  Change vehicle status from Rented back to Available

Rental cost is calculated using:
Total Rental Cost = Rental Duration × Daily Rental Price

6. Statistics
The application displays:
-  Total number of vehicles
-  Number of Available vehicles
-  Number of Rented vehicles
-  Number of Maintenance vehicle
 
7. Sorting
Vehicle data can be sorted by:
-  Cheapest rental price
-  Most expensive rental price
-  Newest vehicle year
-  Oldest vehicle year
-  Brand A-Z

# 🗂️ Data Structure

The application stores vehicle information using multiple Python lists. Each vehicle is represented across the same index position in each list.

List	Description	Example:
kodeMobil 	  |   Vehicle code	      |  M001
merkMobil	    |   Vehicle brand      	|  Toyota
tipeMobil	    |   Vehicle type	      |  Avanza
kategoriMobil	|   Vehicle category	  |  MPV
tahunMobil	  |   Vehicle year	      |  2020
hargaSewa	    |   Daily rental price	|  300000
statusMobil	  |   Vehicle status	    |  Available

For example:
kodeMobil[0]      # M001
merkMobil[0]      # Toyota
tipeMobil[0]      # Avanza
kategoriMobil[0]  # MPV
tahunMobil[0]     # 2020
hargaSewa[0]      # 300000
statusMobil[0]    # Available

The same index refers to the same vehicle.

Valid Categories
- MPV
- Sedan
- Hatchback
- SUV

Valid Statuses
- Available
- Rented
- Maintenance
  
🛠️ Technologies & Library
- Python
- tabulate

The tabulate library is used to display vehicle data in formatted tables in the command-line interface.

# ⚙️ Installation

1. Install Python
Make sure Python is installed on your computer.
Check your Python installation:
python --version
or:
py --version

2. Install Tabulate
Open Command Prompt or Terminal and run:
pip install tabulate
If pip does not work, try:
python -m pip install tabulate
or:
py -m pip install tabulate

▶️ How to Run

1. Open the project folder
Open the project folder in VS Code, Command Prompt, or Terminal.

2. Make sure the files are in the same folder
RENT-GO/
│
├── CAPSTONE PROJECT MODULE 2 NEW(4).py
└── README.me

3. Run the program
python "CAPSTONE PROJECT MODULE 2 NEW(4).py"

Or on Windows:

py "CAPSTONE PROJECT MODULE 2 NEW(4).py"

The main menu will appear:

=======WELCOME TO RENTAL & GO =======

List Menu:
1. Read Data
2. Create Data
3. Update Data
4. Delete Data
5. Rental Menu
6. Statistik Data Mobil
7. Exit Program
🔄 Application Flow
🧩 Program Structure
RENT & GO
│
├── Main Menu
│
├── Helper Functions
│   ├── inputAngka()
│   ├── cekStatus()
│   ├── cariIndex()
│   └── cekKategori()
│
├── Data Display
│   ├── cetakTabel()
│   ├── cetakTabelSewa()
│   └── cetakSemua()
│
├── Sorting
│   └── urutkanData()
│
├── Statistics
│   └── tampilStatistik()
│
├── Rental
│   └── menuRental()
│
├── Delete
│   └── menuDelete()
│
├── Create
│   └── menuCreate()
│
├── Read
│   └── menuRead()
│
├── Update
│   └── menuUpdate()
│
└── Program Execution
    └── menuUtama()
   
# 🧠 CRUD Operations
Operation	  |   Function	    |  Purpose
Create	    |   menuCreate()	|  Add new vehicle data
Read	      |   menuRead()	  |  View, search, filter, and sort data
Update	    |   menuUpdate()	|  Modify existing vehicle data
Delete	    |   menuDelete()	|  Remove vehicle data

# 🔐 Input Validation
The application includes:
- Vehicle code uniqueness validation
- Numeric input validation
- Vehicle category validation
- Vehicle status validation
- Vehicle existence validation
- Rental availability validation
- Rented vehicle deletion restriction
- Confirmation before important actions
  
# 📊 Initial Dataset
The application starts with 5 vehicles:
Code	|  Brand	    |  Type	    |  Category	  |  Year	|  Daily      |  Rental	Status
M001	|  Toyota	    |  Avanza	  |  MPV	      |  2020	|  Rp300,000	|  Available
M002	|  Honda	    |  Civic	  |  Sedan	    |  2019	|  Rp250,000	|  Available
M003	|  Suzuki	    |  Ertiga	  |  Hatchback	|  2021	|  Rp200,000	|  Rented
M004	|  Nissan	    |  X-Trail	|  SUV	      |  2018	|  Rp400,000	|  Maintenance
M005	|  Mitsubishi	|  Pajero	  |  SUV	      |  2020	|  Rp450,000	|  Available

# ⚠️ Notes
- This project is a command-line application.
- Vehicle data is stored in Python lists.
- The application does not use a database.
- Data changes are stored only while the program is running.
- Restarting the program will restore the initial dataset.
- The tabulate library is required to display formatted tables.

# 👩‍💻 Project Information
Project: RENT & GO
Type: Python-Based Car Rental Management System
Course: Capstone Project Module 2
Developer: Zafira Putri Suerman

# 🎯 Learning Objectives
This project was developed to practice:
- Python fundamentals
- CRUD operations
- Functions and modular programming
- Conditional statements and loops
- List manipulation
- Data filtering and sorting
- Input validation
- Basic application logic
- Problem-solving
- Implementation of business rules
