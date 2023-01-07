dict_articulos = { 4: {"nombre": "ASUS TUF GeForce RTX", "stock": 6, "precio": 1400},
 2: {"nombre": "ASUS DUAL Radeon RX6600", "stock": 12, "precio": 294},
 3: {"nombre": "Intel Core i7-13700K", "stock": 9, "precio": 530},
 1: {"nombre": "Kingston Fury Beast 32GB", "stock": 10, "precio": 180},
 10: {"nombre": "Corsair DC Cable Pro Kit", "stock": 20, "precio": 110},
 11: {"nombre": "Gigabyte GC-TITAN RIDGE 2.0", "stock": 15, "precio": 81},
 }

dict_compras = {"AA32E": {"fecha": 20201101, "articulos":{3:1,4:1} },
 "AB37Z": {"fecha": 20201101, "articulos":{1:1,4:1} },
 "CF13U": {"fecha": 20201101, "articulos":{1:1,3:1} },
 "KL11T": {"fecha": 20201101, "articulos":{1:3,3:2,4:2} },
 "ST234": {"fecha": 20191207, "articulos":{1:1,3:1,4:1} },
 "NL345": {"fecha": 20181207, "articulos":{ 1:1,2:1,3:1} },
 "SG345": {"fecha": 20190407, "articulos":{1:1,2:1,3:1,4:3} },
 "SU798": {"fecha": 20210107, "articulos":{2:2,10:3,11:1} }
 }

dict_clientes = {"34343434H": {"nombre": "Jason Statham", "telefono": "666994455"},
 "78787878K": {"nombre": "Dwayne Johnson", "telefono": "666765432"},
 "39292939S": {"nombre": "Federico Luppi", "telefono": "666232211"},
 "53423454C": {"nombre": "Lorenzo Lamas", "telefono": "666987578"},
 "87654334T": {"nombre": "Charlize Theron", "telefono": "555443322"},
 "92837467Z": {"nombre": "Linda Hamilton", "telefono": "555443322"},
 "26548734H": {"nombre": "Scarlett Johansson", "telefono": "555443322"},
 "99837653N": {"nombre": "Uma Thurman", "telefono": "555443322"}
 }

cliente_compra = {"34343434H": ["AA32E", "AB37Z","SG345"], "78787878K": ["CF13U", "KL11T"], "39292939S": ["ST234"],
 "53423454C": ["NL345"], "87654334T":["SU798"] }

compra_cliente = {"AA32E": "34343434H", "AB37Z": "34343434H", "CF13U": "78787878K", "KL11T": "78787878K",
 "ST234": "39292939S", "NL345": "53423454C","SG345" : "34343434H","SU798":"87654334T"}

letrasDni = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N",
             "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
press = "\nPress any key to continue\n"

main = '\n---MAIN MENU---\n1)Items\n2)Purchases\n3)Customers\n4)Exit'
itemmenu = '\n---ITEMS MENU---\n1)New Item\n2)Modify Item\n3)Find Item\n4)List Item\n5)Go Back'
menumodify = '\n---MENU MODIFY ITEMS---\n1)Name\n2)Stock\n3)Price\n4)Show Item\n5)Main Menu\n6)Go Back'
menufinditem = '\n---MENU FIND ITEMS---\n1)Find Item by ID\n2)Find Item by Name\n3)Main Menu\n4)Go Back'
menulistitem = '\n---MENU LIST ITEMS---\n1)List by ID\n2)List by Name\n3)List by Stock\n4)List 3 Best Selling Items\n' \
               '5)List 3 Least Sold Items\n6)Main Menu\n7)Go Back'
purchasemenu = '\n---PURCHASES MENU---\n1)Find Purchase\n2)List Purchases\n3)New Purchase\n4)Go Back'
customermenu = '\n---CUSTOMERS MENU---\n1)New Customer\n2)Find Customer\n3)Go Back'
menuListPurchase = "\n---MENU LIST PURCHASE---\n1)List all purchases\n2)List purchases that contain some item\n3)Go back\n4)Main menu"
menuCustFind = "\n---Menu Find Customers---\n1)Find by NIF\n2)Find by name\n3)Find top 3 highest spending customers\n4)Main menu\n5)Go back"
menuShowCust = "\n---Menu show customer's purchases---\n1)Show purchases\n2)Show detailed purchases\n3)Main menu\n4)Go back"
flecha = "->"
