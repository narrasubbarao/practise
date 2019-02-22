def dispaly():
    print("I am display")
    print("How are you")

show = dispaly #
dispaly()
show()

del dispaly

# dispaly() Error (display is deleted)
show()