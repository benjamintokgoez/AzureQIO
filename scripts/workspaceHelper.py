from azure.quantum import Workspace

#class for a WorkspaceHelper object to login and logout to Azure Quantum Worspace
#
#paremeters needed:
#subscription_id : the subscription id of your Azure subscription 
#resource group : the name of the resource group where the Azure Quantum workspace is deployed
#name : the name of the quantum workspace
#location : the location of the quantum workspace

class WorkspaceHelperInit(object):
    #Constructor for initializing the WorkspaceHelperInit Object
    def __init__(self, subscription_id, resource_group, name, location):
        self.subscription_id = subscription_id
        self.resource_group = resource_group
        self.name = name
        self.location = location
    #Get-method to get the workspace object
    #you need to call this function to get the right object from the SDK
    def getWorkspace(self) -> Workspace:
        workspace = Workspace(
            subscription_id=    self.subscription_id,
            resource_group=     self.resource_group, 
            name=               self.name, 
            location=           self.location  
        )

        return workspace
    #Login method
    #you need to use a login functionality to work with a Azure Quantum Workspace
    def login(self):
        self.login()
        print("Logged in to Azure Quantum Workspace")
    #Logout method
    def logout(self):
        self.logout()
        print("Logged out from Azure Quantum Workspace")

