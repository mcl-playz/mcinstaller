# https://api.papermc.io/v2/projects/${PROJECT}/versions/${MINECRAFT_VERSION}
from responseHandler import ResponseHandler
import requests
import typing

class Paper:
    baseURL = "https://api.papermc.io/v2/projects/paper"
    identifier = "paper"

    def getSupportedVersions(self):
        response = requests.get(self.baseURL)
        if not ResponseHandler.ensureSafeStatus(response): return

        data = ResponseHandler.parse(response)
        if data == None: return

        versions = data["versions"]
        return versions

    def getVersion(self, version):
        url = f"{self.baseURL}/versions/{version}"
        response = requests.get(url)
        if not ResponseHandler.ensureSafeStatus(response): return

        data = ResponseHandler.parse(response)
        if data == None: return
        
        return data
    
    def getBuilds(self, version):
        return self.getVersion(version)["builds"]

    def downloadBuild(self, version, buildNumber: int):
        jarName = f"paper-{version}-{buildNumber}.jar"
        url = f"{self.baseURL}/versions/{version}/builds/{buildNumber}/downloads/{jarName}"
        
        response = requests.get(url)
        if not ResponseHandler.ensureSafeStatus(response): return

        return response.content
