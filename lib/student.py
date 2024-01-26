#!/usr/bin/env python

from user import User

class Student(User):
     def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []


     def learn(self, string_input):
        '''learns from a string and adds to self.knowledge.'''
        self.knowledge.append(string_input)
        
        