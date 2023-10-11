class chef:
    storage = {'egg': 2, 'cheese': 2, 'cream': 2, 'salt': 2, 'meat': 2, 'bbq':2}
    dish_ready = []
    def __init__(self,dish, req_ings):
        self.dish = dish
        self.req_ings = req_ings
        self.ings_available = False
        self.food_cooked = False
        
    def fetch_ingredients(self):
        count = 0
        for ing in self.req_ings:
            if chef.storage[ing] > 0:
                 count += 1
            else:
                print("not enough ingredients")
                break
        if count == len(self.req_ings):
            for ing in self.req_ings:
                chef.storage[ing] -= 1
            self.ings_available = True
        print(chef.storage)
    def cook(self):
        if self.ings_available == True:
            print(f"cooked {self.dish}")
            chef.dish_ready.append(self.dish)
            self.food_cooked = True
        else:
            print('not enough ingrediets to cook')
            self.food_cooked = False
            
    def serve(self):
        if self.food_cooked == True:
            print(f"{self.dish} served")
            chef.dish_ready.remove(self.dish)
            self.food_cooked = False
            self.ings_available = False
        else:
            print('food not cooked')
            
ramsay = chef('steak', ['meat', 'salt', 'bbq'])
john = chef('bland', ['salt', 'cheese', 'cream'])
print(chef.dish_ready)
john.fetch_ingredients()
ramsay.cook()
ramsay.fetch_ingredients()
ramsay.cook()
print(chef.dish_ready)
# ramsay.serve()
print(chef.dish_ready)
john.fetch_ingredients()
john.cook()
print(chef.dish_ready)
ramsay.serve()
print(chef.dish_ready)
# ramsay.fetch_ingredients()
# ramsay.cook()
# ramsay.serve()

        