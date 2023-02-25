from pymongo import MongoClient

class mongodatabase:  
     try:          
            client = MongoClient()
            client = MongoClient('localhost', 27017)       
            db = client['Delivery_database']  

            collection = db['shop-collection']  
            collection_1 =db['User_collection']

            print("connection success")      
     except Exception as error:
            print(error)


     def __init__(self):
        
        data = [          
            {"_id": 1, "Shop Name": "Tea shop", "food": ["fired green", "Thai soup", "squid salad", "fry chicken", "Malashankaw","Cheese Burger","SandWich"], "drink": ["Tea","Americano","Chocolate Shake","Strawberry Juice"] },
            {"_id": 2, "Shop Name": "Pan Ei", "food": ["Fried Assorted Vegitables","BeanPasteRice"], "drink": ["LemonTea","JuicyJuice"]},    
            {"_id": 3, "Shop Name": "FuDo Bakery", "food": ["Burger"], "drink": ["SpecialYogurd","FreshJuice"]},
            {"_id": 4, "Shop Name": "Shwe kaungkin", "food": ["SpoonPlane","FriedGreens"], "drink": ["PapayaJuice","LemonJuice"]},      
            {"_id": 5, "Shop Name": "TeaPro", "food": ["FriedRice","TwelveSoups"], "drink": ["AppleJuice","OrangeJuice"]},
        ]
        data_1 = [
          { "_id":1, "user_name": "sithu", "password":"11111", "phone_number":"959970244289" ,"email":"sithu@gmail.com" },
          { "_id":2, "user_name": "AungKaungSet", "password":"22222", "phone_number":"959966760561","email":"aungkaungset@gmail.com" },
          { "_id":3, "user_name": "khantKoKo", "password":"33333", "phone_number":"959975668931" ,"email":"khantkoko@gmail.com" },
          { "_id":4, "user_name": "ThazinNaing", "password":"44444", "phone_number":"959774820322", "email":"thanhlaing@gmail.com"}      
    ]
        try:        
            # self.collection.drop()
            # self.collection.insert_many(data)
              
            # self.collection_1.drop()
            # self.collection_1.insert_many(data_1)
            print("insert successful")        
        except Exception as error:
                print(error)
          
        
     def showMenu (self):
        #   find = self.collection.find({},{'Shop Name':1,'_id':0})
        #   changeStrng = '\n'.join(map(str, find))
          find1 = self.collection_1.find({},{'user_name':1,'_id':0})
          changeStrng1 = '\n'.join(map(str, find1))

          return changeStrng1
     
    
      

if __name__ == "__main__":
     obj = mongodatabase()
     obj.option()
