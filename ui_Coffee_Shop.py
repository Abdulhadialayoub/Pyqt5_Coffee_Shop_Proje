from xlsxwriter import Workbook
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUiType
import pymysql as mycon
import datetime
def ui_loading():
    global ui
    ui, _ = loadUiType('Coffee_Shop.ui')

# Load the UI at module level
ui_loading()

class MainApp(QMainWindow, ui):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self.Handle_Buttons()
        self.Handel_UI_Changes()
        self.Show_Stock()
        self.Show_Stock_in_Order()
        self.Show_User_Table()
        self.Show_Order_Table()
        self.Dark_Orange_Theme()
        self.Show_Dashbored()
        self.Total_Customer()
        self.Today_income()
        self.Total_income()
    ##########################################
    ####      Buttons For Programs   #########
    def Handle_Buttons(self):
        self.pushButton_17.clicked.connect(self.Hiding_Themes)
        self.pushButton_5.clicked.connect(self.Show_Themes)
        self.pushButton_2.clicked.connect(self.order_tab)
        self.pushButton.clicked.connect(self.Open_stock_Tab)
        self.pushButton_3.clicked.connect(self.Open_Dashbord_Tab)
        self.pushButton_4.clicked.connect(self.Open_Settings_Tab)
        self.pushButton_6.clicked.connect(self.Add_iteam)
        self.pushButton_9.clicked.connect(self.clear_Editline)
        self.pushButton_8.clicked.connect(self.Update_iteam)
        self.pushButton_7.clicked.connect(self.Delete)
        self.pushButton_10.clicked.connect(self.order)
        self.pushButton_11.clicked.connect(self.Delete_Order)
        self.pushButton_12.clicked.connect(self.clear_order)
        self.pushButton_13.clicked.connect(self.Pay_Order)
        self.pushButton_14.clicked.connect(self.Refresh_dashbord)
        self.pushButton_15.clicked.connect(self.Edit_User)
        self.pushButton_16.clicked.connect(self.Delete_User)
        self.pushButton_18.clicked.connect(self.clear_User)
        self.pushButton_19.clicked.connect(self.Export_Dashbored)
        self.pushButton_20.clicked.connect(self.Refresh)
        self.pushButton_21.clicked.connect(self.Add_User)
        self.pushButton_22.clicked.connect(self.Dark_Blue_Theme)
        self.pushButton_23.clicked.connect(self.Dark_Gray_Theme)
        self.pushButton_24.clicked.connect(self.Dark_Orange_Theme)
        self.pushButton_25.clicked.connect(self.QDark_Theme)
        self.pushButton_26.clicked.connect(self.Refresh_Order)
        self.pushButton_27.clicked.connect(self.Hesapla)
        self.pushButton_28.clicked.connect(self.Export_Stock)





    ########################################
    ######### opening tabs #################

    def order_tab(self):
        self.tabWidget.setCurrentIndex(1)
    def Open_stock_Tab(self):
        self.tabWidget.setCurrentIndex(0)
    def Open_Dashbord_Tab(self):
        self.tabWidget.setCurrentIndex(2)
    def Open_Settings_Tab(self):
        self.tabWidget.setCurrentIndex(3)

    def Handel_UI_Changes(self):
        self.Hiding_Themes()
        self.tabWidget.tabBar().setVisible(False)

    def Hiding_Themes(self):
        self.groupBox_3.hide()

    def Show_Themes(self):
        self.groupBox_3.show()
    #############################
    ###       Stock Tab      ####
    def Refresh(self):
        self.Show_Stock()
    def showmsg(self):
        msg = QMessageBox()
        msg.setWindowTitle("ERROR")
        msg.setText("Please Fill The Spaces")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
    def empty(self):
        if self.lineEdit_9.text() == "" or self.lineEdit.text() == "" or self.lineEdit_2.text() == "" or self.lineEdit_10.text() == "" or self.lineEdit_3.text()=="":
            return True
        else:
            return False
    def Show_Stock(self):
        self.db = mycon.connect(host='localhost', user='root', password="", db='coffe_shop')
        self.cur = self.db.cursor()
        self.cur.execute(''' 
                   SELECT * FROM `products`
                ''')
        data = self.cur.fetchall()
        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(0)
        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            self.tableWidget.itemSelectionChanged.connect(self.onItemSelected)

    def onItemSelected(self):
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            pro_type_item = self.tableWidget.item(row, 3)
            pro_name_item = self.tableWidget.item(row, 2)
            pro_price_item = self.tableWidget.item(row, 5)
            pro_id_item = self.tableWidget.item(row, 1)
            pro_qty_item = self.tableWidget.item(row, 4)

            if pro_type_item and pro_name_item and pro_price_item and pro_id_item and pro_qty_item:
                self.lineEdit_9.setText(pro_type_item.text())
                self.lineEdit.setText(pro_name_item.text())
                self.lineEdit_2.setText(pro_price_item.text())
                self.lineEdit_10.setText(pro_id_item.text())
                self.lineEdit_3.setText(pro_qty_item.text())
    def Export_Stock(self):
        try:
            self.db = mycon.connect(host='localhost', user='root', password='', db='coffe_shop')
            self.cur = self.db.cursor()

            self.cur.execute(''' 
                        SELECT id, pro_id, pro_name, pro_type, pro_price, pro_stock, date_insert, date_update FROM products
                    ''')
            data = self.cur.fetchall()
            file_path = 'Stock.xlsx'
            # Check if the file already exists
            if os.path.exists(file_path):
                os.remove(file_path)
            wb = Workbook(file_path)
            sheet1 = wb.add_worksheet()
            # Define column headers
            sheet1.write(0, 0, 'ID')
            sheet1.write(0, 1, 'Product ID')
            sheet1.write(0, 2, 'Product Name')
            sheet1.write(0, 3, 'Product Type')
            sheet1.write(0, 4, 'Product Price')
            sheet1.write(0, 5, 'Product Stock')
            sheet1.write(0, 6, 'Date Inserted')
            sheet1.write(0, 7, 'Date Updated')
            # Fill data into the worksheet
            row_number = 1
            for row in data:
                column_number = 0
                for item in row:
                    sheet1.write(row_number, column_number, str(item))
                    column_number += 1
                row_number += 1
            wb.close()
            QMessageBox.information(None, 'Success', 'Stock Report Created Successfully')
        except mycon.Error as e:
            QMessageBox.critical(None,'Database Error', f"An error occurred: {e}")
    def Add_iteam(self):
        if self.empty():
            self.showmsg()
        else:
            try:
                pro_type = self.lineEdit_9.text()
                pro_name = self.lineEdit.text()
                pro_price = self.lineEdit_2.text()
                pro_id = self.lineEdit_10.text()
                pro_qty = self.lineEdit_3.text()
                today = datetime.date.today()

                mydb = mycon.connect(host="localhost", user="root", password="", database="coffe_shop")
                mycursor = mydb.cursor()

                # Check if pro_id already exists
                mycursor.execute("SELECT * FROM products WHERE pro_id = %s", (pro_id,))
                existing_product = mycursor.fetchone()
                if existing_product:
                    QMessageBox.warning(self, "Error", "Product ID already exists.")
                    return

                # Insert new product
                sql = "INSERT INTO products (pro_type, pro_name, pro_price, pro_id, pro_stock, date_insert) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (pro_type, pro_name, pro_price, pro_id, pro_qty, today)
                mycursor.execute(sql, values)
                mydb.commit()

                QMessageBox.information(self, "Success", "Product added successfully.")
                self.Show_Stock()  # Refresh table

            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

    def clear_Editline(self):
        self.lineEdit_9.clear()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_10.clear()
        self.lineEdit_3.clear()

    def Update_iteam(self):
        if self.empty():
            self.showmsg()
        else:
            try:
                pro_type = self.lineEdit_9.text()
                pro_name = self.lineEdit.text()
                pro_price = self.lineEdit_2.text()
                pro_id = self.lineEdit_10.text()
                pro_qty = self.lineEdit_3.text()
                today = datetime.date.today()

                mydb = mycon.connect(host="localhost", user="root", password="", database="coffe_shop")
                mycursor = mydb.cursor()

                # Check if product exists
                mycursor.execute("SELECT * FROM products WHERE pro_id = %s", (pro_id,))
                existing_product = mycursor.fetchone()
                if not existing_product:
                    QMessageBox.warning(self, "Error", "Product ID does not exist.")
                    return

                # Update product
                sql = "UPDATE products SET pro_type = %s, pro_name = %s, pro_price = %s, pro_stock = %s, date_update = %s WHERE pro_id = %s"
                values = (pro_type, pro_name, pro_price, pro_qty, today, pro_id)
                mycursor.execute(sql, values)
                mydb.commit()

                QMessageBox.information(self, "Success", "Product updated successfully.")
                self.Show_Stock()
                self.lineEdit_9.clear()
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_10.clear()
                self.lineEdit_3.clear()
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

    def Delete(self):
        pro_id = self.lineEdit_10.text()
        if pro_id == "":
            QMessageBox.warning(self, "Error", "Please enter a product ID.")
            return
        try:
            mydb = mycon.connect(host="localhost", user="root", password="", database="coffe_shop")
            mycursor = mydb.cursor()
            # Check if product exists
            mycursor.execute("SELECT * FROM products WHERE pro_id = %s", (pro_id,))
            existing_product = mycursor.fetchone()
            if not existing_product:
                QMessageBox.warning(self, "Error", "Product ID does not exist.")
                return
            # Delete product
            sql = "DELETE FROM products WHERE pro_id = %s"
            mycursor.execute(sql, (pro_id,))
            mydb.commit()
            QMessageBox.information(self, "Success", "Product deleted successfully.")
            self.Show_Stock()  # Refresh table
            self.lineEdit_9.clear()
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_10.clear()
            self.lineEdit_3.clear()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    #############################
    ###       Order Tab       ####
    def Refresh_Order(self):
        self.Show_Order_Table()
        self.Show_Stock_in_Order()
    def Show_Stock_in_Order(self):
        self.db = mycon.connect(host='localhost', user='root', password="", db='coffe_shop')
        self.cur = self.db.cursor()
        self.cur.execute(''' 
                           SELECT * FROM `products`
                        ''')
        data = self.cur.fetchall()

        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.insertRow(0)
        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1
            row_position = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_position)
            self.tableWidget_2.itemSelectionChanged.connect(self.onItemSelected_Order)

    def onItemSelected_Order(self):
                selected_items = self.tableWidget_2.selectedItems()
                if selected_items:
                    row = selected_items[0].row()
                    pro_type_item = self.tableWidget_2.item(row, 3)
                    pro_name_item = self.tableWidget_2.item(row, 2)
                    pro_price_item = self.tableWidget_2.item(row, 5)
                    pro_id_item = self.tableWidget_2.item(row, 1)

                    if pro_type_item and pro_name_item and pro_price_item and pro_id_item:
                        self.lineEdit_11.setText(pro_type_item.text())
                        self.label_10.setText(pro_name_item.text())
                        self.label_9.setText(pro_price_item.text())
                        self.lineEdit_12.setText(pro_id_item.text())
    def Show_Order_Table(self):
        self.db = mycon.connect(host='localhost', user='root', password="", db='coffe_shop')
        self.cur = self.db.cursor()
        self.cur.execute(''' 
                                   SELECT * FROM `orders`
                                ''')
        data = self.cur.fetchall()
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.insertRow(0)
        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1
            row_position = self.tableWidget_3.rowCount()
            self.tableWidget_3.insertRow(row_position)
            self.tableWidget_3.itemSelectionChanged.connect(self.on_item_clicked_order)

    def order(self):
        try:
            # Retrieve data from input fields
            pro_id = self.lineEdit_12.text()  # QLineEdit for product ID
            pro_name = self.label_10.text()  # QLabel for product name
            pro_type = self.lineEdit_11.text()  # QLineEdit for product type
            pro_price = self.label_9.text()  # QLabel for product price
            qty = self.spinBox.value()  # QSpinBox for quantity
            order_date = datetime.date.today()
            # Check if any of the fields are empty
            if not pro_id or not pro_name or not pro_type or not pro_price or qty <= 0:
                QMessageBox.warning(self, "Input Error", "All fields are required.")
                return
            # Validate that pro_price is a number
            try:
                pro_price = float(pro_price)
            except ValueError:
                QMessageBox.warning(self, "Input Error", "Price must be a valid number.")
                return
            # Calculate the total price
            total_price = qty * pro_price
            # Connect to the database
            self.db = mycon.connect(host='localhost', user='root', password='', database='coffe_shop')
            self.cur = self.db.cursor()
            # Disable autocommit mode
            self.db.autocommit = False
            # Retrieve the highest customer_id from the orders table
            self.cur.execute("SELECT MAX(customer_id) FROM orders")
            result = self.cur.fetchone()
            if result and result[0] is not None:
                custID = result[0] + 1
            else:
                custID = 1
            # Retrieve current stock from products table
            self.cur.execute("SELECT pro_stock FROM products WHERE pro_id = %s", (pro_id,))
            result = self.cur.fetchone()
            if result is None:
                QMessageBox.warning(self, "Input Error", "Product ID not found.")
                self.db.rollback()
                return
            current_stock = result[0]
            # Check if there is enough stock
            if current_stock < qty:
                QMessageBox.warning(self, "Stock Error", "Not enough stock available.")
                self.db.rollback()
                return
            # Update the product stock
            new_stock = current_stock - qty
            self.cur.execute("UPDATE products SET pro_stock = %s WHERE pro_id = %s", (new_stock, pro_id))

            # Insert the order into the database with the new customer_id
            sql = """
            INSERT INTO orders (customer_id, pro_id, pro_name, pro_type, pro_price, order_date,qty, total_price)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (custID, pro_id, pro_name, pro_type, pro_price, order_date,qty, total_price)
            self.cur.execute(sql, values)
            # Commit the transaction
            self.db.commit()
            # Provide user feedback
            QMessageBox.information(self, "Success", f"Order placed successfully. Total Price: {total_price}")
            self.Show_Stock_in_Order()
            self.Show_Order_Table()
        except mycon.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error: {err}")
            self.db.rollback()  # Rollback in case of error

    def Delete_Order(self):
        try:
            # Retrieve selected row
            selected_items = self.tableWidget_3.selectedItems()
            if not selected_items:
                QMessageBox.warning(self, "Selection Error", "Please select an order to delete.")
                return
            row = selected_items[0].row()
            order_id_item = self.tableWidget_3.item(row, 0)  # Assuming order_id is in the first column
            if not order_id_item:
                QMessageBox.warning(self, "Selection Error", "Invalid selection.")
                return
            order_id = order_id_item.text()
            # Confirm deletion
            reply = QMessageBox.question(self, 'Confirm Deletion',
                                         "Are you sure you want to delete this order?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.No:
                return
            # Connect to the database
            self.db = mycon.connect(host='localhost', user='root', password='', database='coffe_shop')
            self.cur = self.db.cursor()
            # Delete the order
            self.cur.execute("DELETE FROM orders WHERE customer_id = %s", (order_id,))
            # Commit the transaction
            self.db.commit()
            # Provide user feedback
            QMessageBox.information(self, "Success", "Order deleted successfully.")
            # Refresh the order table
            self.Show_Order_Table()
        except mycon.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error: {err}")
            self.db.rollback()  # Rollback in case of error
    def clear_order(self):
        self.lineEdit_12.clear()
        self.label_10.clear()
        self.lineEdit_11.clear()
        self.label_9.clear()
        self.spinBox.setValue(0)

    def on_item_clicked_order(self):
        selected_items = self.tableWidget_3.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            total_price_item = self.tableWidget_3.item(row, 7)
            if total_price_item:  # Eğer toplam fiyat öğesi varsa devam et
                total_price = total_price_item.text()  # Öğenin metin içeriğini al
                self.label_14.setText(total_price)  # Toplam fiyatı label_14'e yaz
    def Hesapla(self):
        if self.lineEdit_4.text() == "":
            QMessageBox.critical(self, "Error", "Please enter the amount paid", QMessageBox.Ok)
            return

        amount_paid = float(self.lineEdit_4.text())

        # Retrieve total price from the database
        self.db = mycon.connect(host='localhost', user='root', password='', database='coffe_shop')
        self.cur = self.db.cursor()

        self.cur.execute("SELECT total_price FROM orders")
        result = self.cur.fetchone()
        if result:
            total_price = float(result[0])
        else:
            QMessageBox.critical(self, "Error", "No total price found in the database", QMessageBox.Ok)
            return

        if total_price == 0:
            QMessageBox.critical(self, "Error", "No items in the order", QMessageBox.Ok)
            return

        if amount_paid < total_price:
            QMessageBox.critical(self, "Error", "Insufficient amount paid", QMessageBox.Ok)
            return

        change_amount = amount_paid - total_price
        self.label_17.setText(str(change_amount))
    def Pay_Order(self):
        try:
            if self.lineEdit_4.text() == "":
                QMessageBox.critical(self, "Error", "Please enter the amount paid", QMessageBox.Ok)
                return

            amount_paid = float(self.lineEdit_4.text())

            # Retrieve total price from the database
            self.db = mycon.connect(host='localhost', user='root', password='', database='coffe_shop')
            self.cur = self.db.cursor()

            self.cur.execute("SELECT total_price FROM orders")
            result = self.cur.fetchone()
            if result:
                total_price = float(result[0])
            else:
                QMessageBox.critical(self, "Error", "No total price found in the database", QMessageBox.Ok)
                return

            if total_price == 0:
                QMessageBox.critical(self, "Error", "No items in the order", QMessageBox.Ok)
                return

            if amount_paid < total_price:
                QMessageBox.critical(self, "Error", "Insufficient amount paid", QMessageBox.Ok)
                return

            change_amount = amount_paid - total_price
            self.label_17.setText(str(change_amount))
            date_today = datetime.date.today()

            # Connect to the database
            self.db = mycon.connect(host='localhost', user='root', password='', database='coffe_shop')
            self.cur = self.db.cursor()

            # Retrieve the highest customer_id from the customers table
            self.cur.execute("SELECT MAX(customer_id) FROM customers")
            result = self.cur.fetchone()
            if result and result[0] is not None:
                custID = result[0] + 1
            else:
                custID = 1

            # Insert payment details into customers table
            sql_insert_customer = """
                INSERT INTO customers (customer_id, total_price, amount, change_amount, date)
                VALUES (%s, %s, %s, %s, %s)
                """
            values_customer = (custID, total_price, amount_paid, change_amount, date_today)
            self.cur.execute(sql_insert_customer, values_customer)

            # Delete orders after payment
            self.cur.execute("DELETE FROM orders")

            # Commit changes
            self.db.commit()

            # Clear input fields
            self.label_14.clear()
            self.lineEdit_4.clear()
            self.label_17.clear()
            # Provide user feedback
            QMessageBox.information(self, "Payment Successful", "Payment completed successfully", QMessageBox.Ok)

        except mycon.Error as err:
            QMessageBox.critical(self, "Database Error", f"Connection failed: {err}", QMessageBox.Ok)
            self.db.rollback()
    #############################
    ###     Dashbored Tab  ######
    def Show_Dashbored(self):
        self.db = mycon.connect(host='localhost', user='root', password="", db='coffe_shop')
        self.cur = self.db.cursor()
        self.cur.execute(''' 
                                   SELECT * FROM `customers`
                                ''')
        data = self.cur.fetchall()
        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.insertRow(0)
        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_5.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1
            row_position = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(row_position)
    def Refresh_dashbord(self):
        self.Show_Dashbored()
        self.Total_Customer()
        self.Today_income()
        self.Total_income()

    def Total_Customer(self):
        self.db = mycon.connect(host='localhost', user='root', password='', database='coffe_shop')
        self.cur = self.db.cursor()
        try:
            # Retrieve the total number of customers
            self.cur.execute("SELECT COUNT(customer_id) FROM customers")
            result = self.cur.fetchone()
            if result:
                total_customers = result[0]
            else:
                total_customers = 0

            # Display the total number of customers in label_29
            self.label_29.setText(str(total_customers))
        except mycon.Error as e:
            QMessageBox.critical(self, "Error",f"An error occurred while retrieving total number of customers: {str(e)}")
    def Total_income(self):
        self.db = mycon.connect(host='localhost', user='root', password='', database='coffe_shop')
        self.cur = self.db.cursor()
        try:
            # Retrieve the total income
            self.cur.execute("SELECT SUM(total_price) FROM customers")
            result = self.cur.fetchone()
            if result and result[0] is not None:
                total_income = result[0]
            else:
                total_income = 0
            # Display the total income in label_30
            self.label_30.setText(str(total_income))
        except mycon.Error as e:
            QMessageBox.critical(self, "Error", f"An error occurred while retrieving total income: {str(e)}")
    def Today_income(self):
        self.db = mycon.connect(host='localhost', user='root', password='', database='coffe_shop')
        self.cur = self.db.cursor()
        try:
            # Get today's date
            today = datetime.date.today()
            # Retrieve today's income
            self.cur.execute("SELECT SUM(total_price) FROM customers WHERE date = %s", (today))
            result = self.cur.fetchone()
            if result and result[0] is not None:
                today_income = result[0]
            else:
                today_income = 0
            # Display today's income in label_31
            self.label_31.setText(str(today_income))
        except mycon.Error as e:
            QMessageBox.critical(self, "Error", f"An error occurred while retrieving today's income: {str(e)}")
    def Export_Dashbored(self):
        try:
            self.db = mycon.connect(host='localhost', user='root', password='', db='coffe_shop')
            self.cur = self.db.cursor()

            self.cur.execute(''' 
                        SELECT customer_id, total_price, amount, change_amount, date FROM customers
                    ''')
            data = self.cur.fetchall()
            file_path = 'Dashbored.xlsx'

            # Check if the file already exists
            if os.path.exists(file_path):
                os.remove(file_path)

            wb = Workbook(file_path)
            sheet1 = wb.add_worksheet()

            # Define column headers
            sheet1.write(0, 0, 'Customer ID')
            sheet1.write(0, 1, 'Total Price')
            sheet1.write(0, 2, 'Amount')
            sheet1.write(0, 3, 'Change Amount')
            sheet1.write(0, 4, 'Date')

            # Fill data into the worksheet
            row_number = 1
            for row in data:
                column_number = 0
                for item in row:
                    sheet1.write(row_number, column_number, str(item))
                    column_number += 1
                row_number += 1

            wb.close()
            QMessageBox.information(None, 'Success', 'Report Created Successfully')

        except mycon.Error as e:
            QMessageBox.critical(None, 'Database Error', f"An error occurred: {e}")
    #############################
    ####     Settings Tab  ######
    def Show_User_Table(self):
        self.db = mycon.connect(host='localhost', user='root', password="", db='coffe_shop')
        self.cur = self.db.cursor()
        self.cur.execute(''' 
                                   SELECT * FROM `log_db`
                                ''')
        data = self.cur.fetchall()
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.insertRow(0)
        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1
            row_position = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(row_position)
            self.tableWidget_4.itemSelectionChanged.connect(self.onItemSelected_User)
    def onItemSelected_User(self):
                selected_items = self.tableWidget_4.selectedItems()
                if selected_items:
                    row = selected_items[0].row()
                    Fullname_item = self.tableWidget_4.item(row, 0)
                    Username_item = self.tableWidget_4.item(row, 1)
                    Email_item = self.tableWidget_4.item(row, 2)
                    Password_item = self.tableWidget_4.item(row, 3)
                    if Fullname_item and  Username_item and Email_item and Password_item:
                        self.lineEdit_5.setText(Fullname_item.text())
                        self.lineEdit_6.setText(Username_item.text())
                        self.lineEdit_7.setText(Email_item.text())
                        self.lineEdit_8.setText(Password_item.text())
    def clear_User(self):
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
    def Add_User(self):
        Fullname = self.lineEdit_5.text()
        username = self.lineEdit_6.text()
        Email = self.lineEdit_7.text()
        password = self.lineEdit_8.text()
        # Check if any field is empty
        if not Fullname or not username or not Email or not password:
            QMessageBox.warning(self, "Input Error", "All fields are required.")
            return
        try:
            # Connect to the database
            mydb = mycon.connect(host='localhost', user='root', password='toor', database='coffe_shop')
            mycursor = mydb.cursor()
            # Check if username or email already exists
            mycursor.execute("SELECT * FROM log_db WHERE username = %s OR Email = %s", (username, Email))
            existing_user = mycursor.fetchone()
            if existing_user:
                QMessageBox.warning(self, "Input Error", "Username or Email already exists.")
                return
            # Insert the new user into the database
            sql = "INSERT INTO log_db (Fullname, username, Email, password) VALUES (%s, %s, %s, %s)"
            values = (Fullname, username, Email, password)
            mycursor.execute(sql, values)
            mydb.commit()
            QMessageBox.information(self, "Success", "User added successfully.")
            self.Show_User_Table()
            # Clear the text inside the QLineEdit widgets
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()
            self.lineEdit_8.clear()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))
    def Delete_User(self):
        Fullname = self.lineEdit_5.text()
        username = self.lineEdit_6.text()
        Email = self.lineEdit_7.text()
        password = self.lineEdit_8.text()
        # Check if the username field is empty
        if not Fullname or not username or not Email or not password:
            QMessageBox.warning(self, "Input Error", "All fields are required.")
            return
        try:
            # Connect to the database
            mydb = mycon.connect(host='localhost', user='root', password='toor', database='coffe_shop')
            mycursor = mydb.cursor()
            # Check if the user exists
            mycursor.execute("SELECT * FROM log_db WHERE username = %s", (username))
            existing_user = mycursor.fetchone()
            if not existing_user:
                QMessageBox.warning(self, "Input Error", "User does not exist.")
                return
            # Delete the user from the database
            sql = "DELETE FROM log_db WHERE username = %s"
            mycursor.execute(sql, (username,))
            mydb.commit()
            QMessageBox.information(self, "Success", "User deleted successfully.")
            self.Show_User_Table()
            # Clear the text inside the QLineEdit widget
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()
            self.lineEdit_8.clear()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))
    def Edit_User(self):
        Fullname = self.lineEdit_5.text()
        username = self.lineEdit_6.text()
        Email = self.lineEdit_7.text()
        password = self.lineEdit_8.text()
        # Check if the username field is empty
        if not Fullname or not username or not Email or not password:
            QMessageBox.warning(self, "Input Error", "All fields are required.")
            return
        try:
            # Connect to the database
            mydb = mycon.connect(host='localhost', user='root', password='toor', database='coffe_shop')
            mycursor = mydb.cursor()
            # Check if the user exists
            mycursor.execute("SELECT * FROM log_db WHERE username = %s", (username))
            existing_user = mycursor.fetchone()
            if not existing_user:
                QMessageBox.warning(self, "Input Error", "User does not exist.")
                return
            # Update the user in the database
            sql = "UPDATE log_db SET Fullname = %s, Email = %s, password = %s WHERE username = %s"
            values = (Fullname, Email, password, username)
            mycursor.execute(sql, values)
            mydb.commit()
            QMessageBox.information(self, "Success", "User updated successfully.")
            self.Show_User_Table()
            # Clear the text inside the QLineEdit widgets
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()
            self.lineEdit_8.clear()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))
    #############################
    ####     Theme Page   #######
    def Dark_Blue_Theme(self):
        style = open('themes/darkblue.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Gray_Theme(self):
        style = open('themes/darkgray.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Orange_Theme(self):
        style = open('themes/darkorange.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

    def QDark_Theme(self):
        style = open('themes/qdark.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)
def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()