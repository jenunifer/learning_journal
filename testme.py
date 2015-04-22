import random

name=['nigel','gia','jen','sebastian','jen']
def persons(name):
    for person in name:
            if person is 'jen':
                print('Helllo there, %s') % person
                break
            else:
                 print('oh snap, move along %s') % person
                 continue

if __name__ == '__main__':
      persons(random.choice(name))


      
for i in range(5, 10):
       print(i)