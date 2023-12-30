# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import json
import math
import statistics
from datetime import datetime

expenses = {
    "2023-01": {
        "01": {
            "food": [ 22.11, 43, 11.72, 2.2, 36.29, 2.5, 19 ],
            "fuel": [ 210.22 ]
        },
        "09": {
            "food": [ 11.9 ],
            "fuel": [ 190.22 ]
        }
    },
    "2023-03": {
        "07": {
            "food": [ 20, 11.9, 30.20, 11.9 ]
        },
        "04": {
            "food": [ 10.20, 11.50, 2.5 ],
            "fuel": [ 40, 50 ]
        }
    },
    "2023-04": {}
}

class Expenses():
    def __init__(self, input_data : dict) -> object:
        self.data = input_data
        self.preprocessed_data = self.__preprocess__()
        self.result = []
    
    def __call__(self, mode = "median"):
        assert(type(mode) == str)
        if mode == "median":
            for key in self.preprocessed_data.keys():
               self.result += self.preprocessed_data.get(key)
            self.result = sorted(self.result)
            self.result = statistics.median(self.result)
        return self.result
    
    def __preprocess__(self) -> dict:
        aux_data = self.data
        first_week = lambda key_month, month_dict : {day : month_dict.get(day) for day in [key if int(key) <= 7 - datetime.strptime(key_month + "-" + "01", '%Y-%m-%d').date().weekday() else False for key in month_dict.keys()]}
        preprocessed_data = {key_month: {day : dict_days} for key_month in list(aux_data.keys()) for day, dict_days in first_week(key_month, aux_data.get(key_month)).items()  }
        for key in preprocessed_data.keys():
            if False in preprocessed_data[key].keys():
                preprocessed_data[key].pop(False, None)
        keys = list(preprocessed_data.keys()).copy()
        for key in keys:
            if not preprocessed_data[key]:
                preprocessed_data.pop(key, None)
        preprocessed_data = {month_key : expenses["food"] + expenses["fuel"] for month_key, days in preprocessed_data.items() for key, expenses in days.items()}

        return preprocessed_data
    
def get_median_of_first_week_expenses(expenses = expenses):
    assert(type(expenses) == dict)
    expenses_ = Expenses(expenses)
    result = expenses_()
    return result

print(get_median_of_first_week_expenses(expenses))