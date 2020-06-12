#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.mec_mod_interfaces.shape import Shape


class BooleanShape(Shape):
    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         BooleanShape
                | 
                | Represents the shapes based on boolean operations on other
                | shapes.
                | It is the base object for add, assemble, intersect, remove, and split
                | shapes.
                | 
                | See also:
                |     Add, Assemble, Intersect, Remove, Split, Trim
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.boolean_shape = com_object

    @property
    def body(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Body() As Body (Read Only)
                | 
                |     Returns the inserted body.

        :return: Body
        """
        from pycatia.mec_mod_interfaces.body import Body
        return Body(self.boolean_shape.Body)

    def set_operated_object(self, i_reference_object):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetOperatedObject(Reference iReferenceObject)
                | 
                |     Modifies the Second Operand. input object to replace with Body or Volume

        :param Reference i_reference_object:
        :return: None
        """
        return self.boolean_shape.SetOperatedObject(i_reference_object.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_operated_object'
        # # vba_code = """
        # # Public Function set_operated_object(boolean_shape)
        # #     Dim iReferenceObject (2)
        # #     boolean_shape.SetOperatedObject iReferenceObject
        # #     set_operated_object = iReferenceObject
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_operating_volume(self, i_reference_object):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetOperatingVolume(Reference iReferenceObject)
                | 
                |     Swaps the operands. Both the Operands must be Volume. This is available
                |     only for Volume Add and Volume UnionTrim Operations

        :param Reference i_reference_object:
        :return: None
        """
        return self.boolean_shape.SetOperatingVolume(i_reference_object.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_operating_volume'
        # # vba_code = """
        # # Public Function set_operating_volume(boolean_shape)
        # #     Dim iReferenceObject (2)
        # #     boolean_shape.SetOperatingVolume iReferenceObject
        # #     set_operating_volume = iReferenceObject
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'BooleanShape(name="{self.name}")'
