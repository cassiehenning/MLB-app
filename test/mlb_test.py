from attr import s
import pytest
import os

#mlb test

from app.MLB import div, division

# expect default environment variable setting of "CI=true" on Travis CI
# see: https://docs.travis-ci.com/user/environment-variables/#default-environment-variables
CI_ENV = os.getenv("CI") == "true"

@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server") # skips this test on CI
def test_division():
  div == 204
  division == "National League East"
  div == 200
  division == "American League West"
  div == 201
  division == "American League East"
  div == 202
  division == "American League Central"
  div == 203
  division == "National League West"
  div == 205
  division == "National League Central"