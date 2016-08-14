class AbstractTag(object):

    __slots__ = [
        # the board address associted with this tag
        "_board_address",

        # the tag id associated with this tag
        "_tag",

        # the port number associated with this tag
        "_port"
    ]

    def __init__(self, board_address, tag, port):
        self._board_address = board_address
        self._tag = tag
        self._port = port

    @property
    def board_address(self):
        """ The board address of the tag
        """
        return self._board_address

    @property
    def tag(self):
        """ The tag id of the tag
        """
        return self._tag

    @property
    def port(self):
        """ The port of the tag
        """
        return self._port
