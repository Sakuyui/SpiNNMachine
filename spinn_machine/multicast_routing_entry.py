from spinn_machine.exceptions import SpinnMachineAlreadyExistsException
from spinn_machine.exceptions import SpinnMachineInvalidParameterException


class MulticastRoutingEntry(object):
    """ Represents an entry in a multicast routing table
    """
    
    def __init__(self, key, mask, processor_ids, link_ids):
        """
        
        :param key: The routing key
        :type key: int
        :param mask: The route key mask
        :type mask: int
        :param processor_ids: The destination processor ids
        :type processor_ids: iterable of int
        :param link_ids: The destination link ids
        :type link_ids: iterable of int
        :raise spinn_machine.exceptions.SpinnMachineAlreadyExistsException:
                    * If processor_ids contains the same id more than once
                    * If link_ids contains the same id more than once
        """
        self._key = key
        self._mask = mask
        
        # Add processor ids, checking that there is only one of each
        self._processor_ids = set()
        for processor_id in processor_ids:
            if processor_id in self._processor_ids:
                raise SpinnMachineAlreadyExistsException(
                        "processor id", str(processor_id))
            self._processor_ids.add(processor_id)
        
        # Add link ids, checking that there is only one of each
        self._link_ids = set()
        for link_id in link_ids:
            if link_id in self._link_ids:
                raise SpinnMachineAlreadyExistsException(
                        "link id", str(link_id))
            self._link_ids.add(link_id)
    
    @property
    def key(self):
        """ The routing key
        
        :return: The routing key
        :rtype: int
        """
        return self._key
    
    @property
    def mask(self):
        """ The routing mask
        
        :return: The routing mask
        :rtype: int
        """
        return self._mask
    
    @property
    def processor_ids(self):
        """ The destination processor ids
        
        :return: An iterable of processor ids
        :rtype: iterable of int
        """
        return self._processor_ids
    
    @property
    def link_ids(self):
        """ The destination link ids
        
        :return: An iterable of link ids
        :rtype: iterable of int
        """
        return self._link_ids
    
    def merge(self, other_entry):
        """ Merges together two multicast routing entries.  The entry to merge\
            must have the same key and mask.  The merge will join the processor\
            ids and link ids from both the entries.  This could be used to add\
            a new destination to an existing route in a routing table.
            
        :param other_entry: The multicast entry to merge with this entry
        :type other_entry: :py:class:`MulticastRoutingEntry`
        :return: A new multicast routing entry with merged destinations
        :rtype: :py:class:`MulticastRoutingEntry`
        :raise spinn_machine.exceptions.SpinnMachineInvalidParameterException:\
                    If the key and mask of the other entry do not match
        """
        if other_entry.key != self.key:
            raise SpinnMachineInvalidParameterException(
                    "other_entry.key", hex(other_entry.key), 
                    "The key does not match {}".format(hex(self.key)))
        
        if other_entry.mask != self.mask:
            raise SpinnMachineInvalidParameterException(
                    "other_entry.mask", hex(other_entry.mask), 
                    "The mask does not match {}".format(hex(self.mask)))
        
        new_entry = MulticastRoutingEntry(
                self.key, self.mask, 
                self._processor_ids.union(other_entry.processor_ids), 
                self._link_ids.union(other_entry.link_ids))
        return new_entry
