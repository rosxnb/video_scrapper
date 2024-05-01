class Logger:
    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passes here
        if not msg.startswith("[debug] "):
            return self.info(msg)

        pass

    def info(self, msg):
        if msg.startswith("[download] [Filters] "):
            print(f"FATAL: {msg}")

    def warning(self, msg):
        # print(f"warning: {msg =}")
        pass

    def error(self, msg):
        # print(f"error: {msg =}")
        pass
