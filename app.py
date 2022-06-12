import sqlite3

class System:
    def __init__(self, salesman_number, salesman_name, salesman_gender, salesman_age, salesman_address) -> None:
        self.salesman_number = salesman_number
        self.salesman_name = salesman_name
        self.salesman_gender = salesman_gender
        self.salesman_age = salesman_age
        self.salesman_address = salesman_address
        self.database = sqlite3.connect("SalesFile.db")
        self.cursor = self.database.cursor()
    
    def create_salesman(self): 
        b = self.database.cursor()
        c = b.execute("SELECT salesman_no FROM salesman WHERE salesman_name = ?", (self.salesman_name,))
        if b.fetchone():
            return False
        else:
            sql = '''INSERT INTO salesman (salesman_number, salesman_name,
                            salesman_gender,
                            salesman_age,
                            salesman_address) 
                            VALUES(?, ?, ?, ?, ?)'''

            value = (self.salesman_number, self.salesman_name, self.salesman_gender, self.salesman_age, self.salesman_address)
                
            self.database.execute(sql, value)

            self.database.commit()
            return True
        
        #self.database.close()
    @staticmethod
    def delete_salesman(salesman):

        database = sqlite3.connect("SalesFile.db")

        sql = "DELETE from salesman where salesman_number = ?"

        value = (salesman,)

        database.execute(sql, value)

        database.commit()

        #self.database.close()
        return True

    #This will diplay raw data from the database
    def display_salesman(self):

        cursor = self.database.cursor()

        cursor.execute("SELECT * FROM salesman")

        rows = cursor.fetchall()

        return rows
    
    def update_salesman(self):
        #self.new_name = new_name
        #sql2 = """UPDATE sales SET salesman_name = ? where salesman_name = ?"""
        #value2 = (self.new_name, self.salesman_name,)

        #self.database.execute(sql2, value2)       
        
        sql = """UPDATE  salesman SET salesman_name = ?, salesman_gender = ?,
                         salesman_age = ?, salesman_address = ? where salesman_number = ?"""

        value = (self.salesman_name, self.salesman_gender, self.salesman_age, self.salesman_address, self.salesman_number)

        self.database.execute(sql, value)

        self.database.commit()

        return True
        #Sales_system sales table updating the salesman_name






class Sales_system(System):
    def __init__(self, salesman_name, salesman_gender, salesman_age, salesman_address, sales_product_name, sales_stock, sales_quantity, sales_unit,
                       sales_description, sales_price, sales_amount, sales_commission, sales_net_amount ) -> None:
        super().__init__(self, salesman_name, salesman_gender, salesman_age, salesman_address)
        self.sales_product_name = sales_product_name
        self.sales_stock = sales_stock
        self.sales_quantity = sales_quantity
        self.sales_unit = sales_unit
        self.sales_description = sales_description
        self.sales_price = sales_price
        self.sales_amount = sales_amount
        self.sales_commission = sales_commission
        self.sales_net_amount = sales_net_amount

    def create_sales(self):
        sql = """
            INSERT INTO sales (salesman_name, sales_name, sales_stock, sales_quantity, sales_unit, sales_description, sales_price, sales_amount, sales_commission, sales_net_amount)
                               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        value = (self.salesman_name, self.sales_product_name, self.sales_stock, self.sales_quantity, self.sales_unit, self.sales_description, self.sales_price, self.sales_amount,
                 self.sales_commission, self.sales_net_amount)

        cursor = self.database.cursor()

        cursor.execute(sql,value)

        self.database.commit()
        return True
    def update_sales(self):
        sql = """UPDATE sales SET salesman_name = ?, sales_stock = ?, sales_quantity = ?, sales_description = ?, sales_price = ?,
                                  sales_amount = ?, sales_commission = ? , sales_net_amount = ? where sales_name = ?"""

        value = (self.salesman_name, self.sales_stock, self.sales_quantity, self.sales_description, self.sales_price,self.sales_amount, self.sales_commission, 
                 self.sales_net_amount, self.sales_product_name)

        cursor = self.database.cursor()

        cursor.execute(sql, value)

        self.database.commit()

    def delete_sales(self):
        sql = "DELETE from sales where sales_name = ?"

        value = (self.sales_product_name,)

        cursor = self.database.cursor()

        cursor.execute(sql, value)

        self.database.commit()