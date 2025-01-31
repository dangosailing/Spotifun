# Spotifun
Project tracking user spotify stats

## Dependencies
spotipy - handles auth and spotify api requests
flask - webserver interface and session storage of token
pandas, numpy - handle managing and visualizing data

## App flow
1. User is asked to register or login
2. When register direct to login
3. When login succeeds the user is asked to login to spotify
4. User is sesnt to homepage containing information (playlists etc)

## Checklist
1. basic app functionality *make it run ✅
2. basic routes ✅
3. base templates ✅
4. database ✅
5. user model ✅
6. write simple tests for routes (status codes)
7. register user -> func 
8. login user -> func

# Test guidelines
1. Arrange 
2. Act
3. Assert 
4. Cleanup

## What should be tested:
### Unit tests (small units of code)
Models
View
### Functional tests (key functionality)
Routes

#### Test scope
Create user via register and login

### FIXTURE
Initialize test in a known state
Defined as functions
Fixtures defined in tests/conftest.py
 Scope defines WHEN a fixture will be run
    scope = function - run once per test func (default)
    scope = class - run once per test class
    scope = module - run once per module/test file
    scope = function - run once per session (ie per call to pytest)