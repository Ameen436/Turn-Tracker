import unittest
from turnTracker import TurnTracker

# Implement unit tests here


class TestTurnTracker(unittest.TestCase):
    def setUp(self):
        self.tt = TurnTracker()
        self.tt.addPlayer('Jake') 
        self.tt.addPlayer('Lina') 
        self.tt.addPlayer('Ameen') 
        self.tt.addPlayer('Tim') 
    def test_addPlayer(self):
        self.assertEqual(self.tt.nextPlayer(), 'Jake')
        self.assertEqual(self.tt.nextPlayer(), 'Lina')
        self.assertEqual(self.tt.nextPlayer(), 'Ameen')
        self.assertEqual(self.tt.nextPlayer(), 'Tim')
    def test_numberOfPlayers(self):
        self.assertEqual(self.tt.number_Of_Players(), 4)
    def test_skipNextPlayer(self):
        self.tt.skipNextPlayer()
        self.assertEqual(self.tt.nextPlayer(), 'Lina')
        self.tt.skipNextPlayer()
        self.assertEqual(self.tt.nextPlayer(), 'Tim')
    def test_reverseTurnOrder(self):
        self.tt.reverseTurnOrder()
        self.assertEqual(self.tt.nextPlayer(), 'Ameen')
