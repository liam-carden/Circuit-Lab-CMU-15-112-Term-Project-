
# *General Button class that controls a button which controls documentation
class Button:
    # Constructor for the Button
    def __init__(self, x0, y0, x1, y1, documentation, text, color):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.enabled = False
        self.halfX = self.x0 + (self.x1-self.x0) / 2
        self.halfY = self.y0 + (self.y1-self.y0) / 2
        self.documentation = documentation
        self.text = text
        self.color = color

    # swaps the button's enabled state when it is pressed
    def mousePressed(self, eventX, eventY):
        if self.x0 <= eventX <= self.x1 and self.y0 <= eventY <= self.y1:
            self.enabled = not self.enabled
            return True

    # draws the button
    # draws the documentation overlay if enabled is set to True
    def redrawButton(self, app, canvas):
        canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill = self.color)
        canvas.create_text(self.halfX, self.halfY, anchor = 'c', text = self.text)
        if self.enabled:
            canvas.create_rectangle(0, 0 , app.width *(3.75 / 5), 
                                    app.height * (4 / 5), fill = self.color)
            canvas.create_text(260,320,text = self.documentation,
                               font = f"Arial 10 bold", fill = 'black')