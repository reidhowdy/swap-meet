class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
    
    def add(self, item_to_add):
        self.inventory.append(item_to_add)
        return item_to_add

    def remove(self, item_to_remove):
        if item_to_remove not in self.inventory:
            return False
        self.inventory.remove(item_to_remove)
        return item_to_remove

    def get_by_category(self, category):
        category_matches = []
        for item in self.inventory:
            if item.category == category:
                category_matches.append(item)
        return category_matches

    def swap_items(self, other_vendor, selfs_item, others_item):
        if selfs_item in self.inventory and others_item in other_vendor.inventory:
            self.remove(selfs_item)
            self.add(others_item)

            other_vendor.remove(others_item)
            other_vendor.add(selfs_item)

            return True
            
        else:
            return False
    
    def swap_first_item(self, other_vendor):
        if (len(self.inventory) == 0) or (len(other_vendor.inventory) == 0):
            return False
        else:
            selfs_item = self.remove(self.inventory[0])
            others_item = other_vendor.remove(other_vendor.inventory[0])

            self.add(others_item)
            other_vendor.add(selfs_item)
                
            return True

    def get_best_by_category(self, category = ""):
        best_condition = -1
        best_item = None
        for item in self.inventory:
            if ((item.category == category) and
            (item.condition > best_condition)):
                best_item = item
                best_condition = item.condition
        return best_item
    
    def swap_best_by_category(self, other = None, my_priority = "", their_priority = ""):
        self_best = self.get_best_by_category(their_priority)
        other_best = other.get_best_by_category(my_priority)

        if not self_best or not other_best:
            return False
        else:
            self.swap_items(other, self_best, other_best)
            return True






    
        

    
