h = (1,3,5,6,9)
try:
    h.remove(9)
    ##h = a+'hi'
    ##h = float('hlo')

except AttributeError as e:
    print("AttributeError",e)
except TypeError as e:
    print("TypeError",e)
except ValurError as e:
    print("ValueError",e)
finally:
    print("process complete")
