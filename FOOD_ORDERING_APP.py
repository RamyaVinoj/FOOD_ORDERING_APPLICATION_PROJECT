#!/usr/bin/env python
# coding: utf-8

# # FOOD ORDERING APPLICATION USING PYTHON

# In[1]:


class restaurant:
    
    def __init__(self,name):
        self.restro_name=name
        self.food={}
        self.foodID=len(self.food)+1
        self.admin_details={}
        self.user_details={}
        self.ordered_item=[]
    
    def admin_register(self):
        try:
            print("\n ***CREATING NEW ADMIN ACCOUNT***")
            self.admin_email=input("\n ENTER EMAILID TO REGISTER: ")
            self.admin_password=input("\n SET PASSWORD: ")
            self.admin_details={"EMAILID":self.admin_email,"PASSWORD":self.admin_password}
            print("\nACCOUNT CREATED SUCCESSFULLY\n")
            for i in self.admin_details:
                print(i,":", self.admin_details[i])
        except Exception as e:
            print("\nPLEASE INPUT CORRECT VALUES\n")
            
    def admin_login(self):
        try:
            print(f"WELCOME TO {self.restro_name} RESTAURANT\n\n")
            emailid=input("\nENTER YOUR EMAIL:")
            passw=input("\nENTER THE PASSWORD:")
            if len(self.admin_details.values())!=0:
                if (emailid==self.admin_email) and (passw==self.admin_password):
                    print("\nYOU HAVE LOGGED-IN SUCCESSFULY!!\n")
                    while True:
                        print("\n ****PLEASE CHOOSE ANY OF THE BELOW OPTIONS**** \n")
                        print("\n\t1.ADD ITEM \n\t2.EDIT ITEM \n\t3.VIEW ITEM \n\t4.REMOVE ITEM \n\t5.BACK\n")
                        x=int(input())
                        if x==1:
                            self.add_item()
                        elif x==2:
                            self.edit_item()
                        elif x==3:
                            self.view_item()
                        elif x==4:
                            self.remove_item()
                        elif x==5:
                            break
                        else:
                            print("\n INVALID SELECTION \n")
                else:
                    print("\n INCORRECT LOGIN CREDENTIALS \n")
            else:
                print("\n ADMIN DOES NOT EXIST \n")
        except Exception as e:
            print("\n!! PLEASE PROVIDE CORRECT INPUTS !!")
    
    def add_item(self):
        try:
            name=input("\nENTER FOOD ITEM:")
            quantity=input("\nENTER THE QUANTITY:")
            price=float(input("\nENTER THE PRICE OF FOOD ITEM IN RS:"))
            discount=float(input("\nENTER THE DISCOUNT AMOUNT IN RS:"))
            stock=float(input("\nENTER THE NUMBER OF STOCKS AVAILABLE:"))
            food_item={"NAME":name,"QUANTITY":quantity,"PRICE":price,"DISCOUNT":discount,"STOCK":stock}
            self.foodID=len(self.food)+1
            self.food[self.foodID]=food_item
            print("\nFOOD ITEM ADDED SUCCESSFULLY\n")
            print("\nFOOD ITEM IS:",self.food)
            
        except Exception as e:
            print("\n!! PLEASE PROVIDE CORRECT INPUTS !!")
            
    def edit_item(self):
        try:
            x=int(input("ENTER THE FOODID TO EDIT:\n"))
            if x in self.food.keys():
                print("\n\t1.UPDATE NAME\n\t2.UPDATE QUANTITY\n\t3.UPDATE PRICE\n\t4.UPDATE DISCOUNT \n\t5.UPDATE STOCK \n")
                y=int(input("\nENTER 1-5 TO EDIT THE FOOD DETAILS:"))
                if y==1:
                    self.food[x]["NAME"]=input("\nENTER THE UPDATED FOODNAME:")
                    print("\nFOOD NAME IS EDITED SUCCESSFULLY\n")
                elif y==2:
                    self.food[x]["QUANTITY"]=input("\nENTER THE UPDATED QUANTITY:")
                    print("\nQUANTITY IS EDITED SUCCESSFULLY\n")
                elif y==3:
                    self.food[x]["PRICE"]=input("\nENTER THE UPDATED PRICE:")
                    print("\nPRICE IS EDITED SUCCESSFULLY\n")
                elif y==4:
                    self.food[x]["DISCOUNT"]=input("\nENTER THE UPDATED DISCOUNT:")
                    print("\nDISCOUNT IS EDITED SUCCESSFULLY\n")
                elif y==5:
                    self.food[x]["STOCK"]=input("\nENTER THE UPDATED STOCK:")
                    print("\nSTOCK IS EDITED SUCCESSFULLY\n")
                else:
                    print("\nINVALID OPTION\n")
            else:
                print("\nINVALID FOODID \n")
        
        except Exception as e:
            print("\n PLEASE INPUT CORRECT ENTRY\n")
            
    def view_item(self):
        print("\nHERE IS THE FOOD MENU:\n")
        if len(self.food)!=0:
            for i in self.food:
                print(f"FOOD ID:{i}")
                for j in self.food[i]:
                    print(j,":",self.food[i][j])
                print()
        else:
            print("\nTHERE IS NO FOOD!\n")
            
    def remove_item(self):
        try:
            print("\n***THE FOOD ITEM WILL BE REMOVED PERMANENTLY!*** \n")
            x=int(input("\nENTER THE FOOD ID TO REMOVE:"))
            if x in self.food.keys():
                del self.food[x]
                print("\nFOOD ITEM REMOVED SUCCESSFULLY \n")
                print("\nUPDATED FOOD MENU IS:",self.food)
            else:
                print("\nINCORRECT FOOD ID \n")
        except Exception as e:
            print("\nINVALID ENTRY\n")
            
    def user_register(self):
        try:
            print("\n***CREATING NEW USER ACCOUNT***")
            self.user_name=input("\nENTER YOUR NAME:")
            self.user_phone=int(input("\nENTER YOUR PHONE NUMBER:"))
            self.user_email=input("\nENTER EMAILID TO REGISTER:")
            self.user_address=input("\nENTER YOUR ADDRESS:")
            self.user_password=input("\nSET PASSWORD:")
            self.user_details={"NAME":self.user_name,"PHONE":self.user_phone,"EMAIL":self.user_email,"ADDRESS":self.user_address,"PASSWORD":self.user_password}
            print("\nUSER ACCOUNT CREATED SUCCESSFULLY\n")
            for i in self.user_details:
                print(i,":", self.user_details[i])
        except Exception as e:
            print("\nPLEASE INPUT CORRECT VALUES\n")
            
    def user_login(self):
        try:
            print(f"\n\nWELCOME TO {self.restro_name} RESTAURANT\n\n")
            useremail=input("\nENTER YOUR EMAIL:")
            userpass=input("\nENTER THE PASSWORD:")
            if len(self.user_details) !=0:
                if (useremail==self.user_details["EMAIL"]) and (userpass==self.user_details["PASSWORD"]):
                    print("\nLOGIN SUCCESSFULL!!")
                    while True:
                        print("\n****PLEASE CHOOSE ANY OF THE BELOW OPTIONS****\n")
                        print("\n\t1.PLACE ORDER\n\t2.ORDER HISTORY\n\t3.UPDATE PROFILE\n\t4.BACK\n")
                        x=int(input())
                        if x==1:
                            self.place_order()
                        elif x==2:
                            self.order_history()
                        elif x==3:
                            self.update_profile()
                        elif x==4:
                            break
                        else:
                            print("\nINVALID OPTION\n")
                else:
                    print("\n INCORRECT LOGIN CREDENTIALS \n")
            else:
                print("\n USER DOES NOT EXIST \n")
                
        except Exception as e:
            print("\n!! PLEASE PROVIDE CORRECT INPUTS !!")
            
    def place_order(self):
        try:
            if len(self.food)!=0:
                print("\nMENU OF FOOD ITEMS:")
                menu=[]
                for items in self.food:
                    menu.append([self.food[items]["NAME"],self.food[items]["QUANTITY"],self.food[items]["PRICE"]])
                for i in range(len(menu)):
                    print(i+1,".",menu[i])
                while True:
                    print("\n\t1.CONTINUE\n\t2.BACK\n")
                    x=input()
                    if x=="1":
                        print("ENTER THE FOOD NUMBER TO ORDER (separated by comma):")
                        y=input().split(",")
                        for i in y:
                            z=int(i)
                            if z<=len(menu):
                                self.ordered_item.append(menu[z-1])
                            else:
                                print("\nFOOD IS NOT IN LIST",z)
                        print("\nLIST OF FOOD ITEMS SELECTED:\n")
                        for j in self.ordered_item:
                            print(j)
                    elif x=="2":
                        break
                    else:
                        print("\nINVALID OPTION\n")
            else:
                print("\nFOOD IS NOT AVAILABLE\n")
        except Exception as e:
            print("\n!! PLEASE PROVIDE CORRECT INPUTS !!\n")
            
    def order_history(self):
        if len(self.ordered_item)!=0:
            print("\nTHE ORDER HISTORY IS:\n")
            for i in self.ordered_item:
                print(i)
        else:
            print("\nNO ORDER PLACED\n")
            
   #self.user_details={"NAME:":self.user_name,"PHONE:":self.user_phone,"EMAILID:":self.user_email,"ADDRESS:":self.user_address,"PASSWORD:":self.user_password}
         
    def update_profile(self):
        try:
            for i in self.user_details:
                print(i,":",self.user_details[i])
            while True:
                print("\nPLEASE SELECT ANY ONE OF THE BELOW TO UPDATE\n")
                print("\n\t1.UPDATE NAME\n\t2.UPDATE PHONE\n\t3.UPDATE EMAIL\n\t4.UPDATE ADDRESS\n\t5.UPDATE PASSWORD\n\t6.BACK\n")
                a=int(input())
                if a==1:
                    self.user_details["NAME"]=input("\nENTER UPDATED NAME:")
                    print("\nNAME IS UPDATED SUCCESSFULLY\n")
                elif a==2:
                    self.user_details["PHONE"]=int(input("\nENTER UPDATED PHONENO:"))
                    print("\nPHONE NUMBER IS UPDATED SUCCESSFULLY\n")
                elif a==3:
                    self.user_details["EMAIL"]=input("\nENTER UPDATED EMAILID:")
                    print("\nEMAILID IS UPDATED SUCCESSFULLY\n")
                elif a==4:
                    self.user_details["ADDRESS"]=input("\nENTER UPDATED ADDRESS:")
                    print("\nADDRESS IS UPDATED SUCCESSFULLY\n")
                elif a==5:
                    self.user_details["PASSWORD"]=input("\nENTER UPDATED PASSWORD:")
                    print("\nPASSWORD IS UPDATED SUCCESSFULLY\n")
                elif a==6:
                    break
                else:
                    print("\nINVALID OPTION\n")
            if a in [1,2,3,4,5]:
                print(i,":",self.user_details[i])
            else:
                pass
        except Exception as e:
            print("\n!! PLEASE PROVIDE CORRECT INPUTS !!")
            
try:
    def main():
        obj=restaurant("RAMYA")
        print("^"*20,"WELCOME TO",obj.restro_name,"RESTAURANT","^"*20,"\n")
        while True:
            print("-"*40+ "MAIN MENU" +"-"*40,"\n")
            print("\n\t1.ADMIN\n\t2.USER\n\t3.EXIT\n")
            x=int(input())
            if x==1:
                while True:
                    print("*"*40+ "ADMIN PROFILE" +"*"*40,"\n")
                    print("\n\t1.ADMIN REGISTRATION\n\t2.ADMIN LOGIN\n\t3.BACK\n")
                    y=int(input())
                    if y==1:
                        obj.admin_register()
                    elif y==2:
                        obj.admin_login()
                    elif y==3:
                        break
                    else:
                        print("INVALID ENTRY \n")
            elif x==2:
                while True:
                    print("*"*40+"USER PROFILE"+"*"*40,"\n")
                    print("\n\t1.ACCOUNT REGISTRATION\n\t2.LOGIN\n\t3.BACK\n")
                    y=int(input())
                    if y==1:
                        obj.user_register()
                    elif y==2:
                        obj.user_login()
                    elif y==3:
                        break
                    else:
                        print("\nINVALID ENTRY \n")
            elif x==3:
                break
            else:
                print("NOT A VALID OPTION")
except Exception as e:
        print("PLEASE TRY AGAIN LATER")
        
if __name__=='__main__':
    main()
    print("\nTHANK YOU!")


# In[ ]:




