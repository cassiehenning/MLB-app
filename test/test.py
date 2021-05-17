import pytest
import os
import datetime 
import json 
import requests

from app.MLB import div
from app.MLB import division

def test_division():
    result = division(204)
    assert result == "National League East"