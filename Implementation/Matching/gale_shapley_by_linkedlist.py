import logging
from typing import Set
from termcolor import colored
from pprint import pprint

logging.basicConfig(level=logging.DEBUG)

class Node:
    def __init__(self, value: str) -> None:
        self.value: str = value
        self.next: 'Node' = None
        self.prefer: int = 0

    def __repr__(self) -> str:
        return f"Node({self.value})"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value: str) -> True:
        new_node = Node(value)

        done = False
        try:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
        except TypeError as e:
            logging.debug(e)
        else:
            self.length += 1
            done = True
        finally:
            return done
        
    def prepend(self, value: str) -> True:
        new_node = Node(value)

        done = False
        try:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head = new_node
        except TypeError as e:
            logging.debug(e)
        else:
            self.length += 1
            done = True
        finally:
            return done
        
    def pop_first(self) -> Node:
        tmp = self.head
        if self.length == 0:
            return tmp
        
        self.head = self.head.next
        tmp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None
        
        return tmp
    
    def __repr__(self):
        nodelist = []
        node = self.head
        while node is not None:
            nodelist.append(node)
            node = node.next
        return str(nodelist)


class GaleShapley:
    def __init__(self, men: Set[str], mens_preferences: dict, womens_preferences: dict):
        self.men: Set[str] = men
        self.mens_preferences: dict = mens_preferences
        self.womens_preferences: dict = womens_preferences

    @staticmethod
    def preference_to_rank(preference: dict) -> dict:
        """
        Turn a preference list into a dictionary that of numerical ranks, 
        with lower numbers meaning more preferred.
        """
        return {x: {y: rank for rank, y in enumerate(x_pref)} for x, x_pref in preference.items()}
    
    def matching(self) -> dict:
        """Solve the stable matching problem using Gale-Shapley algorithm.
        
        men: set[str]. set of men
        mens_preferences: dict[str, list[str]]. men's preferences
        womens_preferences: dict[str, list[str]]. women's preferences

        """
        mens_list = LinkedList()
        for man in self.men:
            mens_list.append(man)

        mens_rank = self.preference_to_rank(self.mens_preferences)
        womens_rank = self.preference_to_rank(self.womens_preferences)

        pairs = {}

        while mens_list.head is not None:
            proposer: Node = mens_list.pop_first()
            logging.debug(f'proposer: {proposer}')
            try:
                woman: str = self.mens_preferences[proposer.value][proposer.prefer]
                logging.debug(f'proposed woman: {woman}')
            except IndexError as e:
                print(colored(f'No stable match for {proposer.value}', on_color='on_red'))
                logging.debug(e)
                return None
                
            
            engaged_man: str = pairs.get(woman)
            logging.debug(f'engaged man: {engaged_man}')
            if not engaged_man:  # if woman is not engaged
                pairs[woman] = proposer.value
                continue
            
            engaged_man_rank: int = womens_rank[woman][engaged_man]
            proposer_rank: int = womens_rank[woman][proposer.value]
            if engaged_man_rank < proposer_rank:
                mens_list.prepend(proposer.value)
                mens_list.head.prefer = mens_rank[proposer.value][woman] + 1
            else:
                pairs[woman] = proposer.value
                mens_list.prepend(engaged_man)
                mens_list.head.prefer = mens_rank[engaged_man][woman] + 1

        return pairs

if __name__ == "__main__":
    men = {'S.Samuel', 'S.Bobby', 'S.John'}
    women = {'F.Smith', 'F.Martinez', 'F.Brown'}
    mens_preferences = {
        'S.Samuel': ['F.Smith', 'F.Brown', 'F.Martinez'],
        'S.Bobby': ['F.Martinez', 'F.Brown', 'F.Smith'],
        'S.John': ['F.Martinez', 'F.Brown', 'F.Smith']
    }

    womens_preferences = {
        'F.Smith': ['S.Samuel', 'S.John', 'S.Bobby'],
        'F.Martinez': ['S.Samuel', 'S.Bobby', 'S.John'],
        'F.Brown': ['S.John', 'S.Samuel', 'S.Bobby']
    }
    pprint(mens_preferences)
    pprint(womens_preferences)

    gale_shapley: GaleShapley = GaleShapley(men, mens_preferences, womens_preferences)
    pprint(gale_shapley.matching())
