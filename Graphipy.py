import matplotlib.pyplot as plt


class Graphipy(object):
    user_choice = ""

    x_coordinates = []
    y_coordinates = []

    x_min = 0.0
    x_max = 0.0
    y_min = 0.0
    y_max = 0.0

    x_scale_min = 0.0
    x_scale_max = 0.0
    y_scale_min = 0.0
    y_scale_max = 0.0

    num_of_coordinates = 0

    # first - initiated
    def initiated(self):
        print("Hello! \nWelcome To Graphify!")
        print("\nWe Are Going To Cook Up A Graph For You Based On Your Coordinates Data. B) :D\n"
              )
        print("Please Select An Option From The Menu Below On What You Want To Do:")
        print("1) Graphify! : Make New Graph")
        print("2) Exit.\n")

        user_input = input("Please Enter Your Choice. :)\n")

        self.user_choice = user_input

        # print("User input and choice are : " + user_input + " " + self.user_choice)
        return user_input

    # second - process, after initiated
    def process(self, p):
        if (p == "1"):
            print("\nGreat! You Chose Well!\n")

            # Taking X Scale

            print("Now To Get Started With Your Graph I Need Some Information First.")
            print("What Is The Minimum Range Of The X-Axis?")

            self.x_scale_min = float(input("Minimum X-Axis Scale: "))

            print("And The Maximum Value In The X-Axis?")

            self.x_scale_max = float(input("Maximum X-Axis Scale: "))

            # print(self.x_max)

            # Taking Y Scale
            print(
                "Now What Is The Minimum Range Of The Y-Axis?")

            self.y_scale_min = float(input("Minimum Y-Axis Scale: "))

            print("And The Maximum Value In The Y-Axis?")

            self.y_scale_max = float(input("Maximum Y-Axis Scale: "))

            print("Now Tell Me, How Many Coordinates Are You Going To Be Giving?")
            self.num_of_coordinates = int(input("Number Of Coordinates: "))

            # ##
            # x_list = coordinates_list(num_of_coordinates, "X")
            # y_list = coordinates_list(num_of_coordinates, "Y")

            x_list = []
            y_list = []

            self.coordinates_list(self.num_of_coordinates, self.x_coordinates, self.y_coordinates)

            prop_list = self.graph_prop()

            pen_color = prop_list[0]
            pen_size = prop_list[1]
            marker_symbol = prop_list[2]
            marker_symbol_color = prop_list[3]
            marker_symbol_size = prop_list[4]

            # print("X max:", self.x_scale_max, "X Min : ", self.x_scale_min, " Y Max", self.y_scale_max)
            # print("Y Min", self.y_scale_min, "x_coordinate_list", self.x_coordinates)
            # print("y_coordinate_list", self.y_coordinates, "pc=",pen_color, "ps=",pen_size, "ms=", marker_symbol, "msc=", marker_symbol_color)

            self.draw(x_max_scale=self.x_scale_max, x_min_scale=self.x_scale_min, y_max_scale=self.y_scale_max,
                      y_min_scale=self.y_scale_min, x_coordinate_list=self.x_coordinates,
                      y_coordinate_list=self.y_coordinates, pc=pen_color, ps=pen_size, ms=marker_symbol,
                      msc=marker_symbol_color, msz=marker_symbol_size)

        # def draw(self, x_max_scale, x_min_scale, x_coordinate_list, y_max_scale, y_min_scale, y_coordinate_list, pc, ps,
        #          ms, msc):

        return

    # third - cont of 2
    def coordinates_list(self, n, x_list, y_list):
        counter = 0
        listed_coordina = []

        while (counter < n):
            put = float(input("Please Enter Your " + str(counter + 1) + " Number X-Coordinate Value: "))
            x_list.append(put)
            put = float(input("Please Enter Your " + str(counter + 1) + " Number Y-Coordinate Value: "))
            y_list.append(put)
            counter = counter + 1

        return

    def graph_prop(self):
        print('What Color Do You Want Your Marker To Be?')
        print("Color Choices: ")
        print("\n1) b : blue \ng : Green \nr : Red \n c : Cyan \nm : Magenta \n y : Yello \nk : Black \nw : White")
        print("\n <Any Hex Value>")

        line_color = input("Your Color Choice: ")
        lc = line_color

        print("Please Enter The Marker Size. (Default : 1)")

        line_marker_size = float(input("Your Marker Size: "))
        lms = line_marker_size

        print("Please Select The Point Marker You Want.")
        print(
            "Point Markers Available: \n. : Point \n, : Pixel \no : Dot \n^ : Upringht Triangle \nv : Downright Triangle")
        print("\n< : Left Pointed Triangle \n> : Right Pointed Triangle \ns : Square \n* : Star \n+ : Plus \nx : x ")
        print("\nD : Diamond \nd : Thin Diamond ")

        symbol = input("Your Choice Of Marker: ")
        s = symbol

        print("\nWhat Size Do You Want Your Symbol To Be?")

        msz = int(input("Marker Symbol Size: "))

        print('What Color Do You Want Your Symbol To Be?')
        print("Color Choices: ")
        print("\n1) b : blue \ng : Green \nr : Red \n c : Cyan \nm : Magenta \n y : Yello \nk : Black \nw : White")
        print("<Any Hex Value>")

        symbol_color = input("Your Choice Of Symbol Color: ")
        sc = symbol_color

        list_of_props = [lc, lms, s, sc, msz]

        return list_of_props

    def save(self):
        print("Would You Like To Save This File? ")
        choice = input("Y : Yes, N : No")

        if (choice == "Y" or choice == "y"):
            print("What Would You Like To Save This Graph As?")
            file_name = input("File Name:  ")

            plt.savefig(file_name + ".png")

        return

    def draw(self, x_max_scale, x_min_scale, x_coordinate_list, y_max_scale, y_min_scale, y_coordinate_list, pc, ps, ms,
             msc, msz):

        marker = ms + msc
        plt.axis([x_min_scale, x_max_scale, y_min_scale, y_max_scale])

        plt.plot(x_coordinate_list, y_coordinate_list, pc, linewidth=ps)
        plt.plot(x_coordinate_list, y_coordinate_list, marker, markersize=msz)

        print("What Do You Want To Label The X-Axis?")
        x_Label = input("X-Axis Label: ")
        plt.xlabel(x_Label)

        print("What Do You Want To Label The Y-Axis?")
        y_Label = input("Y-Axis Label: ")
        plt.ylabel(y_Label)

        print("What Would You Want To Set The Title Of Your Graph?")
        title = input("Plot Title: ")

        plt.title(title)
        plt.grid(True)

        self.save()

        plt.show()

        return


##############################################################################################################












# pick = initiated()
# process(pick)
#
#
# pick = initiated()

# print(x_list)
# print(y_list)


# lines = plt.plot([1,2,3,4,5],[1,4,9,16,20],)
# lines = plt.plot([1,2,3,4,5],[1,4,9,16,20], "rd")
# plt.axis([0,6,0,20.5])
# plt.show()



# graph_prop(lc, ls, m, ms)

# print(lc)

# print("hey")

# x = "21"
# print(x)
# print(id(x))
# def test():
#     # print(id(x))
#      x= "24"
#      y = "21"
#      l = [x, y]
#      return l
#
# x = test()
# print(x)
# print(x[0])


# l = graph_prop()
# for i in l:
#     print(i)



# draw(10, 0, [1,2,3,4], 6, 1, [2,3,4,5], "r", 2, "o", "r")
#
# save()


g = Graphipy()
# g.initiated()
# x = []
# y = []
#
# print("x and y before : ", x, " & ", y)
#
# g.coordinates_list(5, x, y)
#
# print("x and y after : ", x, " & ", y)


# g.process("1")

g.process(g.initiated())


# g.draw(10, -10, [-1, -2, 0, 1, 2], 10, -10, [-1, -2, 0, 1, 2], "b", 3, "D", "r")
