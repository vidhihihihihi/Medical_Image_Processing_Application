import PIL.Image
from kivy.properties import StringProperty
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from skimage.morphology import disk
from skimage.filters.rank import entropy
from plyer import filechooser
from kivy.properties import ListProperty
from skimage.io import imread
from skimage.color import rgb2gray

class MainWindow(Screen):
    selection = ListProperty([])
    sel = StringProperty("Not Selected")

    def choose(self):

        filechooser.open_file(on_selection=self.handle_selection)

    def handle_selection(self, selection):

        self.selection = selection
        self.sel = str(selection)
        self.ids.my_img.source = selection[0]
        WindowManager.manager_selection = selection
        print(str(selection))

    def bg_remover(self,src):

        len_ = src.shape[0]
        w = src.shape[1]
        for i in range(len_):
            for j in range(w):
                if src[i][j][0] < 100: src[i][j] = [0, 0, 0]
        return src

    def graytocolor(self,color, gray):
        for i in range(gray.shape[0]):
            for j in range(gray.shape[1]):
                if (gray[i][j] == 0): color[i][j] = [0, 0, 0]
        return color

    def Area(self,old_color_img, new_color_img):
        TA = 0
        RA = 0
        for i in range(old_color_img.shape[0]):
            for j in range(old_color_img.shape[1]):
                if (old_color_img[i][j][0] != 0): TA += 1
                if (new_color_img[i][j][0] != 0): RA += 1
        return (100 * RA / TA)

    def ip(self,selection):
        sh = imread(selection[0])
        real = imread(selection[0])

        sh = self.bg_remover(sh)
        real = self.bg_remover(real)
        sh_gray = rgb2gray(sh)
        entropy_image = entropy(sh_gray, disk(5))
        scaled_entropy = sh_gray / sh_gray.max()
        entropy_image = entropy(scaled_entropy, disk(5))
        scaled_entropy = entropy_image / entropy_image.max()
        mask = scaled_entropy > 0.8
        modified_img = sh_gray * mask

        color_img = self.graytocolor(sh, modified_img)


        #print("Area of infected region = %0.3f " % Area(real, color_img) + "%")
        edge = modified_img / modified_img.max()
        edge_mask = edge > 0.6
        final_modified_img = edge_mask * edge
        final_color_img = self.graytocolor(sh, final_modified_img)
        final_color_img = self.graytocolor(sh, final_modified_img)
        fcl = (PIL.Image.fromarray(final_color_img,'RGB')).save("./fin_img.jpg")
        WindowManager.final_image = ["./fin_img.jpg"]
        #print("Area of infected region = %0.3f " % Area(real, final_color_img) + "%")
        #f = plt.figure(num=None, figsize=(10, 8), dpi=60)

        calculated_area = self.Area(real, final_color_img)
        return str("{:.3f}".format(calculated_area))
        #f.add_subplot(1, 2, 1)
        #imshow(real, cmap='gray')
        #f.add_subplot(1, 2, 2)
        #imshow(final_color_img)
        #plt.show(block=True)

    def update(self,txt):
        return "Infected area :" + " " + txt


class LastWindow(Screen):

    def function_1(self,selection1,s):
        self.ids.my__img.source = selection1[0]
        self.ids.f__img.source = s[0]
    def show(self,s):
        return s

    pass
class ThirdWindow(Screen):

    pass

class WindowManager(ScreenManager):
    my_txt = StringProperty("Result")
    manager_selection = ListProperty([])
    final_image = ListProperty([])
    pass


kv = Builder.load_file("IP.kv")


class Medical_Image_ProcessingApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    Medical_Image_ProcessingApp().run()
