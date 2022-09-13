#CRIAÇÃO DE CLASSE
class Masterchef:
    def __init__(self,season,country,winner, main_course, year):
        self.season = season
        self.country = country
        self.winner = winner
        self.main_course = main_course
        self.year = year
    def get_season(self):
        return f"Temporada:{self.season}"
    def get_country(self):
        return f"País: {self.country}"
    def get_winner(self):
      return f"A(o) vencedora/vencedor da temporada foi {self.winner}."
    def get_main_course(self):
      return f"O prato principal servido foi {self.main_course}."
masterchef = Masterchef ('9','Brazil', 'Lays', 'Lagosta com purê de cenoura', '2022')
get_winner = masterchef.get_winner()
get_main_course = masterchef.get_main_course()
print(get_winner, get_main_course)

#HERANÇA
class MaterchefKids(Masterchef):
    def __init__(self,season, country, winner , main_course, year, age_winner):
        self.age_winner = age_winner
        super().__init__(season,country,winner, main_course, year)
    def get_age_winner(self):
        return f"A vencedora(o) tinha apenas {self.age_winner} anos."
masterchefkids  = MaterchefKids('1', 'Brasil', 'Lorenzo Ravioli' , 'Raviolone doro (com gema mole, espinafre e um mix de queijos)', '2015', '13')
print(masterchefkids.get_age_winner())

#ENCAPSULAMENTO

class Tvshow:
    def __init__(self,participants):
        self.participants = participants
        
    def get_participants(self):
        participants_msg = ",".join(self.participants)
        return participants_msg  
    
    def __get_secreat_seasoning(self):
        return('O tempero especial utilizado por esse cozinheiro foi cardamomo.')
    
    def access_secreat_seasoning (self,cooker):
        if cooker == 'Lays':
            return self.__get_secreat_seasoning()
        
        return "Esta é uma informação confidencial."
    
mchef = Tvshow(["Melina","Lays","Renato","Rafael","Fernanda"])
access = mchef.access_secreat_seasoning("Lays")
print(access)

#POLIMORFISMO
class FinalMainCourse:
    def __init__(self): 
        pass    
    def dish_maincourse(self):
        return "Indefinido"  
    
class DishLays(FinalMainCourse):
    def __init__(self,dish) :
        self.dish = dish
        super().__init__()
    def dish_maincourse(self):
        return f"O prato principal servido por Lays na final do Masterchef foi: {self.dish}"
    
dish_lays = DishLays("Lagosta com purê de cenoura.")
print(dish_lays.dish_maincourse())  

         
    
        
    
            


