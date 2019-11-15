import pygame
from pygame.locals import *
from typing import Tuple


class TextField:
    """
    A class to represent a text field

    Things it needs to do:
        Method to parse a key press event
        Method to set textfield active
        Method to set textfield inactive

    Attributes:
        string text: the text of this textfield
        string format: the set of characters that the text is restricted to
        boolean active: sets whether the user can type into the textfield
            (When the user clicks on the field)

        The coordinates:
        int _center_x
        int _center_y
        int _font_size: the font size


    Methods:
        Draw: Draws the textfield on the screen (blit text?)
        setFormat: Restricts the characters that the text can contain
            by using a string

    Subclasses:
        NumericTextField: a TextField where the user can only input numbers
        AlphaTextField: a TextField where the user can only input letters (no
            numbers, symbols, etc...)
        AlphaNumTextField: a TextField where the user can only input letters
            and/or numbers

    """

    _center_x: int
    _center_y: int
    _width: int
    _height: int
    _font_size: int
    _text: str
    _format: str
    _active: bool
    _range: Tuple[Tuple[int, int]]
    _screen: pygame.display
    _color: Tuple[int, int, int]
    _rect: pygame.Rect
    _char_limit: int
    _is_drawn: bool
    _text_blinker: pygame.Rect

    def __init__(self, x: int, y: int, font_size: int, screen, width=150,
                 height=70, is_drawn=True):
        self._center_x = x
        self._center_y = y
        self._font_size = font_size
        self._active = False
        self._format = ""
        self._screen = screen
        self._color = (250, 0, 0)
        self._font_color = (0, 0, 0)
        self._text = ""
        self._char_limit = 6
        self._is_drawn = is_drawn

        # TODO: Add changeable width/height attribute
        self._width = width
        self._height = height

        # Set the range values of the box
        range_x = (self._center_x - (self._width//2),
                   self._center_x + (self._width//2))
        range_y = (self._center_y - (self._height // 2),
                   self._center_y + (self._height // 2))
        self._range = (range_x, range_y)

        # Create the rectangle
        self._rect = pygame.Rect(self._range[0][0], self._range[0][0],
                                 self._width, self._height)

    def active_check(self, e: pygame.event.EventType) -> None:
        """Checks for the mouse click event, if it is on the field, activate
        it.
        """
        mouse_coords = pygame.mouse.get_pos()
        if e.type == MOUSEBUTTONDOWN and self.check_collision(mouse_coords):
            self._active = True
            print(self._active)
        elif e.type == MOUSEBUTTONDOWN and not \
                self.check_collision(mouse_coords):
            self._active = False
            print(self._active)

    def key_check(self, e: pygame.event.Event) -> None:
        """
        Checks if a key was pressed, and adds it to the string if the key is
        in the format and the field is active
        :param e: a pygame event
        """

        if e.type == KEYDOWN and (chr(e.key) in self._format
                                  or not self._format) and \
                self._active and len(self._text) < self._char_limit:
            self._text += chr(e.key)

    def check_change(self, e: pygame.event.Event) -> None:
        """
        Check for a change in the textField (given an event)
        :param e: pygame.event.Event
        """
        self.key_check(e)
        self.active_check(e)

    def draw(self) -> None:
        """
        draws the text field to the screen
        """
        if self._is_drawn:
            # Draw the rectangle
            pygame.draw.rect(self._screen, self._color, self._rect)

            # Draw the text to the screen
            text_font = pygame.font.Font(None, self._font_size)
            disp = text_font.render(self._text, 1, self._font_color)
            disp_pos = disp.get_rect(centerx=self._center_x,
                                     centery=self._center_y)
            self._screen.blit(disp, disp_pos)

    def get_text(self) -> str:
        """
        return: the current value of the text field
        """
        return self._text

    def check_collision(self, coords: Tuple[int, int]) -> bool:
        """
        Checks whether the given coordinates are in this text field

        :param coords: A tuple of coordinates (x, y)
        :return: true/false depending on whether the coordinates are in
        this text field or not
        """
        return self._rect.collidepoint(coords)

    def set_format(self, new_format: str) -> None:
        """
        Sets the format of this text field
        :param new_format: a string representation of all the characters allowed
        in this format
        """
        self._format = new_format

    def set_color(self, new_color: Tuple[int, int, int]) -> None:
        """
        Sets the color of the textbox
        :param new_color: an RGB tuple
        """
        self._color = new_color

    def set_font_color(self, new_color: Tuple[int, int, int]) -> None:
        """
        Sets the color of the font
        :param new_color: an RGB tuple
        """
        self._font_color = new_color

    def set_char_limit(self, limit: int) -> None:
        """
        Sets the character limit for the text field
        :param limit: the character limit, in integers
        """
        self._char_limit = limit

    def clear_field(self) -> None:
        """
        Clears the text field only if the field is active
        """
        if self._active:
            self._text = ""

    def set_clear(self) -> None:
        """
        Clears the text field only if the field is active
        """

        self._text = ""

    def get_active(self) -> bool:
        """
        :returns: Whether this text field is active
        """
        return self._active

    def set_dimensions(self, width: int, height: int) -> None:
        """
        Sets the width and height of this text field
        :param width: an int representing width
        :param height: an int representing height
        """
        self._width = width
        self._height = height

    def set_drawn(self, state: bool) -> None:
        """
        Sets the state of whether the textfield will be drawn

        :param state: a boolean representing whether the object will be drawn
        """
        self._is_drawn = state
