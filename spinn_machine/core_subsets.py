from collections import OrderedDict
from spinn_machine.core_subset import CoreSubset


class CoreSubsets(object):
    """ Represents a group of CoreSubsets, with a maximum of one per chip
    """

    __slots__ = ("_core_subsets")

    def __init__(self, core_subsets=None):
        """
        :param core_subsets: An iterable of cores for each desired chip
        :type core_subsets: iterable of\
                    :py:class:`spinn_machine.core_subset.CoreSubset`
        :raise spinnman.exceptions.SpinnmanInvalidParameterException: If there\
                    is more than one subset with the same core x and y\
                    coordinates
        """
        self._core_subsets = OrderedDict()
        if core_subsets is not None:
            for core_subset in core_subsets:
                self.add_core_subset(core_subset)

    def add_core_subset(self, core_subset):
        """ Add a core subset to the set

        :param core_subset: The core subset to add
        :type core_subset: :py:class:`spinn_machine.core_subset.CoreSubset`
        :return: Nothing is returned
        :rtype: None
        """
        self._core_subsets[(core_subset.x, core_subset.y)] = core_subset

    def add_processor(self, x, y, processor_id):
        """ Add a processor on a given chip to the set

        :param x: The x-coordinate of the chip
        :type x: int
        :param y: The y-coordinate of the chip
        :type y: int
        :param processor_id: A processor id
        :type processor_id: int
        :return: Nothing is returned
        :rtype: None
        """
        if (x, y) not in self._core_subsets:
            self.add_core_subset(CoreSubset(x, y, []))
        self._core_subsets[(x, y)].add_processor(processor_id)

    def is_chip(self, x, y):
        """ Determine if the chip with coordinates (x, y) is in the subset

        :param x: The x-coordinate of a chip
        :type x: int
        :param y: The y-coordinate of a chip
        :type y: int
        :return: True if the chip with coordinates (x, y) is in the subset
        :rtype: bool
        """
        return (x, y) in self._core_subsets

    def is_core(self, x, y, processor_id):
        """ Determine if there is a chip with coordinates (x, y) in the\
            subset, which has a core with the given id in the subset

        :param x: The x-coordinate of a chip
        :type x: int
        :param y: The y-coordinate of a chip
        :type y: int
        :param processor_id: The id of a core
        :type processor_id: int
        :return: True if there is a chip with coordinates (x, y) in the\
                    subset, which has a core with the given id in the subset
        """
        if (x, y) not in self._core_subsets:
            return False
        return processor_id in self._core_subsets[(x, y)]

    @property
    def core_subsets(self):
        """ The one-per-chip subsets

        :return: Iterable of core subsets
        :rtype: iterable of :py:class:`spinn_machine.core_subset.CoreSubset`
        """
        return self._core_subsets.itervalues()

    def get_core_subset_for_chip(self, x, y):
        """ Get the core subset for a chip

        :param x: The x-coordinate of a chip
        :type x: int
        :param y: The y-coordinate of a chip
        :type y: int
        :return: The core subset of a chip, which will be empty if not added
        :rtype: :py:class:`spinn_machine.core_subset.CoreSubset`
        """
        if (x, y) not in self._core_subsets:
            return CoreSubset(x, y, [])
        return self._core_subsets[(x, y)]

    def __iter__(self):
        """ Iterable of core_subsets
        """
        return self._core_subsets.itervalues()

    def __len__(self):
        """ The total number of processors that are in these core subsets
        """
        counter = 0
        for (x, y) in self._core_subsets:
            counter += len(self._core_subsets[(x, y)])
        return counter
