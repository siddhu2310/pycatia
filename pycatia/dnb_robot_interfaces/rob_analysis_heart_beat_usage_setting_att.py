#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.setting_controller import SettingController


class RobAnalysisHeartBeatUsageSettingAtt(SettingController):

    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         RobAnalysisHeartBeatUsageSettingAtt
                | 
                | Interface to handle the parameter used to set as an option, to either enable or
                | disable robot heart beat rate while motion planning, in the
                | Infrastructure-DELMIA Infrastructure-Robot Analysis Tools Options Tab
                | page.
                | Role: This interface is implemented by a component which is one among the
                | controller properties of Robot Analysis Tools Options parameter settings. Here
                | is the parameter to use and its meaning:
                | 
                |     EnableHeartBeat: defines whether to enable robot motion planning based on
                |     robot heart beat rate
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.rob_analysis_heart_beat_usage_setting_att = com_object

    @property
    def enable_heart_beat(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property EnableHeartBeat() As boolean
                | 
                | 
                |     Role:Enables or Disables the Heart Beat Rate while the robot motion is
                |     planned return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :rtype: bool
        """

        return self.rob_analysis_heart_beat_usage_setting_att.EnableHeartBeat

    @enable_heart_beat.setter
    def enable_heart_beat(self, value: bool):
        """
        :param bool value:
        """

        self.rob_analysis_heart_beat_usage_setting_att.EnableHeartBeat = value

    def get_enable_heart_beat_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetEnableHeartBeatInfo(CATBSTR ioAdminLevel,
                | CATBSTR ioLocked) As boolean
                | 
                |     Retrieves environment informations for the SingularColor
                |     parameter.
                |     Role:Retrieves the state of the SingularColor parameter in the current
                |     environment.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         ioLocked
                |             Indicates if the parameter has been locked. 
                | 
                |     Returns:
                |         Indicates if the parameter has been explicitly modified or remain to
                |         the administrated value.

        :param str io_admin_level:
        :param str io_locked:
        :rtype: bool
        """
        return self.rob_analysis_heart_beat_usage_setting_att.GetEnableHeartBeatInfo(io_admin_level, io_locked)

    def set_enable_heart_beat_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetEnableHeartBeatLock(boolean iLocked)
                | 
                |     Locks or unlocks the SingularColor parameter.
                |     Role:Locks or unlocks the SingularColor parameter if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter.

        :param bool i_locked:
        :rtype: None
        """
        return self.rob_analysis_heart_beat_usage_setting_att.SetEnableHeartBeatLock(i_locked)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_enable_heart_beat_lock'
        # # vba_code = """
        # # Public Function set_enable_heart_beat_lock(rob_analysis_heart_beat_usage_setting_att)
        # #     Dim iLocked (2)
        # #     rob_analysis_heart_beat_usage_setting_att.SetEnableHeartBeatLock iLocked
        # #     set_enable_heart_beat_lock = iLocked
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'RobAnalysisHeartBeatUsageSettingAtt(name="{ self.name }")'
