from threading import Timer

my_timer = Timer(interval=1, function=my_function, args=(msg,))
my_timer.name = 'MyTimer'
my_timer.daemon = True
