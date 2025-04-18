class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Method to initialize the Television object.
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to change the power status of the Television object.
        Sets __status to either True/False.
        """
        self.__status = True if self.__status is False else False

    def mute(self) -> None:
        """
        Method to mute the Television object.
        Sets __muted to True/False.
        """
        if self.__status:
            self.__muted = True if self.__muted is False else False

    def channel_up(self) -> None:
        """
        Method to raise the __channel variable by 1.
        Will reset to MIN_CHANNEL if already at MAX_CHANNEL.
        """
        if self.__status:
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to lower the __channel variable by 1.
        Will reset to MAX_CHANNEL if already at MIN_CHANNEL.
        """
        if self.__status:
            if self.__channel > self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to raise the __volume variable by 1.
        Does nothing if already at MAX_VOLUME.
        """
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to lower the __volume variable by 1.
        Does nothing if already at MIN_VOLUME.
        """
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to return the status of the Television instance.
        :return: Power status, channel number, and volume of Television instance.
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume if self.__muted is False else 0}"