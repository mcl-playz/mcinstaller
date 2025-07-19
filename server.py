from paper import Paper
from pathlib import Path
import os
import shutil

CACHE_DIR = "./cache"
SERVERS_DIR = "./servers"

class Server:
    SOFTWARES = [Paper]
    def __init__(self, software, version, build, name, port):
        if not isinstance(software, *self.SOFTWARES):
            print(TypeError("Incorrect server software provided. Please provide the software in the form of a class"))
            return
        self.software = software
        self.version = version
        self.build = build
        self.name = name
        self.ram = "4G"
        self.port = port
    
    def install(self, overwrite: bool = False):
        """
        Creates the files necessary for a server to operate.
        Returns True if successful, False otherwise.
            """
        if not self.software:
            return False

        installDir = Path(SERVERS_DIR) / self.name

        if installDir.exists() and not overwrite:
            print("A server with that name already exists!")
            return False

        try:
            installDir.mkdir(parents=True, exist_ok=overwrite)
        except Exception as e:
            print(f"Failed to create server directory: {e}")
            return False

        self.serverDir = str(installDir)

        jarName = f"{self.software.identifier}-{self.version}-{self.build}.jar"
        jarCache = Path(CACHE_DIR) / jarName
        jarServer = installDir / jarName

        try:
            if not jarCache.exists():
                # Download and save to server dir, then copy to cache
                jarData = self.software.downloadBuild(self.version, self.build)
                jarServer.write_bytes(jarData)
                shutil.copy(jarServer, jarCache)
            else:
                shutil.copy(jarCache, jarServer)

            # Write required files
            (installDir / "eula.txt").write_text("eula=true")
            (installDir / "server.properties").write_text(f"server-port={self.port}")
            (installDir / "run.bat").write_text(
                f"@echo off\njava -Xms{self.ram} -Xmx{self.ram} -jar {jarName} nogui"
            )

            return True

        except Exception as e:
            print(f"Installation failed: {e}")
            return False