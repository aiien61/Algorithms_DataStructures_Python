from collections import namedtuple, deque, defaultdict
from itertools import product
from termcolor import colored
from pprint import pprint

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

Pair = namedtuple('Pair', ['man', 'woman'])

def preference_to_rank(preference: dict) -> dict:
    """Turn a preference list into a dictionary that of numerical ranks, with lower numbers meaning
    more preferred.
    """
    return {x: {y: i for i, y in enumerate(x_pref)} for x, x_pref in preference.items()}

def stable_matching_brute_force(*, men, women, mens_preferences, womens_preferences):
    """Solve the stable matching problem using Brute force implementation.
    
    men: set[str]. set of men
    women: set[str]. set of women
    mens_preferences: dict[str, list[str]]. men's preferences
    womens_preferences: dict[str, list[str]]. women's preferences

    Returns: list[Pair]. list of unstable matching
    """
    men_rank = preference_to_rank(mens_preferences)
    women_rank = preference_to_rank(womens_preferences)
    
    men_sequence = tuple(men)
    matchings = {Pair(*pair) for pair in product(men, women)}
    
    def is_stable(matching):
        match_man, match_woman = matching
        rest_matchings = matchings - {matching}
        for rest_man, rest_woman in rest_matchings:
            has_better_man = women_rank[match_woman][rest_man] < women_rank[match_woman][match_man]
            has_better_woman = men_rank[match_man][rest_woman] < men_rank[match_man][match_woman]
            if has_better_man and has_better_woman:
                return False
        return True
    
    return [matching for matching in matchings if not is_stable(matching)]

def gale_shapley(*, men, women, mens_preferences, womens_preferences):
    """Solve the stable matching problem using Gale-Shapley algorithm.
    
    men: set[str]. set of men
    women: set[str]. set of women
    mens_preferences: dict[str, list[str]]. men's preferences
    womens_preferences: dict[str, list[str]]. women's preferences

    """
    women_rank = preference_to_rank(womens_preferences)
    proposers = men
    men_rank = {man: deque(preference)
                for man, preference in mens_preferences.items()}
    pairs = {}

    while proposers:
        proposer = proposers.pop()
        try:
            woman = men_rank[proposer].popleft()
        except IndexError:
            print(colored(f'No stable match for {proposer}.', on_color='on_red'))
            return None
        
        if engaged_man := pairs.get(woman):
            if women_rank[woman][proposer] < women_rank[woman][engaged_man]:
                pairs[woman] = proposer
                proposers.add(engaged_man)
            else:
                proposers.add(proposer)
        else:
            pairs[woman] = proposer
    
    return pairs    

if __name__ == '__main__':
    pprint(mens_preferences)
    pprint(womens_preferences)
    
    print(stable_matching_brute_force(men=men, women=women, mens_preferences=mens_preferences, womens_preferences=womens_preferences))
    pprint(gale_shapley(men=men, women=women, mens_preferences=mens_preferences, womens_preferences=womens_preferences))

