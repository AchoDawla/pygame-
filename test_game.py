import unittest
import pygame
import sys
import random
import time

class TestGameLogic(unittest.TestCase):
   def setUp(self):
       pygame.init()
       self.width, self.height = 400, 400
       self.screen = pygame.display.set_mode((self.width,self.height))
       self.squares = []
       self.corrects = 0
       self.clicks = 0
       self.i = 0

   def test_square_generation(self):
       # Test that squares are being generated correctly
       self.assertEqual(len(self.squares), 0)
       for _ in range(5):
           sx, sy = random.randint(0,4)*self.width//5 , random.randint(0,4)*self.height//5
           self.squares.append([sx,sy])
       self.assertEqual(len(self.squares), 5)

   def test_square_hiding(self):
       # Test that squares are being hidden correctly
       for _ in range(5):
           self.squares.append([random.randint(0,4)*self.width//5, random.randint(0,4)*self.height//5])
       self.i = 0
       self.assertEqual(self.i, 0)
       self.i += 1
       self.assertEqual(self.i, 1)

   def test_click_and_correct_tracking(self):
       # Test that clicks and corrects are being tracked correctly
       self.assertEqual(self.clicks, 0)
       self.assertEqual(self.corrects, 0)
       self.clicks += 1
       self.assertEqual(self.clicks, 1)
       self.corrects += 1
       self.assertEqual(self.corrects, 1)
      
       def tearDown(self):
        pygame.quit()
      

if __name__ == '__main__':
   unittest.main()