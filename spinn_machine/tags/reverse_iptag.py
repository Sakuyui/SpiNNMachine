from .abstract_tag import AbstractTag


class ReverseIPTag(AbstractTag):
    """ Used to hold data that is contained within an IPTag
    """

    __slots__ = [
        "_destination_x",
        "_destination_y",
        "_destination_p",
        "_sdp_port"
    ]

    # pylint: disable=too-many-arguments
    def __init__(self, board_address, tag, port, destination_x, destination_y,
                 destination_p, sdp_port=1):
        """
        :param board_address: \
            The ip address of the board on which the tag is allocated
        :type board_address: str or None
        :param tag: The tag of the SDP packet
        :type tag: int
        :param port: The UDP port on which SpiNNaker will listen for packets
        :type port: int
        :param destination_x: The x-coordinate of the chip to send packets to
        :type destination_x: int
        :param destination_y: The y-coordinate of the chip to send packets to
        :type destination_y: int
        :param destination_p: The id of the processor to send packets to
        :type destination_p: int
        :param sdp_port: The optional port number to use for SDP packets that\
            are formed on the machine (default is 1)
        :type sdp_port: int
        :raise None: No known exceptions are raised
        """
        super(ReverseIPTag, self).__init__(board_address, tag, port)
        self._destination_x = destination_x
        self._destination_y = destination_y
        self._destination_p = destination_p
        self._sdp_port = sdp_port

    @property
    def sdp_port(self):
        """ The SDP port number of the tag that these packets are to be\
            received on for the processor.
        """
        return self._sdp_port

    @property
    def destination_x(self):
        """ The destination x coordinate of a chip in the SpiNNaker machine\
            that packets should be sent to for this reverse IP tag.
        """
        return self._destination_x

    @property
    def destination_y(self):
        """ The destination y coordinate of a chip in the SpiNNaker machine\
            that packets should be sent to for this reverse IP tag.
        """
        return self._destination_y

    @property
    def destination_p(self):
        """ The destination processor id for the chip at (x,y) that packets\
            should be send to for this reverse IP tag
        """
        return self._destination_p

    def __repr__(self):
        return (
            "ReverseIPTag(board_address={}, tag={}, port={}, destination_x={},"
            " destination_y={}, destination_p={}, sdp_port={})".format(
                self._board_address, self._tag, self._port,
                self._destination_x, self._destination_y,
                self._destination_p, self._sdp_port))
