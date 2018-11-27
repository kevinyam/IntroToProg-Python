# -------------------------------------------------#
# Title: Exception Handling Assignment 8
# Dev:   Kevin Yam
# Date:  November 26, 2018
# ChangeLog: (Who, When, What)
#   Kevin Yam, 11/26/2018, Created program to showcase classes using products
# -------------------------------------------------#

# This program will creates a product class and a product list class
# Product will create the basic definition of a product
# Product list will allow the user to store and process multiple products

class Product(object):
    """ Base Class for Product data """

    # -------------------------------------#
    # Desc:  Holds Product data
    # Dev:   Kevin Yam
    # Date:  12/12/2012
    # ChangeLog: Created class to store product data
    # -------------------------------------#

    # --Fields--
    # ID = ""
    # Name = ""
    # Price = ""

    # --Constructor--
    def __init__(self, ID = "", Name = "", Price = ""):
        # Attributes
        self.__ID = ID
        self.__Name = Name
        self.__Price = Price

    # --Properties--
    # ID of Product
    @property  # (getter or accessor)
    def ID(self):
        return self.__ID

    @ID.setter  # (setter or mutator)
    def ID(self, Value):
        self.__ID = Value
    # Name of Product
    @property  # (getter or accessor)
    def Name(self):
        return self.__Name

    @Name.setter  # (setter or mutator)
    def Name(self, Value):
        self.__Name = Value
    # Price of Product
    @property  # (getter or accessor)
    def Price(self):
        return self.__Price

    @Price.setter  # (setter or mutator)
    def Price(self, Value):
        self.__Price = Value
        # --Methods--
    # Returns the Name of the product
    def __str__(self):
        return self.Name
    # Returns the ID,Name,Price of product
    def ToString(self):
        return self.ID + ',' + self.Name + ',' + self.Price
        # --End of class--


class ProductList(object):
    """ Base Class for Product List """

    # -------------------------------------#
    # Desc:  Holds Product data
    # Dev:   Kevin Yam
    # Date:  12/12/2012
    # ChangeLog: Created class that creates a list and stores products
    # -------------------------------------#

    # --Fields--
    # plist = ""

    # --Constructor--
    # Starts with an empty list if one hasn't been provided
    def __init__(self, plist = []):
        # Attributes
        self.__plist = plist

    # --Properties--
    # Product List
    @property  # (getter or accessor)
    def plist(self):
        return self.__plist

    @plist.setter  # (setter or mutator)
    def plist(self, Value):
        self.__plist = Value

    # --Methods--
    # returns the product list
    def __str__(self):
        return self.plist
    # returns the state of the product list
    def ToString(self):
        if len(self.plist) == 0:
            return "Empty Product List"
        else:
            return "Product List contains " + len(self.plist) + "Products"\

    # Adds product to the product list
    def AddProduct(self, strInput):
        # Needs a specific formatting
        try:
            input = strInput.rsplit(',')
            product1 = Product(input[0].rstrip(), input[1].rstrip(), input[2].rstrip())
            self.plist.append(product1)
        # Tells user to use certain formatting
        except Exception:
            print("Please use this format Id, Name, and Price (ex. 1,ProductA,9.99)")

    # Creates the list of products using user input
    def CreateProductList(self):
        print("Type in a Product Id, Name, and Price you want to add to the file")
        print("(Enter 'Exit' to quit!)")
        while (True):
            strUserInput = input("Enter the Id, Name, and Price (ex. 1,ProductA,9.99): ")
            if (strUserInput.lower() == "exit"):
                break
            else:
                self.AddProduct(strUserInput)

    # Returns a product from the list based on the index
    def getProduct(self, i):
        try:
            return self.plist(i-1)
        except Exception:
            print("Index not found in list")
            return None

    # Stores the product list to a file
    def WriteListToFile(self, file):
      try:
        for item in self.plist:
            file.write(item.ToString() + "\n")
      except Exception as e:
        print("Error: " + str(e))

    # Reads and displays a file
    @staticmethod
    def ReadAllFileData(file, Message="Contents of File"):
      try:
        print(Message)
        file.seek(0)
        print(file.read())
      except Exception as e:
        print("Error: " + str(e))

        # --End of class--

#Data
objFile = None #File Handle

#I/O
prodlist = ProductList()
prodlist.CreateProductList()

try:
  objFile = open("Products.txt", "r+")
  prodlist.ReadAllFileData(objFile, "Here is the Current data:")
  prodlist.WriteListToFile(objFile)
  prodlist.ReadAllFileData(objFile, "Here is this data was saved:")
except FileNotFoundError as e:
     print("Error: " + str(e) + "\n Please check the file name")
except Exception as e:
    print("Error: " + str(e))
finally:
  if(objFile != None):objFile.close()

