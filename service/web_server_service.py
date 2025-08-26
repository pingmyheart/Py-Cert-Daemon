from abc import ABC, abstractmethod


class WebServerService(ABC):
    @abstractmethod
    def reload(self) -> None:
        pass

    @abstractmethod
    def web_server(self) -> str:
        pass


class ApacheWebServerService(WebServerService):
    def web_server(self) -> str:
        return "apache"

    def reload(self):
        import subprocess
        subprocess.run(["systemctl", "reload", "apache2"], check=True)


class NginxWebServerService(WebServerService):
    def web_server(self) -> str:
        return "nginx"

    def reload(self):
        import subprocess
        subprocess.run(["systemctl", "reload", "nginx"], check=True)
