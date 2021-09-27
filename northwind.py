import sqlite3
import pandas as pd
# Python
curs.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY
name;").fetchall()
[('Category',), ('Customer',), ('CustomerCustomerDemo',),
('CustomerDemographic',), ('Employee',), ('EmployeeTerritory',), ('Order',),
('OrderDetail',), ('Product',), ('Region',), ('Shipper',), ('Supplier',),
('Territory',)]

CONN = sqlite3.connect('/Users/Josh/PycharmProject/pythonProject/northwind_small.sqlite3')
def run_queries():
    # Part 2
    expensive_items = 'SELECT * FROM Product ORDER BY UnitPrice DESC LIMIT 10;'
    avg_hire_age = 'SELECT *  FROM (Birthdate - HireDate) AVG([ALL]);'
    age_by_city = ('SELECT City, AVG(HireDate - BirthDate) FROM Employee '
                   'GROUP BY City;')
    # Part 3
    item_suppliers = ('SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName '
                      'FROM Product Product, Supplier Supplier WHERE Product.SupplierId = Supplier.Id '
                      'ORDER BY Product.UnitPrice DESC LIMIT 10;')
    largest_category = ('SELECT Category.CategoryName, COUNT(DISTINCT p.Id) '
                        'FROM Category Category, Product Product WHERE Category.Id = Product.CategoryId '
                        'GROUP BY 1 ORDER BY 2 DESC LIMIT 1;')
    employee = ('SELECT Employee.Id, Employee.FirstName, Employee.LastName, COUNT(DISTINCT TerritoryId.Id) '
                'FROM Territory Territory, Employee Employee, EmployeeTerritory EmployeeTerritory '
                'WHERE Employee.Id = EmployeeTerritory.EmployeeId AND TerritoryId.id = EmployeeTerritory.TerritoryId '
                'GROUP BY 1, 2, 3 ORDER BY 4 DESC LIMIT 1;')
    # Put them all together, run them, print the results
    queries = (expensive_items, avg_hire_age, age_by_city, item_suppliers,
               largest_category, employee)
    curs = CONN.cursor()
    for query in queries:
        print(curs.execute(query).fetchall())
if __name__ == "__main__":
    run_queries()



# # Ten most expensive items (per unit price) in the game
#
# conn = sqlite3.connect("northwind_small/OrderDetails.sqlite3")
# def expensive_items():
#     curs = conn.cursor()
#     print(curs.execute('SELECT(*) FROM Product ORDER BY Unit Price DESC LIMIT 10);')
# if __name__ == "__main__":
#     expensive_items()
# # expensive_items = conn.nlargest(10, ['UnitPrice'])
#
# # What is the average age of an employee at the time of their hiring?
# conn = sqlite3.connect("northwind_small/Employee.sqlite3")
# def calculate_age():
#     curs = conn.cursor()
#     print(curs.execute('Select(*) FROM BirthDate MINUS HireDate AVG([ALL]);')
# if __name__ == "__main__":
#     calculate_age()
#
# # How does the average age of employee at hire vary by city?
# conn = sqlite3.connect("northwind_small/Employee.sqlite3")
# def avg_age_by_city():
#     curs = conn.cursor()
#     print(curs.execute('Select(*) FROM BirthDate MINUS HireDate AVG([ALL]) GROUP BY City);')
# if __name__ == "__main__":
#     avg_age_by_city()
#
# # Part 3
#
# # hat are the ten most expensive items (per unit price) in the database and their suppliers?
# conn = sqlite3.connect("northwind_small/Product.sqlite3")
# def ten_most_expensive():
#         curs = conn.cursor()
#         print(curs.execute('SELECT(*) FROM Product ORDER BY Unit Price DESC LIMIT 10 FROM Product INNER JOIN Supplier ON Product.SupplierId = Supplier.Id);')
# if __name__ == "__main__":
#         ten_most_expensive()
#
#         conn = sqlite3.connect("northwind_small/OrderDetails.sqlite3")
#
# # What is the largest category (by number of unique products in it)
# def largest_category():
#     curs = conn.cursor()
#     print(curs.execute('SELECT(DISTINCT) FROM Product ORDER BY CategoryId INNER JOIN Product ON Product.CategoryId = Category.Id);')
# if __name__ == "__main__":
#                 largest_category()
#
#         # born = conn['BirthDate'].date()
#     # hired = conn['HireDate'].date()
# #     return born.year - hire.year - ((hire.month, hire.day) < (born.month, born.day))
# # # Create column of age at hire
# # df['age_hired'] = df['col19'].apply(calculate_age)
#
# # print(expensive_items)
# #
# # # Average age of employee at time of hiring
# # df = pd.read_csv("northwind_small/Employee.sqlite3")
# #
# # # Create a function that calculates age from at hire date
# #
# #
# # # Save and print the average age at hire
# # avg_hire_age = df['age_hired'].mean()
# #
# # print(avg_hire_age)
# #
# # # STRETCH: average age by city
# #
# # avg_age_by_city = ...
# #
# # # SQLITE
# #
# # curs.execute('SELECT sql FROM sqlite_master WHERE name="Customer";').fetchall()
# # [('CREATE TABLE "Customer" \n(\n  "Id" VARCHAR(8000) PRIMARY KEY, \n
# # "CompanyName" VARCHAR(8000) NULL, \n  "ContactName" VARCHAR(8000) NULL, \n
# # "ContactTitle" VARCHAR(8000) NULL, \n  "Address" VARCHAR(8000) NULL, \n  "City"
# # VARCHAR(8000) NULL, \n  "Region" VARCHAR(8000) NULL, \n  "PostalCode"
# # VARCHAR(8000) NULL, \n  "Country" VARCHAR(8000) NULL, \n  "Phone" VARCHAR(8000)
# # NULL, \n  "Fax" VARCHAR(8000) NULL \n)',)]
# #
# # # Ten most expensive items (per unit price) in the game
# #
# # ten_most_expensive =
# #
# # # Average age of employee at time of hiring
# #
# # avg_hire_age =