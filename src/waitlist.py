# src/waitlist.py

class Waitlist:
    def __init__(self):
        self._queue = []

    def join(self, name: str):
        """Add a name to the waitlist."""
        self._queue.append(name)

    def to_list(self):
        """Return the current waitlist as a list."""
        return list(self._queue)

    def __len__(self):
        """Return the number of people in the waitlist."""
        return len(self._queue)

    def find(self, name: str) -> bool:
        """Check if a name exists in the waitlist."""
        return name in self._queue

    def cancel(self, name: str) -> bool:
        """Cancel the first occurrence of a name from the waitlist.
        Returns True if removed, False if not found.
        """
        try:
            self._queue.remove(name)
            return True
        except ValueError:
            return False

    def bump(self, name: str) -> bool:
        """Move a name to the front of the waitlist.
        Returns True if successful, False if not found.
        """
        if name in self._queue:
            self._queue.remove(name)
            self._queue.insert(0, name)
            return True
        return False
