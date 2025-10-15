from lib.grammar import GrammarStats

def test_grammar_stats_create():
    gs = GrammarStats()
    assert type(gs) == GrammarStats
    assert gs.count == 0
    assert gs.good_count == 0

def test_grammar_stats_check():
    gs = GrammarStats()
    assert gs.check("I'm autistic.") == True
    assert gs.check("u smell lol") == False
    assert gs.check("holy poop from the butt") == False
    assert gs.check("Stay classy!") == True

def test_grammar_stats_percentage():
    gs = GrammarStats()
    gs.check("I'm autistic.") # good
    gs.check("u smell lol") # bad
    gs.check("holy poop from the butt") # bad
    gs.check("Stay classy!") # good
    # so we should have 50%
    assert gs.percentage_good() == 50