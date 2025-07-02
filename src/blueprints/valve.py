"""Generic Valve Base Class"""
import logging

from typing import Union


class Valve:

    def __init__(self, name: str = None):
        logger_name = self.__class__.__name__ + (f".{name}" if name else "")
        self.log = logging.getLogger(logger_name)


class IsolationValve(Valve):
    """isolation valve that can open and close."""

    def open(self) -> None:
        self._open()

    def close(self) -> None:
        self.close()

    def _open(self) -> None:
        raise NotImplementedError

    def _close(self) -> None:
        raise NotImplementedError



class SolenoidValve(Valve):
    """Solenoid valve that can be energized and deenergized."""

    def energize(self) -> None:
        self.log.debug("Energizing.")
        self._energize()

    def deenergize(self) -> None:
        self.log.debug("De-energizing.")
        self._deenergize()

    def _energize(self) -> None:
        raise NotImplementedError

    def _deenergize(self) -> None:
        raise NotImplementedError



class NCValve(IsolationValve):
    """Normally-Closed isolation valve. De-energized state is closed."""
    pass


class NOValve(IsolationValve):
    """Normally-Open isolation valve. De-energized state is open."""
    pass


class NCSolenoidValve(NCValve, SolenoidValve):
    """Normally-Closed solenoid valve."""

    def _open(self):
        self.energize()

    def _close(self):
        self.deenergize()


class NOSolenoidValve(NOValve, SolenoidValve):
    """Normally-Open solenoid valve."""

    def _open(self):
        self.deenergize()

    def _close(self):
        self.energize()


class ThreeTwoValve(Valve):
    """3/2 valve that can switch a common port between two ways."""

    def select_way(self, way: Union[int, str]) -> None:
        """Select way 'A' (0) or 'B' (1)."""

    def _select_way(self, way: Union[int, str]) -> None:
        raise NotImplementedError


class ThreeTwoSolenoidValve(SolenoidValve):
    pass


# Simulated Classes

class SimNCValve(NCValve):

    def _open(self) -> None:
        pass

    def _close(self) -> None:
        pass


class SimNOValve(NOValve):

    def _open(self) -> None:
        pass

    def _close(self) -> None:
        pass


class SimNCSolenoidValve(NCSolenoidValve):

    def _open(self) -> None:
        pass

    def _close(self) -> None:
        pass

    def _energize(self) -> None:
        pass

    def _deenergize(self) -> None:
        pass


class SimNOSolenoidValve(NOSolenoidValve):

    def _open(self) -> None:
        pass

    def _close(self) -> None:
        pass

    def _energize(self) -> None:
        pass

    def _deenergize(self) -> None:
        pass

