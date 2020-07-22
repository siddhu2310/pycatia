#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.parameter import Parameter


class StrParam(Parameter):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeInterfaces.Parameter
                |                         StrParam
                | 
                | Represents the string parameter.
                | The following example shows how to create it:
                | 
                | 	Dim CATDocs As Documents
                |  Set CATDocs = CATIA.Documents
                |  Dim part1 As Document
                |  Set part1   = CATDocs.Add("CATPart")
                |  Dim material As String
                |  Set material = part1.Parameters.CreateString("material", "glass")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.str_param = com_object

    @property
    def value(self) -> str:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)
                | o Property Value() As CATBSTR
                | 
                |     Returns or sets the string parameter value.
                | 
                |     Example:
                |         This example returns in myValue the value of the string parameter
                |         material:
                | 
                |          
                | 
                |          myValue = material.Value

        :return: str
        :rtype: str
        """

        return self.str_param.Value

    @value.setter
    def value(self, value: str):
        """
        :param str value:
        """

        self.str_param.Value = value

    def get_enumerate_values(self, o_safe_array: tuple) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub GetEnumerateValues(CATSafeArrayVariant oSafeArray)
                | 
                |     Returns an array containing the different values that the real param can
                |     take in the case of multiple values.
                | 
                |     Example:
                | 
                |          Dim enumValues () as Variant
                |          ReDim enumValues (aStrParameter.GetEnumerateValuesSize() -
                |          1)
                |          aStrParameter.GetEnumerateValues(enumValues)
                |          For i = LBound(enumValues) to UBound(enumValues)
                |            ...
                |          Next

        :param tuple o_safe_array:
        :return: None
        :rtype: None
        """
        return self.str_param.GetEnumerateValues(o_safe_array)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_enumerate_values'
        # # vba_code = """
        # # Public Function get_enumerate_values(str_param)
        # #     Dim oSafeArray (2)
        # #     str_param.GetEnumerateValues oSafeArray
        # #     get_enumerate_values = oSafeArray
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_enumerate_values_size(self) -> int:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Func GetEnumerateValuesSize() As long
                | 
                |     Returns the number of enumerate values.

        :return: int
        :rtype: int
        """
        return self.str_param.GetEnumerateValuesSize()

    def set_enumerate_values(self, i_safe_array: tuple) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SetEnumerateValues(CATSafeArrayVariant iSafeArray)
                | 
                |     Sets an array containing the different values that the StrParam object can
                |     take in the case of multiple values.
                | 
                |     Parameters:
                | 
                |         The
                |             array of enumerated values.

        :param tuple i_safe_array:
        :return: None
        :rtype: None
        """
        return self.str_param.SetEnumerateValues(i_safe_array)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_enumerate_values'
        # # vba_code = """
        # # Public Function set_enumerate_values(str_param)
        # #     Dim iSafeArray (2)
        # #     str_param.SetEnumerateValues iSafeArray
        # #     set_enumerate_values = iSafeArray
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def suppress_enumerate_values(self) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445))
                | o Sub SuppressEnumerateValues()
                | 
                |     Resets the status of the object to a single value object.

        :return: None
        :rtype: None
        """
        return self.str_param.SuppressEnumerateValues()

    def __repr__(self):
        return f'StrParam(name="{ self.name }")'
