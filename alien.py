alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'slow', 'colour': 
           'green', 'points': 5}

# Moving the alien

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
    
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("The " + alien_0['colour'] + " alien is now located at x-position " + 
      str(alien_0['x_position']))