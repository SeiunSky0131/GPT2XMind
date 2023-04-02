import answer_getter
import xmind_interface

if __name__ == "__main__":
    print("----------Welcome to the xmind interface. Please input the name of the xmind file you want to manipulate.----------\n")
    filename = input()
    xmind_interface.manipulate_xmind(filename)


