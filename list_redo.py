def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname":"Andrés", "lastname": "Sierra"}

    super_list = [
        {"firstname":"Andrés", "lastname": "Sierra"},
        {"firstname":"Hedo", "lastname": "Zarufar"},
        {"firstname":"Ras", "lastname": "AlGhul"}
    ] 
 

    for value in super_list:
        print(value["firstname"], "", value["lastname"])           

      

if __name__ == "__main__":
    run()
