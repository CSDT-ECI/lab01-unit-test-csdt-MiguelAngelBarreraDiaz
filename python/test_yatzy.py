from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_demo():
        expected = 15
        actual = 15
        assert expected == actual        

def test_change():
        chance = Yatzy.chance(4,5,5,6,1);
        score = 21
        assert score == chance

def test_yatzy_Score_WillBe_50():
        dices = [2,2,2,2,2]
        yatzy_score = Yatzy.yatzy(dices)
        score = 50
        assert score == yatzy_score
        

def test_yatzy_Score_WillBe_0():
        dices = [3,3,3,3,4]
        yatzy_score = Yatzy.yatzy(dices)
        score = 0
        assert score == yatzy_score

def test_ones_WillBe_2():
        ones = Yatzy.ones(1,1,3,3,4)
        score = 2
        assert ones == score

def test_twos_WillBe_3():
        twos = Yatzy.twos(2,2,2,4,5)
        score = 6
        assert twos == score

def test_threes_WillBe_3():
        threes = Yatzy.threes(3,3,2,4,5)
        score = 6
        assert threes == score


def test_crazyChance_pares():
        crazy_pares = Yatzy.crazyChance(2,4,6,2,2)
        score = 48
        assert crazy_pares == score



